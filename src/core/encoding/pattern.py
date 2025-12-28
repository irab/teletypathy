"""
Pattern encoding library for Teletypathy.

Converts characters to tactile patterns and manages pattern definitions.
"""

from typing import List, Tuple, Optional
from dataclasses import dataclass
from enum import IntEnum


class ActuatorEvent:
    """Represents a single actuator activation event."""
    
    def __init__(self, actuator_id: int, time_offset_ms: int, duration_ms: int, intensity: int = 200):
        """
        Initialize actuator event.
        
        Args:
            actuator_id: Actuator ID (0-7)
            time_offset_ms: Time offset from pattern start (ms)
            duration_ms: Duration of activation (ms)
            intensity: Vibration intensity (0-255)
        """
        self.actuator_id = actuator_id
        self.time_offset_ms = time_offset_ms
        self.duration_ms = duration_ms
        self.intensity = intensity
    
    def __repr__(self):
        return f"ActuatorEvent(actuator={self.actuator_id}, time={self.time_offset_ms}ms, duration={self.duration_ms}ms, intensity={self.intensity})"


@dataclass
class Pattern:
    """Represents a tactile pattern."""
    
    events: List[ActuatorEvent]
    total_duration_ms: int
    
    def __init__(self, events: List[ActuatorEvent]):
        """Initialize pattern with events."""
        self.events = sorted(events, key=lambda e: e.time_offset_ms)
        self.total_duration_ms = max(
            (e.time_offset_ms + e.duration_ms for e in self.events),
            default=0
        )
    
    def get_duration(self) -> int:
        """Get total pattern duration in milliseconds."""
        return self.total_duration_ms


