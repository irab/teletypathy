# Transmission Time Analysis: Guardian Article

## Article Statistics
- **Total characters (printable)**: 7,014
  - Letters: 5,529
  - Spaces: 1,191
  - Punctuation: 227
  - Numbers: 60
- **Total words**: 1,157
- **Average word length**: 6.1 characters

## Encoding Mode Comparison

### 1. Single-Byte Encoding (FASTEST)
- **Patterns**: 7,014 (one per character)
- **Pattern duration**: 80ms per character
- **Total transmission time**: **9.4 minutes** (561 seconds)
- **Speed**: 12.5 characters/second
- **Includes**: ✅ **ALL characters** (letters, spaces, punctuation, numbers)
- **Notes**: 
  - Fastest pattern execution (80ms per character)
  - **Every character gets a pattern** - spaces and punctuation included
  - Optimized for passive learning
  - All 8 actuators can activate simultaneously (ring-based: max 4 per ring)
  - Best for well-trained users who can distinguish patterns quickly

### 2. Character Encoding (Traditional)
- **Patterns**: 6,926 (spaces excluded)
- **Average pattern duration**: 180ms per character
- **Total transmission time**: **21.0 minutes** (1,263 seconds)
- **Speed**: 5.6 characters/second
- **Includes**: ✅ Letters, punctuation, numbers
- **Excludes**: ❌ Spaces (become 0ms pauses), some unsupported characters
- **Notes**:
  - More reliable pattern recognition initially
  - Patterns vary from 150ms (common letters) to 640ms (rare letters)
  - Spaces create pauses but no vibration pattern
  - Better for learning phase

### 3. Phoneme Encoding
- **Patterns**: 6,273 phonemes (10.6% fewer than characters)
- **Average pattern duration**: 168ms per phoneme
- **Total transmission time**: **17.6 minutes** (1,055 seconds)
- **Speed**: 6.6 characters/second
- **Includes**: ✅ Phonemes from letters
- **Excludes**: ❌ Spaces (become pauses), most punctuation
- **Notes**:
  - Fewer patterns than character mode (phoneme compression)
  - Faster word recognition for trained users
  - Requires G2P conversion (adds ~1-50ms latency per word)
  - Spaces and punctuation often skipped

## Fastest Transmission: Single-Byte Encoding

**For a well-trained user**, the fastest transmission method is **single-byte encoding**:

- **Total time**: **9.4 minutes** (561 seconds)
- **Speed**: **12.5 characters/second**
- **Pattern duration**: 80ms per character

### Why Single-Byte is Fastest

1. **Shortest pattern duration**: 80ms vs. 150-640ms for character mode
2. **No conversion overhead**: Direct ASCII mapping (no G2P conversion)
3. **Optimized for speed**: Designed specifically for low-latency passive learning
4. **Ring-based layout**: Max 4 actuators simultaneous per ring (better discrimination)

### Considerations for Well-Trained Users

- **Pattern recognition**: Well-trained users can recognize patterns as fast as they execute
- **No waiting**: Patterns can be queued back-to-back (80ms each)
- **System limit**: Transmission speed is limited by pattern execution time, not recognition speed
- **Physical constraint**: LRA motors need ~10-20ms to activate, but pattern duration (80ms) dominates

## Comparison Summary

| Mode | Duration | Speed | Patterns | Best For |
|------|----------|-------|----------|----------|
| **Single-byte** | **9.4 min** | **12.5 cps** | 7,014 | **Well-trained users** |
| Phoneme | 17.6 min | 6.6 cps | 6,273 | Word recognition |
| Character | 21.0 min | 5.6 cps | 6,926 | Learning phase |

## Conclusion

**The fastest transmission for a well-trained user is single-byte encoding at 9.4 minutes** (561 seconds) for the entire 7,014-character article.

**Important**: This calculation **INCLUDES spaces and punctuation**. Single-byte encoding treats every character equally:
- Each letter: 80ms pattern
- Each space: 80ms pattern  
- Each punctuation mark: 80ms pattern
- Each number: 80ms pattern

This assumes:
- User can distinguish 8-bit patterns reliably (well-trained)
- Patterns execute back-to-back (no additional spacing needed)
- System operates at optimal speed (80ms per pattern)

For comparison, reading the article aloud typically takes 5-7 minutes, so single-byte encoding is competitive with natural speech pace for trained users.

### If spaces were excluded:
- Letters + punctuation + numbers only: ~5,816 characters
- Single-byte time: ~7.8 minutes (465 seconds)
- But this would lose word boundaries and readability

