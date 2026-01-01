# Character Capacity: Single-Byte Encoding

## Overview

This document calculates the character capacity of the ring layout design using single-byte encoding.

## Single-Byte Encoding Capacity

### Basic Calculation

**8-bit encoding:**
- **Bits per pattern**: 8 bits
- **Total possible patterns**: 2^8 = **256 patterns**
- **Character capacity**: **256 distinct characters**

### Character Set Coverage

**Extended ASCII (8-bit):**
- **Basic ASCII (7-bit)**: 128 characters (0-127)
- **Extended ASCII (8-bit)**: 256 characters (0-255)
- **Single-byte capacity**: ✅ **256 characters** (covers Extended ASCII)

**Unicode:**
- **Full Unicode range**: 1,114,112 characters (U+0000 to U+10FFFF)
- **Single-byte limitation**: ❌ Cannot encode full Unicode (needs multi-byte)

### Practical Character Sets

**English Language:**
- **Uppercase letters (A-Z)**: 26 characters
- **Lowercase letters (a-z)**: 26 characters
- **Numbers (0-9)**: 10 characters
- **Common punctuation**: ~20 characters (space, period, comma, etc.)
- **Total**: ~82 characters

**Remaining Capacity:**
- **Used**: ~82 characters
- **Available**: ~174 patterns (for extended ASCII, symbols, etc.)

## Pattern Distribution

### Ring Layout (4+4)

**Lower Ring (4 bits):**
- **Possible patterns**: 2^4 = **16 patterns**
- **Actuators**: 0-3 (4 positions)

**Upper Ring (4 bits):**
- **Possible patterns**: 2^4 = **16 patterns**
- **Actuators**: 4-7 (4 positions)

**Combined:**
- **Total patterns**: 16 × 16 = **256 patterns**
- **Natural split**: Lower 4 bits + Upper 4 bits

### Encoding Examples

**Character 'A' = 65 = 0b01000001**
- Lower ring (0101): Actuators 0, 2
- Upper ring (0100): Actuator 5
- **Pattern**: Lower (top+bottom), Upper (right)

**Character 'a' = 97 = 0b01100001**
- Lower ring (0001): Actuator 0
- Upper ring (0110): Actuators 5, 6
- **Pattern**: Lower (top), Upper (right+bottom)

**Character '0' = 48 = 0b00110000**
- Lower ring (0000): None
- Upper ring (0011): Actuators 4, 5
- **Pattern**: Lower (none), Upper (top+right)

## Comparison with Other Encoding Methods

### Single-Byte Encoding

**Capacity:**
- **Patterns**: 256 (2^8)
- **Coverage**: Extended ASCII (256 characters)
- **Duration**: 80ms per character
- **Latency**: <1ms (direct lookup)

### Temporal Encoding (Current)

**Capacity:**
- **Patterns**: ~40-50 (alphabet + numbers + punctuation)
- **Coverage**: Basic character set
- **Duration**: 150-320ms per character
- **Latency**: <1ms (lookup table)

### Phoneme Encoding

**Capacity:**
- **Patterns**: ~44 (English phonemes)
- **Coverage**: Phoneme set
- **Duration**: Varies by phoneme
- **Latency**: ~1-50ms (G2P conversion)

## Character Coverage Analysis

### ASCII Character Set (128 characters)

**Control Characters (0-31):**
- **32 patterns**: Non-printable (may not need encoding)
- **Usage**: Could skip or use special patterns

**Printable ASCII (32-126):**
- **95 characters**: All printable ASCII
- **Coverage**: ✅ Fully covered by 256 patterns

**Extended ASCII (128-255):**
- **128 characters**: Extended symbols, accented characters
- **Coverage**: ✅ Fully covered by 256 patterns

### Common Use Cases

**English Text:**
- **Alphabet**: 52 characters (A-Z, a-z)
- **Numbers**: 10 characters (0-9)
- **Punctuation**: ~20 characters
- **Total**: ~82 characters
- **Remaining**: ~174 patterns available

**Code/Programming:**
- **ASCII**: 128 characters
- **Extended**: May need some extended ASCII
- **Coverage**: ✅ Fully covered

**International Text:**
- **Extended ASCII**: 256 characters (covers many European languages)
- **Full Unicode**: Not covered (would need multi-byte encoding)

## Pattern Utilization

### Current Pattern Usage

**Letter-Based Encoder:**
- **Patterns defined**: ~40-50 (alphabet + numbers + punctuation)
- **Utilization**: ~16-20% of 256 capacity

**Single-Byte Encoder:**
- **Patterns possible**: 256 (all Extended ASCII)
- **Utilization**: 100% capacity (direct ASCII mapping)

### Pattern Optimization Opportunities

**Frequency-Based Bit Patterns:**
- **Common characters**: Use simpler bit patterns (fewer bits set)
- **Rare characters**: Can use complex patterns (many bits set)
- **Example**: 'E' = 0b00000001 (only 1 bit), 'Z' = 0b11111111 (all bits)

**Benefits:**
- Common letters = simpler patterns = easier perception
- Rare letters = complex patterns = acceptable (rarely used)

## Multi-Byte Encoding (Future)

### Unicode Support

**If needed for full Unicode:**

**Option 1: UTF-8 Encoding**
- **1 byte**: ASCII (0-127)
- **2 bytes**: Latin, Greek, Cyrillic, etc.
- **3 bytes**: Chinese, Japanese, Korean, etc.
- **4 bytes**: Rare/emoji characters

**Option 2: UTF-16 Encoding**
- **2 bytes**: Most characters (65,536 patterns)
- **4 bytes**: Rare characters (surrogate pairs)

**Implementation:**
```python
def encode_unicode(char: str) -> List[Pattern]:
    """Encode Unicode character (may need multiple bytes)."""
    utf8_bytes = char.encode('utf-8')
    patterns = []
    for byte in utf8_bytes:
        patterns.append(single_byte_encoder.encode_byte(byte))
    return patterns
```

**Tradeoff:**
- **ASCII**: 1 pattern (80ms)
- **Extended**: 1 pattern (80ms)
- **Unicode**: 2-4 patterns (160-320ms)

## Summary

### Single-Byte Encoding Capacity

**Total Patterns: 256 (2^8)**

**Coverage:**
- ✅ **Extended ASCII**: 256 characters (fully covered)
- ✅ **English text**: ~82 characters (32% utilization)
- ✅ **Code/programming**: 128+ characters (fully covered)
- ❌ **Full Unicode**: Not covered (needs multi-byte)

**Pattern Distribution:**
- **Lower ring (4 bits)**: 16 patterns
- **Upper ring (4 bits)**: 16 patterns
- **Combined**: 256 total patterns

**Practical Capacity:**
- **Common characters**: ~82 (alphabet, numbers, punctuation)
- **Remaining**: ~174 patterns (for extended ASCII, symbols, etc.)
- **Total usable**: 256 characters

## Conclusion

**Single-byte encoding with ring layout supports 256 distinct characters**, which covers:
- ✅ All Extended ASCII (256 characters)
- ✅ English text (alphabet, numbers, punctuation)
- ✅ Code/programming (ASCII + extended)
- ✅ Many European languages (extended ASCII)

**This is more than sufficient** for most use cases. Full Unicode support would require multi-byte encoding (2-4 patterns per character for non-ASCII).

