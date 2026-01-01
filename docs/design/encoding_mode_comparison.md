# Encoding Mode Comparison: Character vs. Phoneme

## Overview

Teletypathy supports two encoding modes with different strengths and use cases. This document compares character-by-character (letter-based) and phoneme-based encoding approaches.

## Two Encoding Modes

### Mode 1: Character-by-Character (Letter-Based)

**What it is:**
- Direct mapping: Each typed character → tactile pattern
- Text-based: Works with any text input (typing, copy-paste, etc.)
- Spelling-focused: Preserves exact spelling of words

**How it works:**
```
User types: "hello"
↓
Character encoder: h → e → l → l → o
↓
5 tactile patterns (one per character)
```

### Mode 2: Phoneme-Based

**What it is:**
- Speech-sound mapping: Text → phonemes → tactile patterns
- Speech-aligned: Matches how words are pronounced
- Pronunciation-focused: Represents spoken sounds, not spelling

**How it works:**
```
User types: "hello"
↓
G2P conversion: "hello" → /h/ /ə/ /l/ /oʊ/
↓
4 tactile patterns (one per phoneme)
```

## Key Differences

### 1. Input Processing

**Character Mode:**
- **Direct**: Character → Pattern (no conversion)
- **Latency**: <1ms (lookup table)
- **No dependencies**: Works with any text
- **Spelling preserved**: Exact character sequence maintained

**Phoneme Mode:**
- **Conversion required**: Text → Phonemes → Patterns
- **Latency**: ~1-50ms (G2P conversion adds overhead)
- **G2P dependency**: Requires grapheme-to-phoneme conversion
- **Pronunciation-based**: Represents sounds, not spelling

### 2. Pattern Count

**Character Mode:**
- **Patterns per word**: Usually equals character count
- **Example**: "hello" = 5 patterns (h-e-l-l-o)
- **Longer words**: More patterns (e.g., "teletypathy" = 11 patterns)

**Phoneme Mode:**
- **Patterns per word**: Usually fewer than characters
- **Example**: "hello" = 4 patterns (/h/-/ə/-/l/-/oʊ/)
- **Efficiency**: Often 10-30% fewer patterns than character mode

### 3. Learning Approach

**Character Mode:**
- **Learn letters**: Master 26 letters + numbers + punctuation
- **Spell words**: Recognize words by spelling them out
- **Visual alignment**: Matches what you see on screen
- **Familiar**: Similar to learning to type or read

**Phoneme Mode:**
- **Learn phonemes**: Master ~44 phonemes
- **Recognize words**: Direct word recognition from phonemes
- **Speech alignment**: Matches how words sound
- **Less familiar**: Requires learning phoneme system

### 4. Word Recognition

**Character Mode:**
- **Process**: Character → Character → Character → Recognize word
- **Speed**: Slower (must process each character)
- **Method**: Spell out, then recognize word
- **Example**: h-e-l-l-o → "hello"

**Phoneme Mode:**
- **Process**: Phoneme → Phoneme → Recognize word directly
- **Speed**: Faster (direct word recognition)
- **Method**: Recognize word from phoneme sequence
- **Example**: /h/-/ə/-/l/-/oʊ/ → "hello" (direct recognition)

### 5. Accuracy and Errors

**Character Mode:**
- **Accuracy**: ~100% (direct mapping, no conversion)
- **Errors**: None (1:1 character mapping)
- **Spelling variations**: Handled correctly (e.g., "color" vs "colour")
- **Unknown words**: Always works (no conversion needed)

**Phoneme Mode:**
- **Accuracy**: ~95-98% (depends on G2P quality)
- **Errors**: G2P conversion errors possible
- **Spelling variations**: May map differently (e.g., "color" vs "colour" → same phonemes)
- **Unknown words**: May fail if G2P doesn't recognize word

### 6. Use Cases

**Character Mode:**
- **Typing feedback**: Real-time keystroke feedback
- **Text reading**: Reading any text (code, URLs, names)
- **Spelling practice**: Learning spelling through tactile feedback
- **Universal**: Works with any text, any language (if patterns defined)
- **Debugging**: See exact characters being transmitted

