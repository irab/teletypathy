# 8-Bit Phoneme Encoding: Implementation Guide

## Quick Reference

### Performance Summary

| Method | Avg Duration | Avg Speed | Improvement | Best For |
|--------|-------------|-----------|-------------|----------|
| **8-Bit Phoneme** | **4.49 min** | **13.7 cps** | **+8.9%** | **General text** |
| Single-byte Character | 4.93 min | 12.5 cps | Baseline | Technical text |
| Character + Top 150 | 4.80 min | 13.1 cps | +2.6% | Word learning |
| Hybrid | 4.80 min | 12.8 cps | +2.6% | Mixed content |
| Temporal Phoneme | 9.83 min | 6.3 cps | -99% | Learning only |

### Pattern Space Allocation

```
256 Total Patterns (8-bit)
├── Patterns 0-127: Character/Word Mode (Actuator 7 = OFF)
│   ├── Basic characters: ~78 patterns
│   └── Top 150 words: 150 patterns (or subset)
│
└── Patterns 128-255: Phoneme Mode (Actuator 7 = ON)
    ├── English phonemes: 40 patterns
    └── Remaining: 88 patterns (for expansion)
```

## Implementation Code

### Basic 8-Bit Phoneme Encoder

```python
class Phoneme8BitEncoder:
    """8-bit phoneme encoder with mode indicator."""
    
    def __init__(self):
        self.phoneme_map = self._build_phoneme_map()
        self.g2p_converter = PhonemeConverter()  # G2P library
    
    def encode_phoneme(self, phoneme: str) -> int:
        """
        Encode phoneme as 8-bit pattern.
        
        Returns: Pattern value (128-255, Actuator 7 = ON)
        """
        if phoneme not in self.phoneme_map:
            raise ValueError(f"Unknown phoneme: {phoneme}")
        
        phoneme_id = self.phoneme_map[phoneme]
        # Actuator 7 = ON (bit 7 = 1) for phoneme mode
        pattern = 128 + phoneme_id  # Patterns 128-255
        return pattern
    
    def encode_text(self, text: str) -> List[int]:
        """Encode text as 8-bit phoneme patterns."""
        phonemes = self.g2p_converter.text_to_phonemes(text)
        patterns = []
        for phoneme in phonemes:
            if phoneme != ' ':  # Skip spaces
                pattern = self.encode_phoneme(phoneme)
                patterns.append(pattern)
        return patterns
    
    def _build_phoneme_map(self) -> Dict[str, int]:
        """Map phonemes to IDs (0-127 for 7-bit data)."""
        phonemes = [
            # High-frequency consonants
            'n', 't', 's', 'r', 'l',
            # Medium-frequency consonants
            'd', 'k', 'm', 'p', 'b', 'g',
            # Fricatives
            'f', 'v', 'z', 'θ', 'ð',
            # Complex consonants
            'ʃ', 'ʒ', 'tʃ', 'dʒ', 'ŋ', 'h', 'w', 'j',
            # Vowels
            'ə', 'ɪ', 'ɛ', 'æ', 'ʌ', 'ɑ', 'ɔ', 'ʊ', 'u', 'i', 'o',
            # Diphthongs
            'aɪ', 'aʊ', 'eɪ', 'oʊ', 'ɔɪ',
        ]
        return {ph: i for i, ph in enumerate(phonemes)}
```

### Mode Indicator Pattern Generator

```python
def generate_pattern(byte_value: int, mode: str = 'character') -> Pattern:
    """
    Generate 8-bit pattern with mode indicator.
    
    Args:
        byte_value: Data value (0-127)
        mode: 'character' or 'phoneme'
    
    Returns:
        Pattern object with actuator events
    """
    events = []
    
    # Set mode indicator (Actuator 7)
    if mode == 'phoneme':
        mode_bit = 1  # Actuator 7 ON
        pattern_value = 128 + byte_value  # Patterns 128-255
    else:
        mode_bit = 0  # Actuator 7 OFF
        pattern_value = byte_value  # Patterns 0-127
    
    # Activate mode indicator
    if mode_bit == 1:
        events.append(ActuatorEvent(
            actuator_id=7,
            time_offset_ms=0,
            duration_ms=80,
            intensity=200
        ))
    
    # Activate data actuators (0-6) based on byte_value
    for i in range(7):
        if (byte_value >> i) & 1:  # Check bit i
            events.append(ActuatorEvent(
                actuator_id=i,
                time_offset_ms=0,
                duration_ms=80,
                intensity=200
            ))
    
    return Pattern(events)
```

### Unified Encoder with Mode Switching

