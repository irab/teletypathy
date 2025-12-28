"""Unit tests for pattern encoding."""

import unittest
from src.core.encoding.pattern import PatternEncoder, Pattern, ActuatorEvent


class TestPatternEncoder(unittest.TestCase):
    """Test pattern encoder."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.encoder = PatternEncoder()
    
    def test_encode_character_e(self):
        """Test encoding letter E."""
        pattern = self.encoder.encode_character('E')
        self.assertIsNotNone(pattern)
        self.assertEqual(len(pattern.events), 1)
        self.assertEqual(pattern.events[0].actuator_id, 0)
        self.assertEqual(pattern.events[0].duration_ms, 150)
    
    def test_encode_character_n(self):
        """Test encoding letter N (two-actuator pattern)."""
        pattern = self.encoder.encode_character('N')
        self.assertIsNotNone(pattern)
        self.assertEqual(len(pattern.events), 2)
        self.assertEqual(pattern.events[0].actuator_id, 0)
        self.assertEqual(pattern.events[1].actuator_id, 1)
    
    def test_encode_character_case_insensitive(self):
        """Test that encoding is case-insensitive."""
        pattern_lower = self.encoder.encode_character('e')
        pattern_upper = self.encoder.encode_character('E')
        self.assertIsNotNone(pattern_lower)
        self.assertIsNotNone(pattern_upper)
        # Patterns should be similar (same actuators)
        self.assertEqual(pattern_lower.events[0].actuator_id, pattern_upper.events[0].actuator_id)
    
    def test_encode_character_unsupported(self):
        """Test encoding unsupported character."""
        pattern = self.encoder.encode_character('@')
        self.assertIsNone(pattern)
    
    def test_encode_text(self):
        """Test encoding text string."""
        patterns = self.encoder.encode_text("HELLO")
        self.assertEqual(len(patterns), 5)
        self.assertIsInstance(patterns[0], Pattern)
    
    def test_pattern_duration(self):
        """Test pattern duration calculation."""
        pattern = self.encoder.encode_character('E')
        duration = pattern.get_duration()
        self.assertGreater(duration, 0)
        self.assertLessEqual(duration, 500)  # Reasonable upper bound


if __name__ == '__main__':
    unittest.main()


