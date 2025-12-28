"""Unit tests for communication protocol."""

import unittest
from src.core.protocol.message import (
    Message,
    MessageType,
    PatternMessage,
    ConfigMessage,
    StatusResponseMessage,
    ErrorMessage,
    ConfigType,
    ErrorCode
)


class TestMessage(unittest.TestCase):
    """Test message serialization/deserialization."""
    
    def test_message_serialize_deserialize(self):
        """Test message serialization and deserialization."""
        original = Message(MessageType.HEARTBEAT, b'test')
        data = original.serialize()
        deserialized = Message.deserialize(data)
        
        self.assertIsNotNone(deserialized)
        self.assertEqual(deserialized.msg_type, MessageType.HEARTBEAT)
        self.assertEqual(deserialized.payload, b'test')
    
    def test_pattern_message(self):
        """Test pattern message."""
        events = [
            {'actuator': 0, 'time_offset': 0, 'duration': 150, 'intensity': 200}
        ]
        msg = PatternMessage('E', events)
        data = msg.serialize()
        
        # Verify message type
        self.assertEqual(data[0], MessageType.PATTERN)
    
    def test_config_message(self):
        """Test configuration message."""
        msg = ConfigMessage(ConfigType.INTENSITY, 200)
        data = msg.serialize()
        
        deserialized = Message.deserialize(data)
        self.assertIsNotNone(deserialized)
        self.assertEqual(deserialized.msg_type, MessageType.CONFIG)
        
        config_type, value = ConfigMessage.deserialize_config(deserialized.payload)
        self.assertEqual(config_type, ConfigType.INTENSITY)
        self.assertEqual(value, 200)
    
    def test_status_response_message(self):
        """Test status response message."""
        msg = StatusResponseMessage(80, -50, 0, 5)
        data = msg.serialize()
        
        deserialized = Message.deserialize(data)
        self.assertIsNotNone(deserialized)
        
        battery, quality, error, queue = StatusResponseMessage.deserialize_status(deserialized.payload)
        self.assertEqual(battery, 80)
        self.assertEqual(queue, 5)
    
    def test_error_message(self):
        """Test error message."""
        msg = ErrorMessage(ErrorCode.QUEUE_FULL, "Queue is full")
        data = msg.serialize()
        
        deserialized = Message.deserialize(data)
        self.assertIsNotNone(deserialized)
        self.assertEqual(deserialized.msg_type, MessageType.ERROR)


if __name__ == '__main__':
    unittest.main()


