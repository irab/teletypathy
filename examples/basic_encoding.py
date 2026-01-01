#!/usr/bin/env python3
"""
Basic encoding example for Teletypathy.

Demonstrates how to encode characters and text into tactile patterns.
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.core.encoding import PatternEncoder


def main():
    """Main example function."""
    print("Teletypathy Basic Encoding Example")
    print("=" * 40)
    
    # Create encoder
    encoder = PatternEncoder()
    
    # Example 1: Encode single character
    print("\n1. Encoding single character 'E':")
    pattern = encoder.encode_character('E')
    if pattern:
        print(f"   Pattern duration: {pattern.get_duration()}ms")
        print(f"   Number of events: {len(pattern.events)}")
        for event in pattern.events:
            print(f"     - Actuator {event.actuator_id}: "
                  f"{event.time_offset_ms}ms + {event.duration_ms}ms "
                  f"(intensity: {event.intensity})")
    
    # Example 2: Encode text string
    print("\n2. Encoding text 'HELLO':")
    text = "HELLO"
    patterns = encoder.encode_text(text)
    print(f"   Encoded {len(patterns)} patterns")
    for i, pattern in enumerate(patterns):
        char = text[i]
        print(f"   '{char}': {pattern.get_duration()}ms, "
              f"{len(pattern.events)} events")
    
    # Example 3: Compare different characters
    print("\n3. Comparing pattern durations:")
    test_chars = ['E', 'N', 'C', 'Z']
    for char in test_chars:
        pattern = encoder.encode_character(char)
        if pattern:
            print(f"   '{char}': {pattern.get_duration()}ms")
    
    # Example 4: Case insensitivity
    print("\n4. Case insensitivity:")
    upper_pattern = encoder.encode_character('E')
    lower_pattern = encoder.encode_character('e')
    if upper_pattern and lower_pattern:
        print(f"   'E': {upper_pattern.get_duration()}ms")
        print(f"   'e': {lower_pattern.get_duration()}ms")
        print(f"   Same pattern: {upper_pattern.events[0].actuator_id == lower_pattern.events[0].actuator_id}")
    
    print("\n" + "=" * 40)
    print("Example complete!")


if __name__ == '__main__':
    main()



