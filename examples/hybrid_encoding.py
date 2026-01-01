"""
Example: Hybrid encoding combining character and phoneme modes.

Demonstrates adaptive mode switching and word-level hybrid strategies.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.encoding import HybridEncoder, UnifiedEncoder, EncodingMode


def main():
    """Demonstrate hybrid encoding."""
    
    # Test text with words and non-words
    test_texts = [
        "hello world",
        "Visit https://example.com",
        "The quick brown fox jumps over the lazy dog",
        "Code: x = 42; print('hello')",
        "Hello world! Visit https://example.com for more info.",
    ]
    
    print("=" * 80)
    print("Hybrid Encoding Examples")
    print("=" * 80)
    print()
    
    # Create encoders
    hybrid_adaptive = HybridEncoder(strategy='adaptive')
    hybrid_word_level = HybridEncoder(strategy='word_level')
    pure_character = UnifiedEncoder(mode=EncodingMode.LETTER)
    pure_phoneme = UnifiedEncoder(mode=EncodingMode.PHONEME)
    
    for text in test_texts:
        print(f"Text: {text}")
        print("-" * 80)
        
        # Compare strategies
        strategies = {
            'Pure Character': pure_character.encode_text(text),
            'Pure Phoneme': pure_phoneme.encode_text(text),
            'Hybrid Adaptive': hybrid_adaptive.encode_text(text),
            'Hybrid Word-Level': hybrid_word_level.encode_text(text),
        }
        
        for strategy_name, patterns in strategies.items():
            duration = sum(p.get_duration() for p in patterns)
            print(f"  {strategy_name:20} {len(patterns):3} patterns, {duration:5}ms")
        
        print()
    
    print("=" * 80)
    print("Strategy Comparison")
    print("=" * 80)
    print()
    print("Pure Character:")
    print("  ✅ 100% accuracy, universal compatibility")
    print("  ❌ More patterns, slower")
    print()
    print("Pure Phoneme:")
    print("  ✅ Fewer patterns, faster word recognition")
    print("  ❌ May fail on code/URLs, ~95-98% accuracy")
    print()
    print("Hybrid Adaptive:")
    print("  ✅ Automatic optimization, handles edge cases")
    print("  ✅ Best balance of efficiency and accuracy")
    print("  ⚠️  Mode switching may be noticeable")
    print()
    print("Hybrid Word-Level:")
    print("  ✅ Phoneme for common words, character for rare")
    print("  ✅ Predictable behavior")
    print("  ⚠️  Requires word frequency dictionary")


if __name__ == "__main__":
    main()

