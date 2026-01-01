# Phoneme-Based Encoding Implementation

## Overview

This document describes the phoneme-based encoding implementation for Teletypathy, providing an alternative to letter-based encoding based on TAPS (TActile Phonemic Sleeve) research.

## Implementation Status

✅ **Implemented**: Core phoneme encoder with pattern mappings  
✅ **Implemented**: Unified encoder supporting both modes  
⚠️ **Basic G2P**: Simplified grapheme-to-phoneme conversion (needs improvement)  
⏳ **Pending**: Full G2P library integration (espeak-ng/phonemizer)

## Architecture

### Components

1. **PhonemeEncoder** (`src/core/encoding/phoneme.py`)
   - Converts text to phonemes
   - Maps phonemes to tactile patterns
   - 44 English phonemes supported

2. **UnifiedEncoder** (`src/core/encoding/unified.py`)
   - Supports both letter and phoneme modes
   - Mode switching at runtime
   - Unified interface for both encoders

3. **Pattern Library**
   - 44 phoneme patterns defined
   - Frequency-optimized (common phonemes = shorter patterns)
   - Spatial + temporal encoding

## Usage

### Basic Usage

```python
from src.core.encoding import UnifiedEncoder, EncodingMode

# Create encoder in phoneme mode
encoder = UnifiedEncoder(mode=EncodingMode.PHONEME)

# Encode text
patterns = encoder.encode_text("hello")
# Returns list of Pattern objects for phonemes: /h/, /ɛ/, /l/, /oʊ/
```

### Mode Switching

```python
encoder = UnifiedEncoder()

# Start in letter mode (default)
patterns = encoder.encode_text("hello")  # 5 patterns (h-e-l-l-o)

# Switch to phoneme mode
encoder.set_mode(EncodingMode.PHONEME)
patterns = encoder.encode_text("hello")  # 4 patterns (/h/-/ɛ/-/l/-/oʊ/)
```

### Comparison Example

See `examples/phoneme_encoding.py` for complete examples.

## Phoneme Patterns

### Pattern Categories

#### High-Frequency Consonants (120ms, single actuator)
- `/n/`, `/t/`, `/s/`, `/r/`, `/l/` - Most common consonants

#### High-Frequency Vowels (150ms, single actuator)
- `/ə/` (schwa), `/ɪ/`, `/ɛ/` - Most common vowels

#### Medium-Frequency Consonants (200ms, two actuators sequential)
- `/d/`, `/k/`, `/m/`, `/p/`, `/b/`, `/g/`

#### Fricatives (200ms continuous)
- `/f/`, `/v/`, `/z/`, `/θ/`, `/ð/`

#### Complex Consonants (multi-actuator)
- `/ʃ/`, `/ʒ/`, `/tʃ/`, `/dʒ/`, `/ŋ/`

#### Vowels (300ms, three actuators)
- `/æ/`, `/ʌ/`, `/ɑ/`, `/ɔ/`, `/ʊ/`, `/u/`, `/i/`, `/o/`

#### Diphthongs (two-phase patterns)
- `/aɪ/`, `/aʊ/`, `/eɪ/`, `/oʊ/`, `/ɔɪ/`

#### Liquids and Glides
- `/w/`, `/j/`, `/h/`

## Grapheme-to-Phoneme (G2P) Conversion

### Current Implementation

Basic rule-based G2P conversion is implemented in `PhonemeEncoder._build_g2p_map()`.