```python
class Unified8BitEncoder:
    """Unified encoder supporting both character and phoneme modes."""
    
    def __init__(self, default_mode: str = 'phoneme'):
        self.phoneme_encoder = Phoneme8BitEncoder()
        self.character_encoder = SingleByteEncoder()
        self.default_mode = default_mode
    
    def encode_text(self, text: str, mode: str = None) -> List[Pattern]:
        """
        Encode text using specified mode.
        
        Args:
            text: Text to encode
            mode: 'phoneme', 'character', or 'hybrid'
        """
        if mode is None:
            mode = self.default_mode
        
        if mode == 'phoneme':
            return self._encode_phoneme(text)
        elif mode == 'character':
            return self._encode_character(text)
        elif mode == 'hybrid':
            return self._encode_hybrid(text)
        else:
            raise ValueError(f"Unknown mode: {mode}")
    
    def _encode_phoneme(self, text: str) -> List[Pattern]:
        """Encode as pure phonemes."""
        phonemes = self.phoneme_encoder.g2p_converter.text_to_phonemes(text)
        patterns = []
        for phoneme in phonemes:
            if phoneme != ' ':
                pattern_value = self.phoneme_encoder.encode_phoneme(phoneme)
                pattern = generate_pattern(pattern_value & 0x7F, mode='phoneme')
                patterns.append(pattern)
        return patterns
    
    def _encode_character(self, text: str) -> List[Pattern]:
        """Encode as pure characters."""
        patterns = []
        for char in text:
            if char.isprintable():
                byte_value = ord(char) & 0x7F  # 7-bit only
                pattern = generate_pattern(byte_value, mode='character')
                patterns.append(pattern)
        return patterns
    
    def _encode_hybrid(self, text: str) -> List[Pattern]:
        """Encode using hybrid approach (phonemes for common words)."""
        words = text.split()
        patterns = []
        
        for word in words:
            # Check if word is common (use phonemes)
            if self._is_common_word(word):
                phonemes = self.phoneme_encoder.g2p_converter.text_to_phonemes(word)
                for phoneme in phonemes:
                    if phoneme != ' ':
                        pattern_value = self.phoneme_encoder.encode_phoneme(phoneme)
                        pattern = generate_pattern(pattern_value & 0x7F, mode='phoneme')
                        patterns.append(pattern)
            else:
                # Use character encoding for uncommon words
                for char in word:
                    byte_value = ord(char) & 0x7F
                    pattern = generate_pattern(byte_value, mode='character')
                    patterns.append(pattern)
            
            # Add space pattern
            patterns.append(generate_pattern(32, mode='character'))  # Space
        
        return patterns
    
    def _is_common_word(self, word: str) -> bool:
        """Check if word is in top 150 common words."""
        return word.lower() in TOP_150_WORDS
```

## Pattern Examples

### Example 1: Phoneme /h/

```
Pattern: 128 (binary: 10000000)
Actuators:
  - Actuator 7: ON  (mode = phoneme)
  - Actuators 0-6: OFF (phoneme ID = 0)
Duration: 80ms
```

### Example 2: Phoneme /ɛ/

```
Pattern: 129 (binary: 10000001)
Actuators:
  - Actuator 7: ON  (mode = phoneme)
  - Actuator 0: ON  (phoneme ID = 1)
  - Actuators 1-6: OFF
Duration: 80ms
```

### Example 3: Character 'A'

```
Pattern: 65 (binary: 01000001)
Actuators:
  - Actuator 7: OFF (mode = character)
  - Actuator 0: ON  (character ID = 65)
  - Actuators 1-6: OFF
Duration: 80ms
```

### Example 4: Word "the" (if using word patterns)

```
Pattern: 100 (binary: 01100100)
Actuators:
  - Actuator 7: OFF (mode = character/word)
  - Actuator 2: ON  (word ID = 100)
  - Actuator 5: ON
  - Actuator 6: ON
  - Other actuators: OFF
Duration: 200ms (word pattern, longer than character)
```

## Performance Optimization

### Pattern Duration

**All 8-bit patterns: 80ms**
- Character patterns: 80ms
- Phoneme patterns: 80ms
- Word patterns: 200-250ms (if implemented)

**Recommendation**: Keep all 8-bit patterns at 80ms for consistency and speed.

### Pattern Frequency Optimization

**Within phoneme space (128-255):**
- Common phonemes: Simpler bit patterns (fewer bits set)
- Rare phonemes: More complex patterns (more bits set)
- All: 80ms duration

**Example mapping:**
- /n/ (very common): Pattern 128 = 10000000 (only actuator 7)
- /t/ (very common): Pattern 129 = 10000001 (actuators 7, 0)
- /θ/ (rare): Pattern 200 = 11001000 (actuators 7, 6, 3)

## Testing Results Summary

### All Articles Tested

| Article | Single-Byte | 8-Bit Phoneme | Improvement |
|---------|-------------|---------------|------------|
| Romanian Villagers | 9.35 min | 8.36 min | **+10.6%** |
| Climate Crisis | 3.49 min | 3.21 min | **+8.0%** |
| AI Breakthrough | 3.43 min | 3.19 min | **+7.2%** |
| Healthcare Systems | 3.45 min | 3.21 min | **+6.7%** |
| **Average** | **4.93 min** | **4.49 min** | **+8.9%** |

### Key Metrics

- **Average speed improvement**: 8.9%
- **Pattern reduction**: 6.7-10.6% fewer patterns
- **Speed**: 13.4-14.0 characters/second
- **Consistency**: Works across all text types

## Recommendations

### Primary Implementation

**Use 8-bit phoneme encoding as default:**
- Fastest overall method
- Consistent performance
- Simple implementation
- Room for expansion

### Fallback Strategy

**Use character encoding when:**
- G2P conversion fails
- Proper nouns detected
- User preference
- Technical terms

### Future Enhancements

1. **Expand phoneme inventory**: Use remaining 88 patterns
2. **Optimize pattern design**: Frequency-based bit patterns
3. **Add word-level patterns**: Common words as single patterns
4. **Hybrid mode improvements**: Better word classification

## Conclusion

**8-bit phoneme encoding with mode indicator** provides the best performance while maintaining flexibility for character encoding when needed. The mode indicator approach elegantly solves capacity constraints while enabling maximum speed for both encoding types.