**Phoneme Mode:**
- **Speech-to-text**: Converting speech to tactile patterns
- **Word recognition**: Faster word-level comprehension
- **Language learning**: Learning pronunciation through tactile feedback
- **Natural speech**: Better matches spoken language rhythm
- **Vocabulary building**: Research shows 500+ words learnable (TAPS)

## Detailed Comparison Table

| Aspect | Character Mode | Phoneme Mode |
|--------|---------------|--------------|
| **Pattern Count** | Usually more (1 per character) | Usually fewer (1 per phoneme) |
| **"hello" patterns** | 5 patterns | 4 patterns |
| **Latency** | <1ms (direct lookup) | ~1-50ms (G2P conversion) |
| **Accuracy** | ~100% (no conversion) | ~95-98% (G2P dependent) |
| **Learning Curve** | Moderate (26 letters) | Steeper (44 phonemes) |
| **Word Recognition** | Spell out, then recognize | Direct word recognition |
| **Speed** | Slower (character-by-character) | Faster (word-level) |
| **Spelling** | Preserved exactly | Pronunciation-based |
| **Dependencies** | None | G2P library needed |
| **Use Cases** | Typing, text reading, spelling | Speech, word recognition, learning |
| **Unknown Words** | Always works | May fail if G2P doesn't know |
| **Code/URLs** | Works perfectly | May struggle (not natural speech) |
| **Research Support** | Skin Reading (2016) | TAPS (2020) - 500 words learned |

## Tradeoffs

### Character Mode: Pros and Cons

**Pros:**
- ✅ **100% accuracy**: No conversion errors
- ✅ **Universal**: Works with any text (code, URLs, names)
- ✅ **Low latency**: <1ms pattern generation
- ✅ **Familiar**: Matches visual text
- ✅ **No dependencies**: Works out of the box
- ✅ **Spelling preserved**: Exact character sequence
- ✅ **Debugging**: Easy to see what's being transmitted

**Cons:**
- ❌ **More patterns**: Usually more patterns per word
- ❌ **Slower recognition**: Must spell out words
- ❌ **Less efficient**: More bandwidth/patterns needed
- ❌ **No speech alignment**: Doesn't match pronunciation

### Phoneme Mode: Pros and Cons

**Pros:**
- ✅ **Fewer patterns**: Usually 10-30% fewer patterns
- ✅ **Faster recognition**: Direct word recognition
- ✅ **Speech-aligned**: Matches pronunciation
- ✅ **Research-backed**: TAPS shows 500 words learnable
- ✅ **Natural rhythm**: Matches speech timing
- ✅ **Word-level learning**: Learn words, not just letters

**Cons:**
- ❌ **G2P dependency**: Requires conversion library
- ❌ **Conversion errors**: ~2-5% error rate possible
- ❌ **Higher latency**: G2P adds 1-50ms overhead
- ❌ **Steeper learning**: 44 phonemes vs. 26 letters
- ❌ **Spelling lost**: Doesn't preserve exact spelling
- ❌ **Code/URLs**: May struggle with non-speech text
- ❌ **Unknown words**: May fail if G2P doesn't recognize

## When to Use Each Mode

### Use Character Mode When:

1. **Real-time typing feedback**
   - Typing on keyboard
   - Want immediate character-by-character feedback
   - Need to see exact characters

2. **Reading text/code**
   - Reading code, URLs, technical terms
   - Need exact spelling preserved
   - Non-speech content

3. **Spelling practice**
   - Learning spelling through tactile feedback
   - Want to see exact character sequence
   - Educational use

4. **Universal compatibility**
   - Need to work with any text
   - Don't want G2P dependencies
   - Maximum compatibility

5. **Debugging/development**
   - Need to see exact characters
   - Testing pattern encoding
   - Development work

### Use Phoneme Mode When:

1. **Speech-to-text applications**
   - Converting speech to tactile patterns
   - Speech recognition systems
   - Voice input