class PatternEncoder:
    """Encodes characters into tactile patterns."""
    
    def __init__(self):
        """Initialize pattern encoder with character mappings."""
        self.pattern_map = self._build_pattern_map()
    
    def encode_character(self, char: str) -> Optional[Pattern]:
        """
        Encode a single character into a tactile pattern.
        
        Args:
            char: Character to encode
            
        Returns:
            Pattern object or None if character not supported
        """
        if len(char) != 1:
            return None
        
        pattern_def = self.pattern_map.get(char)
        if pattern_def is None:
            return None
        
        return self._create_pattern(pattern_def)
    
    def encode_text(self, text: str) -> List[Pattern]:
        """
        Encode a text string into a list of patterns.
        
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
            # Space is handled as pause (no pattern, but spacing)
        return patterns
    
    def _create_pattern(self, pattern_def: dict) -> Pattern:
        """Create Pattern object from pattern definition."""
        events = []
        for event_def in pattern_def.get('events', []):
            event = ActuatorEvent(
                actuator_id=event_def['actuator'],
                time_offset_ms=event_def['time_offset'],
                duration_ms=event_def['duration'],
                intensity=event_def.get('intensity', 200)
            )
            events.append(event)
        return Pattern(events)
    
    def _build_pattern_map(self) -> dict:
        """Build character to pattern mapping dictionary."""
        # High-frequency letters: single actuator, short pulse
        patterns = {
            'E': {'events': [{'actuator': 0, 'time_offset': 0, 'duration': 150}]},
            'T': {'events': [{'actuator': 1, 'time_offset': 0, 'duration': 150}]},
            'A': {'events': [{'actuator': 2, 'time_offset': 0, 'duration': 150}]},
            'O': {'events': [{'actuator': 3, 'time_offset': 0, 'duration': 150}]},
            'I': {'events': [{'actuator': 4, 'time_offset': 0, 'duration': 150}]},
            
            # Medium-frequency letters: two-actuator sequential
            'N': {'events': [
                {'actuator': 0, 'time_offset': 0, 'duration': 100},
                {'actuator': 1, 'time_offset': 150, 'duration': 100}
            ]},
            'S': {'events': [
                {'actuator': 1, 'time_offset': 0, 'duration': 100},
                {'actuator': 2, 'time_offset': 150, 'duration': 100}
            ]},
            'H': {'events': [
                {'actuator': 2, 'time_offset': 0, 'duration': 100},
                {'actuator': 3, 'time_offset': 150, 'duration': 100}
            ]},
            'R': {'events': [
                {'actuator': 3, 'time_offset': 0, 'duration': 100},
                {'actuator': 4, 'time_offset': 150, 'duration': 100}
            ]},
            'D': {'events': [
                {'actuator': 4, 'time_offset': 0, 'duration': 100},
                {'actuator': 5, 'time_offset': 150, 'duration': 100}
            ]},
            'L': {'events': [
                {'actuator': 5, 'time_offset': 0, 'duration': 100},
                {'actuator': 6, 'time_offset': 150, 'duration': 100}
            ]},
            
            # Medium-frequency letters: three-actuator patterns
            'C': {'events': [
                {'actuator': 0, 'time_offset': 0, 'duration': 80},
                {'actuator': 1, 'time_offset': 120, 'duration': 80},
                {'actuator': 2, 'time_offset': 240, 'duration': 80}
            ]},
            'U': {'events': [
                {'actuator': 1, 'time_offset': 0, 'duration': 80},
                {'actuator': 2, 'time_offset': 120, 'duration': 80},
                {'actuator': 3, 'time_offset': 240, 'duration': 80}
            ]},
            'M': {'events': [
                {'actuator': 2, 'time_offset': 0, 'duration': 80},
                {'actuator': 3, 'time_offset': 120, 'duration': 80},
                {'actuator': 4, 'time_offset': 240, 'duration': 80}
            ]},
            'W': {'events': [
                {'actuator': 3, 'time_offset': 0, 'duration': 80},
                {'actuator': 4, 'time_offset': 120, 'duration': 80},
                {'actuator': 5, 'time_offset': 240, 'duration': 80}
            ]},
            'F': {'events': [
                {'actuator': 4, 'time_offset': 0, 'duration': 80},
                {'actuator': 5, 'time_offset': 120, 'duration': 80},
                {'actuator': 6, 'time_offset': 240, 'duration': 80}
            ]},
            'G': {'events': [
                {'actuator': 5, 'time_offset': 0, 'duration': 80},
                {'actuator': 6, 'time_offset': 120, 'duration': 80},
                {'actuator': 7, 'time_offset': 240, 'duration': 80}
            ]},
            'Y': {'events': [
                {'actuator': 0, 'time_offset': 0, 'duration': 80},
                {'actuator': 2, 'time_offset': 120, 'duration': 80},
                {'actuator': 4, 'time_offset': 240, 'duration': 80}
            ]},
            'P': {'events': [
                {'actuator': 1, 'time_offset': 0, 'duration': 80},
                {'actuator': 3, 'time_offset': 120, 'duration': 80},
                {'actuator': 5, 'time_offset': 240, 'duration': 80}
            ]},
            'B': {'events': [
                {'actuator': 2, 'time_offset': 0, 'duration': 80},
                {'actuator': 4, 'time_offset': 120, 'duration': 80},
                {'actuator': 6, 'time_offset': 240, 'duration': 80}
            ]},
            'V': {'events': [
                {'actuator': 3, 'time_offset': 0, 'duration': 80},
                {'actuator': 5, 'time_offset': 120, 'duration': 80},
                {'actuator': 7, 'time_offset': 240, 'duration': 80}
            ]},
            
            # Lower-frequency letters: complex patterns
            'K': {'events': [
                {'actuator': 0, 'time_offset': 0, 'duration': 70},
                {'actuator': 1, 'time_offset': 100, 'duration': 70},
                {'actuator': 2, 'time_offset': 200, 'duration': 70},
                {'actuator': 3, 'time_offset': 300, 'duration': 70}
            ]},
            'J': {'events': [
                {'actuator': 4, 'time_offset': 0, 'duration': 70},
                {'actuator': 3, 'time_offset': 100, 'duration': 70},
                {'actuator': 2, 'time_offset': 200, 'duration': 70},
                {'actuator': 1, 'time_offset': 300, 'duration': 70}
            ]},
            'X': {'events': [
                {'actuator': 0, 'time_offset': 0, 'duration': 100},
                {'actuator': 7, 'time_offset': 0, 'duration': 100},
                {'actuator': 1, 'time_offset': 120, 'duration': 100},
                {'actuator': 6, 'time_offset': 120, 'duration': 100},
                {'actuator': 2, 'time_offset': 240, 'duration': 100},
                {'actuator': 5, 'time_offset': 240, 'duration': 100},
                {'actuator': 3, 'time_offset': 360, 'duration': 100},
                {'actuator': 4, 'time_offset': 360, 'duration': 100}
            ]},
            'Q': {'events': [
                {'actuator': 0, 'time_offset': 0, 'duration': 60},
                {'actuator': 1, 'time_offset': 80, 'duration': 60},
                {'actuator': 2, 'time_offset': 160, 'duration': 60},
                {'actuator': 3, 'time_offset': 240, 'duration': 60},
                {'actuator': 4, 'time_offset': 320, 'duration': 60},
                {'actuator': 5, 'time_offset': 400, 'duration': 60},
                {'actuator': 6, 'time_offset': 480, 'duration': 60},
                {'actuator': 7, 'time_offset': 560, 'duration': 60}
            ]},
            'Z': {'events': [
                {'actuator': 7, 'time_offset': 0, 'duration': 60},
                {'actuator': 6, 'time_offset': 80, 'duration': 60},
                {'actuator': 5, 'time_offset': 160, 'duration': 60},
                {'actuator': 4, 'time_offset': 240, 'duration': 60},
                {'actuator': 3, 'time_offset': 320, 'duration': 60},
                {'actuator': 2, 'time_offset': 400, 'duration': 60},
                {'actuator': 1, 'time_offset': 480, 'duration': 60},
                {'actuator': 0, 'time_offset': 560, 'duration': 60}
            ]},
            
            # Numbers (marker on actuator 5)
            '0': {'events': [{'actuator': 5, 'time_offset': 0, 'duration': 200}]},
            '1': {'events': [
                {'actuator': 5, 'time_offset': 0, 'duration': 100},
                {'actuator': 0, 'time_offset': 150, 'duration': 150}
            ]},
            '2': {'events': [
                {'actuator': 5, 'time_offset': 0, 'duration': 100},
                {'actuator': 0, 'time_offset': 150, 'duration': 100},
                {'actuator': 1, 'time_offset': 300, 'duration': 100}
            ]},
            '3': {'events': [
                {'actuator': 5, 'time_offset': 0, 'duration': 100},
                {'actuator': 0, 'time_offset': 150, 'duration': 80},
                {'actuator': 1, 'time_offset': 270, 'duration': 80},
                {'actuator': 2, 'time_offset': 390, 'duration': 80}
            ]},
            
            # Punctuation
            '.': {'events': [
                {'actuator': i, 'time_offset': 0, 'duration': 200} for i in range(8)
            ]},
            ',': {'events': [
                {'actuator': 0, 'time_offset': 0, 'duration': 150},
                {'actuator': 7, 'time_offset': 0, 'duration': 150}
            ]},
            '?': {'events': [
                {'actuator': 0, 'time_offset': 0, 'duration': 100},
                {'actuator': 4, 'time_offset': 150, 'duration': 100},
                {'actuator': 0, 'time_offset': 300, 'duration': 100}
            ]},
            '!': {'events': [
                {'actuator': i, 'time_offset': 0, 'duration': 150} for i in range(8)
            ] + [
                {'actuator': i, 'time_offset': 200, 'duration': 150} for i in range(8)
            ]},
            ' ': {'events': []},  # Space: no pattern (pause handled separately)
        }
        
        # Add lowercase versions (same patterns)
        lowercase_patterns = {char.lower(): pattern for char, pattern in patterns.items() if char.isalpha()}
        patterns.update(lowercase_patterns)
        
        return patterns


