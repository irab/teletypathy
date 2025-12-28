"""
Communication protocol implementation for Teletypathy.

Handles message serialization/deserialization and protocol communication.
"""

from typing import List, Optional
from enum import IntEnum
import struct


class MessageType(IntEnum):
    """Message types for protocol."""
    PATTERN = 0x01
    PATTERN_BATCH = 0x02
    CONFIG = 0x03
    STATUS_REQUEST = 0x04
    STATUS_RESPONSE = 0x05
    HEARTBEAT = 0x06
    ERROR = 0x07
    RESET = 0x08


class ConfigType(IntEnum):
    """Configuration types."""
    INTENSITY = 0x01
    SPEED = 0x02
    PATTERN_SPACING = 0x03


class ErrorCode(IntEnum):
    """Error codes."""
    INVALID_MESSAGE = 0x01
    QUEUE_FULL = 0x02
    INVALID_ACTUATOR = 0x03
    INVALID_PATTERN = 0x04
    DEVICE_BUSY = 0x05
    LOW_BATTERY = 0x06


class Message:
    """Base message class."""
    
    def __init__(self, msg_type: MessageType, payload: bytes = b''):
        """Initialize message."""
        self.msg_type = msg_type
        self.payload = payload
    
    def serialize(self) -> bytes:
        """Serialize message to bytes."""
        header = struct.pack('BB', self.msg_type, len(self.payload))
        checksum = self._calculate_checksum(header + self.payload)
        return header + self.payload + struct.pack('B', checksum)
    
    @staticmethod
    def deserialize(data: bytes) -> Optional['Message']:
        """Deserialize message from bytes."""
        if len(data) < 3:  # Header (2) + checksum (1)
            return None
        
        msg_type, payload_len = struct.unpack('BB', data[:2])
        if len(data) < 3 + payload_len:
            return None
        
        payload = data[2:2+payload_len]
        checksum = data[2+payload_len]
        
        # Verify checksum
        calculated_checksum = Message._calculate_checksum(data[:2+payload_len])
        if checksum != calculated_checksum:
            return None
        
        return Message(MessageType(msg_type), payload)
    
    @staticmethod
    def _calculate_checksum(data: bytes) -> int:
        """Calculate simple checksum."""
        return sum(data) & 0xFF


class PatternMessage(Message):
    """Pattern message (single character pattern)."""
    
    def __init__(self, char: str, pattern_events: List[dict]):
        """
        Initialize pattern message.
        
        Args:
            char: Character (ASCII)
            pattern_events: List of actuator events
        """
        # Build payload: char (1 byte) + pattern data
        char_byte = ord(char) if len(char) == 1 else 0
        pattern_data = self._serialize_pattern(pattern_events)
        payload = struct.pack('B', char_byte) + pattern_data
        
        super().__init__(MessageType.PATTERN, payload)
        self.char = char
        self.pattern_events = pattern_events
    
    @staticmethod
    def _serialize_pattern(events: List[dict]) -> bytes:
        """Serialize pattern events to bytes."""
        # Format: [actuator_count: 1 byte] [events...]
        # Each event: [actuator_id: 1] [time_offset: 2] [duration: 1] [intensity: 1]
        data = struct.pack('B', len(events))
        for event in events:
            data += struct.pack('BHHB', 
                event['actuator'],
                event['time_offset'],
                event['duration'],
                event.get('intensity', 200)
            )
        return data
    
    @staticmethod
    def deserialize_pattern(data: bytes) -> tuple:
        """Deserialize pattern from message payload."""
        if len(data) < 2:  # char (1) + actuator_count (1)
            return None, None
        
        char = chr(data[0])
        actuator_count = data[1]
        
        events = []
        offset = 2
        for _ in range(actuator_count):
            if len(data) < offset + 5:  # actuator (1) + time_offset (2) + duration (1) + intensity (1)
                break
            actuator, time_offset, duration, intensity = struct.unpack('BHHB', data[offset:offset+5])
            events.append({
                'actuator': actuator,
                'time_offset': time_offset,
                'duration': duration,
                'intensity': intensity
            })
            offset += 5
        
        return char, events


class PatternBatchMessage(Message):
    """Pattern batch message (multiple patterns)."""
    
    def __init__(self, patterns: List[tuple]):
        """
        Initialize pattern batch message.
        
        Args:
            patterns: List of (char, pattern_events) tuples
        """
        payload = struct.pack('B', len(patterns))
        for char, events in patterns:
            char_byte = ord(char) if len(char) == 1 else 0
            pattern_data = PatternMessage._serialize_pattern(events)
            payload += struct.pack('B', char_byte) + struct.pack('H', len(pattern_data)) + pattern_data
        
        super().__init__(MessageType.PATTERN_BATCH, payload)
        self.patterns = patterns


class ConfigMessage(Message):
    """Configuration message."""
    
    def __init__(self, config_type: ConfigType, value: int):
        """Initialize configuration message."""
        payload = struct.pack('BB', config_type, value)
        super().__init__(MessageType.CONFIG, payload)
        self.config_type = config_type
        self.value = value
    
    @staticmethod
    def deserialize_config(data: bytes) -> tuple:
        """Deserialize configuration from message payload."""
        if len(data) < 2:
            return None, None
        config_type, value = struct.unpack('BB', data[:2])
        return ConfigType(config_type), value


class StatusResponseMessage(Message):
    """Status response message."""
    
    def __init__(self, battery_level: int, connection_quality: int, error_code: int, queue_length: int):
        """Initialize status response message."""
        payload = struct.pack('BBBB', battery_level, connection_quality, error_code, queue_length)
        super().__init__(MessageType.STATUS_RESPONSE, payload)
        self.battery_level = battery_level
        self.connection_quality = connection_quality
        self.error_code = error_code
        self.queue_length = queue_length
    
    @staticmethod
    def deserialize_status(data: bytes) -> tuple:
        """Deserialize status from message payload."""
        if len(data) < 4:
            return None, None, None, None
        battery, quality, error, queue = struct.unpack('BBBB', data[:4])
        return battery, quality, error, queue


class ErrorMessage(Message):
    """Error message."""
    
    def __init__(self, error_code: ErrorCode, message: str = ''):
        """Initialize error message."""
        msg_bytes = message.encode('ascii', errors='ignore')[:255]
        payload = struct.pack('B', error_code) + msg_bytes
        super().__init__(MessageType.ERROR, payload)
        self.error_code = error_code
        self.message = message