2. **Word recognition focus**
   - Want faster word comprehension
   - Learning vocabulary
   - Word-level communication

3. **Language learning**
   - Learning pronunciation
   - Pronunciation practice
   - Speech-focused learning

4. **Natural speech rhythm**
   - Want patterns to match speech
   - Natural language processing
   - Conversational interfaces

5. **Efficiency priority**
   - Want fewer patterns
   - Bandwidth optimization
   - Faster communication

## Performance Comparison

### Pattern Count Example

**Word: "teletypathy"**

**Character Mode:**
- Patterns: 11 (t-e-l-e-t-y-p-a-t-h-y)
- Total duration: ~1650ms (11 × 150ms average)

**Phoneme Mode:**
- Patterns: 10 (/t/-/ɛ/-/l/-/ɪ/-/t/-/aɪ/-/p/-/ə/-/θ/-/i/)
- Total duration: ~1200ms (varies by phoneme)
- **Savings**: 1 pattern, ~450ms faster

### Latency Comparison

**Character Mode:**
- Pattern generation: <1ms
- Total latency: <1ms

**Phoneme Mode:**
- G2P conversion: ~1-50ms (depends on library)
- Pattern generation: <1ms
- Total latency: ~2-51ms

**Tradeoff**: Phoneme mode adds latency but provides efficiency gains.

### Learning Curve Comparison

**Character Mode:**
- **Patterns to learn**: ~40 (26 letters + 10 numbers + punctuation)
- **Learning time**: Moderate (familiar concept)
- **Recognition**: Character-by-character, then word
- **Research**: Skin Reading (2016) - several weeks to months

**Phoneme Mode:**
- **Patterns to learn**: ~44 phonemes
- **Learning time**: Steeper (less familiar)
- **Recognition**: Direct word recognition
- **Research**: TAPS (2020) - 500 words learned, faster word recognition

## Research Evidence

### Character Mode: Skin Reading (2016)

**Findings:**
- 6-channel haptic display
- Letter-based encoding
- ~60-80% word recognition after training
- Several weeks to months for basic proficiency

**Strengths:**
- Simple, direct mapping
- Familiar concept (letters)
- Good for learning

### Phoneme Mode: TAPS (2020)

**Findings:**
- Phoneme-based tactile display
- **500 English words learned** through phonemes
- Faster word recognition than letter-based
- Two-way communication demonstrated (2024)

**Strengths:**
- Faster word recognition
- More efficient (fewer patterns)
- Better for vocabulary building

## Hybrid Approach

### Best of Both Worlds

**Option 1: Mode Switching**
- Start in character mode (learning)
- Switch to phoneme mode (efficiency)
- User chooses based on context

**Option 2: Adaptive Mode**
- Character mode for unknown words
- Phoneme mode for known words
- Automatic switching based on G2P confidence

**Option 3: Dual Output**
- Both patterns available
- User can choose which to feel
- Compare character vs. phoneme patterns

## Recommendations

### For Beginners
**Start with Character Mode:**
- More familiar (letters)
- Easier to learn
- No dependencies
- 100% accuracy

### For Advanced Users
**Consider Phoneme Mode:**
- Faster word recognition
- More efficient
- Better for vocabulary
- Research shows superior learning

### For Production
**Support Both Modes:**
- Let users choose
- Character mode for compatibility
- Phoneme mode for efficiency
- Mode switching capability

## Conclusion

**Character Mode** is better for:
- Universal compatibility
- Exact spelling preservation
- Real-time typing feedback
- Code/technical text

**Phoneme Mode** is better for:
- Faster word recognition
- Speech-to-text applications
- Vocabulary building
- Natural speech rhythm

**Best Practice**: Support both modes and let users choose based on their needs and context.

## Related Documents

- [Phoneme Encoding Design](phoneme_encoding.md)
- [Encoding System Design](encoding_system.md)
- [Comparative Analysis](../research/comparative_analysis.md)
- [Training Texts](../development/training_texts.md)

