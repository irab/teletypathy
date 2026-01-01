"""
Single-byte encoding for passive learning.

Encodes characters as 8-bit patterns using all 8 actuators simultaneously,
optimized for low latency and passive/subconscious learning.
"""

from typing import List, Optional
from .pattern import Pattern, ActuatorEvent


class SingleByteEncoder:
    """
    Single-byte encoder optimized for passive learning.
    
    Encodes each character as 8-bit pattern (all actuators simultaneously)
    with very short duration (50-100ms) for low latency and non-intrusive patterns.
    
    Designed for passive learning: device worn constantly, patterns learned
    subconsciously through continuous exposure.
    
    Optimized for ring layout: 8 actuators in two rings (4+4).
    Lower 4 bits → Lower ring (actuators 0-3)
    Upper 4 bits → Upper ring (actuators 4-7)
    """
    
    def __init__(self, mode: str = 'ring_based', layout: str = 'ring'):
        """
        Initialize single-byte encoder.
        
        Args:
            mode: Encoding mode
                - 'ring_based': Ring layout (4+4 split, recommended for ring layout)
                - 'pure': All 8 actuators simultaneously (fastest, hardest to distinguish)
                - 'micro_temporal': 2 phases, max 4 actuators (recommended for linear)
                - 'intensity': Intensity variation for bit position
                - 'grouped': Spatial grouping into pairs
            layout: Actuator layout
                - 'ring': Ring layout (two rings of 4)
                - 'linear': Linear array (8 in line)
        """
        self.mode = mode
        self.layout = layout
        self.frequency_map = self._build_frequency_map()
    
    def encode_character(self, char: str) -> Optional[Pattern]:
        """
        Encode character as single-byte pattern.
        
        Args:
            char: Character to encode
            
        Returns:
            Pattern object or None if character not supported
        """
        if len(char) != 1:
            return None
        
        byte_value = ord(char)
        
        if self.mode == 'ring_based':
            return self._encode_ring_based(byte_value)
        elif self.mode == 'pure':
            return self._encode_pure(byte_value)
        elif self.mode == 'micro_temporal':
            return self._encode_micro_temporal(byte_value)
        elif self.mode == 'intensity':
            return self._encode_intensity(byte_value)
        elif self.mode == 'grouped':
            return self._encode_grouped(byte_value)
        else:
            return self._encode_ring_based(byte_value)  # Default for ring layout
    
    def encode_text(self, text: str) -> List[Pattern]:
        """
        Encode text string into single-byte patterns.
        
        Args:
            text: Text string to encode
            
        Returns:
            List of Pattern objects
        """
        patterns = []
        for char in text:
            pattern = self.encode_character(char)
            if pattern:
                patterns.append(pattern)
        return patterns
    
    def _encode_ring_based(self, byte_value: int) -> Pattern:
        """
        Ring-based encoding: Lower 4 bits → Lower ring, Upper 4 bits → Upper ring.
        
        Optimized for ring layout (two rings of 4 actuators each).
        Max 4 actuators simultaneous (one ring), better discrimination.
        """
        events = []
        
        # Lower 4 bits (0-3) → Lower ring (actuators 0-3)
        lower_bits = byte_value & 0b1111
        for i in range(4):
            if (lower_bits >> i) & 1:
                events.append(ActuatorEvent(
                    actuator_id=i,
                    time_offset_ms=0,
                    duration_ms=80,
                    intensity=200
                ))
        
        # Upper 4 bits (4-7) → Upper ring (actuators 4-7)
        upper_bits = (byte_value >> 4) & 0b1111
        for i in range(4):
            if (upper_bits >> i) & 1:
                events.append(ActuatorEvent(
                    actuator_id=i + 4,
                    time_offset_ms=0,
                    duration_ms=80,
                    intensity=200
                ))
        
        return Pattern(events)
    
    def _encode_pure(self, byte_value: int) -> Pattern:
        """
        Pure single-byte: All 8 actuators simultaneously.
        
        Fastest (80ms) but hardest to distinguish.
        """
        events = []
        for i in range(8):
            if (byte_value >> i) & 1:  # Check bit i
                events.append(ActuatorEvent(
                    actuator_id=i,
                    time_offset_ms=0,  # All simultaneous!
                    duration_ms=80,
                    intensity=200
                ))
        return Pattern(events)
    
    def _encode_micro_temporal(self, byte_value: int) -> Pattern:
        """
        Micro-temporal: 2 phases, max 4 actuators simultaneous.
        
        Phase 1 (0ms): Lower 4 bits (actuators 0-3)
        Phase 2 (20ms): Upper 4 bits (actuators 4-7)
        
        Duration: 80ms total (60ms pulse + 20ms gap)
        Max simultaneous: 4 actuators (within perception limits)
        """
        events = []
        
        # Phase 1: Lower 4 bits (0-3) at t=0ms
        for i in range(4):
            if (byte_value >> i) & 1:
                events.append(ActuatorEvent(
                    actuator_id=i,
                    time_offset_ms=0,
                    duration_ms=60,
                    intensity=200
                ))
        
        # Phase 2: Upper 4 bits (4-7) at t=20ms
        for i in range(4, 8):
            if (byte_value >> i) & 1:
                events.append(ActuatorEvent(
                    actuator_id=i,
                    time_offset_ms=20,
                    duration_ms=60,
                    intensity=200
                ))
        
        return Pattern(events)
    
    def _encode_intensity(self, byte_value: int) -> Pattern:
        """
        Intensity variation: Higher intensity for higher bits.
        
        Helps distinguish bit positions through intensity differences.
        """
        events = []
        for i in range(8):
            if (byte_value >> i) & 1:
                # Intensity increases with bit position (150-220 range)
                intensity = 150 + (i * 10)
                events.append(ActuatorEvent(
                    actuator_id=i,
                    time_offset_ms=0,
                    duration_ms=80,
                    intensity=intensity
                ))
        return Pattern(events)
    
    def _encode_grouped(self, byte_value: int) -> Pattern:
        """
        Spatial grouping: Group actuators into pairs.
        
        Reduces cognitive load by grouping into 4 pairs:
        (0,1), (2,3), (4,5), (6,7)
        """
        events = []
        
        # Group into 4 pairs: (0,1), (2,3), (4,5), (6,7)
        for group in range(4):
            bits = (byte_value >> (group * 2)) & 0b11
            
            if bits & 0b01:  # Lower bit of pair
                events.append(ActuatorEvent(
                    actuator_id=group * 2,
                    time_offset_ms=0,
                    duration_ms=80,
                    intensity=180  # Lower intensity
                ))
            
            if bits & 0b10:  # Upper bit of pair
                events.append(ActuatorEvent(
                    actuator_id=group * 2 + 1,
                    time_offset_ms=0,
                    duration_ms=80,
                    intensity=220  # Higher intensity
                ))
        
        return Pattern(events)
    
    def _build_frequency_map(self) -> dict:
        """
        Build frequency-optimized bit pattern mapping.
        
        Common characters get simpler bit patterns (fewer bits set).
        This makes them easier to perceive and learn passively.
        """
        # For now, use direct ASCII mapping
        # Future: Optimize bit patterns for common characters
        return {}