**Limitations:**
- Simplified rules (doesn't handle all English spelling variations)
- No context awareness (same letter may map differently)
- No stress/syllable information

**Supported:**
- Common single letters
- Common digraphs (th, sh, ch, ng, etc.)
- Common vowel combinations (ai, oi, ou, etc.)

### Production Recommendation

For production use, integrate a proper G2P library:

**Options:**
1. **espeak-ng**: Command-line tool, can be called from Python
2. **phonemizer**: Python library, uses espeak-ng backend
3. **CMU Pronouncing Dictionary**: Dictionary-based, high accuracy

**Example with phonemizer:**
```python
from phonemizer import phonemize

def text_to_phonemes(text: str) -> List[str]:
    """Convert text to phonemes using phonemizer."""
    phonemes = phonemize(text, language='en-us', backend='espeak', strip=True)
    return phonemes.split()
```

## Pattern Frequency Optimization

### Strategy

Patterns are optimized based on phoneme frequency in English speech:

| Frequency | Pattern Duration | Examples |
|-----------|-----------------|----------|
| Very High (>7%) | 120-150ms | /n/, /t/, /s/, /ə/ |
| High (4-7%) | 200-250ms | /d/, /k/, /m/, /ɪ/ |
| Medium (2-4%) | 250-300ms | /p/, /b/, /ɛ/ |
| Low (<2%) | 300-400ms | /θ/, /ð/, /ʒ/ |

### Benefits

- **Faster communication**: Common phonemes use shorter patterns
- **Natural rhythm**: Patterns match speech timing
- **Efficient encoding**: Optimized for real-world usage

## Comparison: Letter vs. Phoneme

### Word "hello"

**Letter Mode:**
- Patterns: 5 (h-e-l-l-o)
- Total duration: ~750ms (5 × 150ms)
- Recognition: Spell out letters, then recognize word

**Phoneme Mode:**
- Patterns: 4 (/h/-/ɛ/-/l/-/oʊ/)
- Total duration: ~600ms (varies by phoneme)
- Recognition: Direct word recognition from phonemes

### Advantages of Phoneme Mode

1. **Faster word recognition**: Direct phoneme-to-word mapping
2. **Fewer patterns**: Often fewer phonemes than letters
3. **Natural speech flow**: Patterns match speech rhythm
4. **Research-backed**: TAPS research shows 500 words learned

### Advantages of Letter Mode

1. **Simpler learning**: Direct letter-to-pattern mapping
2. **Spelling practice**: Helps with spelling skills
3. **No G2P needed**: No conversion required
4. **Universal**: Works for any text

## Research Alignment

### TAPS Research (2020)

✅ **Phoneme-level encoding**: Implemented  
✅ **Frequency optimization**: Implemented  
✅ **Distinctive patterns**: Implemented  
✅ **Word recognition**: Supported (through phoneme sequences)  
⏳ **500-word vocabulary**: Requires training/validation

### Key Differences from TAPS

- **Actuator count**: TAPS uses 4×6 array (24 actuators), Teletypathy uses 8 actuators
- **Pattern design**: Adapted for 8-actuator linear array
- **G2P**: Basic implementation (TAPS may use different approach)

## Future Enhancements

### Short-Term

1. **G2P Library Integration**: Integrate phonemizer or espeak-ng
2. **Pattern Validation**: User testing for pattern discrimination
3. **Learning Mode**: Guided learning with phoneme practice
4. **Word-Level Patterns**: Common words as single patterns

### Long-Term

1. **Context-Aware Encoding**: Optimize phoneme sequences
2. **Stress Marking**: Emphasize stressed syllables
3. **Multimodal**: Add intensity variation for emphasis
4. **Adaptive Patterns**: Adjust based on user performance

## Testing

### Unit Tests

Create tests in `tests/unit/test_phoneme_encoding.py`:

```python
def test_phoneme_encoder():
    encoder = PhonemeEncoder()
    patterns = encoder.encode_text("hello")
    assert len(patterns) == 4  # /h/, /ɛ/, /l/, /oʊ/

def test_unified_encoder_mode_switching():
    encoder = UnifiedEncoder(mode=EncodingMode.LETTER)
    assert encoder.get_mode() == EncodingMode.LETTER
    
    encoder.set_mode(EncodingMode.PHONEME)
    assert encoder.get_mode() == EncodingMode.PHONEME
```

### Integration Tests

Test with real words and compare letter vs. phoneme encoding.

## Performance

### Latency

- **Pattern generation**: <1ms (lookup table, same as letter mode)
- **G2P conversion**: ~1-5ms (basic rules), ~10-50ms (with library)
- **Total**: Comparable to letter mode for basic G2P

### Memory

- **Pattern storage**: ~44 patterns × 50 bytes = ~2.2 KB
- **G2P map**: ~100 entries × 10 bytes = ~1 KB
- **Total**: ~3.2 KB (acceptable)

## References

1. Tan, H.Z., Reed, C.M., et al. (2020). "Acquisition of 500 English Words through a TActile Phonemic Sleeve (TAPS)". IEEE Xplore.
2. Reed, C.M., Tan, H.Z., et al. (2019). "A Phonemic-Based Tactile Display for Speech Communication". ResearchGate.
3. [Phoneme Encoding Design](../research/phoneme_encoding_design.md): Design document

## Related Documents

- [Encoding System Design](encoding_system.md): Letter-based encoding
- [Comparative Analysis](../research/comparative_analysis.md): Research comparison
- [Improvement Roadmap](../research/improvement_roadmap.md): Implementation priorities

