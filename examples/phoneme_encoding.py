"""
Example: Phoneme-based encoding for Teletypathy.

Demonstrates phoneme-based encoding system based on TAPS research.
"""

from src.core.encoding import UnifiedEncoder, EncodingMode, Pattern


def main():
    """Demonstrate phoneme-based encoding."""
    
    # Create encoder in phoneme mode
    encoder = UnifiedEncoder(mode=EncodingMode.PHONEME)
    
    # Example words
    words = [
        "hello",
        "world",
        "teletypathy",
        "phoneme",
    ]
    
    print("Phoneme-Based Encoding Examples")
    print("=" * 50)
    
    for word in words:
        print(f"\nWord: {word}")
        print(f"Mode: {encoder.get_mode_name()}")
        
        # Encode word
        patterns = encoder.encode_text(word)
        
        print(f"Patterns: {len(patterns)}")
        for i, pattern in enumerate(patterns):
            print(f"  Pattern {i+1}: {len(pattern.events)} events, "
                  f"duration={pattern.get_duration()}ms")
            for event in pattern.events:
                print(f"    - Actuator {event.actuator_id} at {event.time_offset_ms}ms "
                      f"for {event.duration_ms}ms")
    
    # Compare with letter mode
    print("\n" + "=" * 50)
    print("Comparison: Letter vs Phoneme Mode")
    print("=" * 50)
    
    test_word = "hello"
    
    # Letter mode
    encoder.set_mode(EncodingMode.LETTER)
    letter_patterns = encoder.encode_text(test_word)
    
    # Phoneme mode
    encoder.set_mode(EncodingMode.PHONEME)
    phoneme_patterns = encoder.encode_text(test_word)
    
    print(f"\nWord: {test_word}")
    print(f"Letter mode: {len(letter_patterns)} patterns")
    print(f"Phoneme mode: {len(phoneme_patterns)} patterns")
    
    # Calculate total duration
    letter_duration = sum(p.get_duration() for p in letter_patterns)
    phoneme_duration = sum(p.get_duration() for p in phoneme_patterns)
    
    print(f"\nTotal duration:")
    print(f"  Letter mode: {letter_duration}ms")
    print(f"  Phoneme mode: {phoneme_duration}ms")
    print(f"  Difference: {letter_duration - phoneme_duration}ms "
          f"({((letter_duration - phoneme_duration) / letter_duration * 100):.1f}% faster)")


if __name__ == "__main__":
    main()

