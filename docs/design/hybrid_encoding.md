# Hybrid Encoding: Combining Character and Phoneme Modes

## Overview

This document explores ways to combine character-by-character and phoneme-based encoding modes to leverage the strengths of both approaches.

## Hybrid Approaches

### Approach 1: Adaptive Mode Switching

**Concept**: Automatically switch between modes based on content type.

**How it works:**
- **Words**: Use phoneme mode (faster, more efficient)
- **Non-words**: Use character mode (code, URLs, numbers, punctuation)
- **Unknown words**: Fallback to character mode if G2P fails

**Implementation:**
```python
def encode_text_adaptive(text: str) -> List[Pattern]:
    words = text.split()
    patterns = []
    
    for word in words:
        if is_word(word):  # Check if it's a real word
            try:
                # Try phoneme mode
                phoneme_patterns = phoneme_encoder.encode_text(word)
                patterns.extend(phoneme_patterns)
            except G2PError:
                # Fallback to character mode
                char_patterns = char_encoder.encode_text(word)
                patterns.extend(char_patterns)
        else:
            # Non-word (code, URL, etc.) - use character mode
            char_patterns = char_encoder.encode_text(word)
            patterns.extend(char_patterns)
    
    return patterns
```

**Pros:**
- ✅ Best of both worlds
- ✅ Automatic optimization
- ✅ Handles edge cases gracefully

**Cons:**
- ❌ Mode switching may be confusing
- ❌ Need word detection logic
- ❌ Inconsistent patterns for same word

---

### Approach 2: Dual Output (Parallel Patterns)

**Concept**: Send both character and phoneme patterns simultaneously or sequentially.

**How it works:**
- **Option A**: Character pattern first, then phoneme pattern
- **Option B**: Phoneme pattern first, then character pattern
- **Option C**: Both patterns simultaneously (different actuators)

**Implementation:**
```python
def encode_text_dual(text: str, order='phoneme_first') -> List[Pattern]:
    char_patterns = char_encoder.encode_text(text)
    phoneme_patterns = phoneme_encoder.encode_text(text)
    
    if order == 'phoneme_first':
        return phoneme_patterns + char_patterns
    elif order == 'character_first':
        return char_patterns + phoneme_patterns
    else:  # simultaneous
        # Interleave patterns (requires pattern merging)
        return merge_patterns(char_patterns, phoneme_patterns)
```

**Pros:**
- ✅ Provides both perspectives
- ✅ Aids learning (see both representations)
- ✅ Maximum information

**Cons:**
- ❌ Double the patterns (slower)
- ❌ May be overwhelming
- ❌ Higher cognitive load

---

### Approach 3: Word-Level Hybrid

**Concept**: Use phoneme mode for common words, character mode for rare/unknown words.

**How it works:**
- **Common words** (top 1000): Use phoneme mode
- **Rare words**: Use character mode
- **Unknown words**: Use character mode

**Implementation:**
```python
COMMON_WORDS = set(['the', 'be', 'to', 'of', 'and', ...])  # Top 1000 words

def encode_text_word_hybrid(text: str) -> List[Pattern]:
    words = text.split()
    patterns = []
    
    for word in words:
        word_lower = word.lower().strip('.,!?')
        
        if word_lower in COMMON_WORDS:
            # Common word - use phoneme mode
            patterns.extend(phoneme_encoder.encode_text(word))
        else:
            # Rare/unknown word - use character mode
            patterns.extend(char_encoder.encode_text(word))
    
    return patterns
```

**Pros:**
- ✅ Optimizes common words (phoneme)
- ✅ Handles rare words (character)
- ✅ Predictable behavior

**Cons:**
- ❌ Need word frequency dictionary
- ❌ Mode switching may be noticeable
- ❌ Inconsistent for same word in different contexts

---

### Approach 4: Layered Encoding (Intensity Variation)

**Concept**: Use character patterns with phoneme information encoded as intensity variation.

**How it works:**
- **Base layer**: Character patterns (spatial + temporal)
- **Overlay layer**: Phoneme information via intensity variation
- **Result**: Single pattern with dual information

**Implementation:**
```python
def encode_text_layered(text: str) -> List[Pattern]:
    char_patterns = char_encoder.encode_text(text)
    phoneme_patterns = phoneme_encoder.encode_text(text)
    
    # Merge: Use character spatial/temporal, add phoneme intensity
    merged = []
    for char_pat, phon_pat in zip(char_patterns, phoneme_patterns):
        # Adjust intensity based on phoneme match
        intensity = calculate_intensity(char_pat, phon_pat)
        char_pat.adjust_intensity(intensity)
        merged.append(char_pat)
    
    return merged
```

**Pros:**
- ✅ Single pattern stream
- ✅ Dual information encoded
- ✅ No mode switching

**Cons:**
- ❌ Complex to decode
- ❌ Intensity discrimination challenging
- ❌ May be confusing

---

### Approach 5: Context-Aware Hybrid

**Concept**: Switch modes based on context (typing vs. reading vs. speech).

**How it works:**
- **Typing input**: Character mode (immediate feedback)
- **Text reading**: Phoneme mode (word recognition)
- **Speech input**: Phoneme mode (natural)
- **Code/URLs**: Character mode (exact spelling)

**Implementation:**
```python
class ContextAwareEncoder:
    def encode(self, text: str, context: str) -> List[Pattern]:
        if context == 'typing':
            return char_encoder.encode_text(text)
        elif context == 'reading':
            return phoneme_encoder.encode_text(text)
        elif context == 'speech':
            return phoneme_encoder.encode_text(text)
        elif context == 'code':
            return char_encoder.encode_text(text)
        else:
            # Default: adaptive
            return self.encode_adaptive(text)
```

**Pros:**
- ✅ Context-appropriate encoding
- ✅ User control
- ✅ Optimized for use case

**Cons:**
- ❌ Requires context detection
- ❌ User must specify context
- ❌ More complex interface

---

## Recommended Approach: Adaptive Mode Switching

### Implementation Details

**Strategy:**
1. **Detect word boundaries**
2. **For each word:**
   - Try phoneme mode first
   - If G2P fails or word is non-standard → use character mode
3. **For non-words** (numbers, punctuation, code) → always character mode

**Word Detection:**
```python
def is_word(text: str) -> bool:
    """Check if text is a real word (not code, URL, etc.)."""
    # Remove punctuation
    cleaned = text.strip('.,!?;:')
    
    # Check if all alphabetic
    if not cleaned.replace("'", "").isalpha():
        return False
    
    # Check if it's a URL/code pattern
    if any(char in cleaned for char in ['/', ':', '@', '#', '$']):
        return False
    
    # Check if it's a number
    if cleaned.isdigit():
        return False
    
    return True
```

**G2P Confidence:**
```python
def encode_text_adaptive(text: str) -> List[Pattern]:
    words = text.split()
    patterns = []
    
    for word in words:
        if is_word(word):
            # Try phoneme mode
            try:
                phoneme_patterns = phoneme_encoder.encode_text(word)
                # Check G2P confidence (if available)
                if phoneme_encoder.get_confidence(word) > 0.8:
                    patterns.extend(phoneme_patterns)
                else:
                    # Low confidence - use character mode
                    patterns.extend(char_encoder.encode_text(word))
            except G2PError:
                # G2P failed - use character mode
                patterns.extend(char_encoder.encode_text(word))
        else:
            # Non-word - use character mode
            patterns.extend(char_encoder.encode_text(word))
        
        # Add space pattern
        patterns.append(space_pattern)
    
    return patterns
```

### Benefits

1. **Automatic optimization**: Uses best mode for each word
2. **Graceful fallback**: Character mode when phoneme fails
3. **Handles edge cases**: Code, URLs, numbers always character mode
4. **User-friendly**: No manual mode switching needed

### Challenges

1. **Mode switching**: Users may notice different patterns for same word
2. **Consistency**: Same word might encode differently in different contexts
3. **Word detection**: Need robust word detection logic
4. **G2P confidence**: Need confidence scoring for G2P

---

## Alternative: User-Selectable Hybrid

**Concept**: Let users choose hybrid strategy.

**Options:**
1. **Pure character**: Always character mode
2. **Pure phoneme**: Always phoneme mode
3. **Adaptive**: Automatic switching (recommended)
4. **Word-level**: Phoneme for common words, character for rare
5. **Dual output**: Both patterns (learning mode)

**Implementation:**
```python
class HybridEncoder:
    def __init__(self, strategy='adaptive'):
        self.strategy = strategy
        self.char_encoder = PatternEncoder()
        self.phoneme_encoder = PhonemeEncoder()
    
    def encode(self, text: str) -> List[Pattern]:
        if self.strategy == 'character':
            return self.char_encoder.encode_text(text)
        elif self.strategy == 'phoneme':
            return self.phoneme_encoder.encode_text(text)
        elif self.strategy == 'adaptive':
            return self.encode_adaptive(text)
        elif self.strategy == 'word_level':
            return self.encode_word_level(text)
        elif self.strategy == 'dual':
            return self.encode_dual(text)
```

---

## Performance Comparison

### Example: "Hello world! Visit https://example.com"

**Pure Character Mode:**
- Patterns: 38 (all characters)
- Duration: ~5700ms
- Accuracy: 100%

**Pure Phoneme Mode:**
- Patterns: ~30 (phonemes)
- Duration: ~4500ms
- Accuracy: ~95% (URL may fail)

**Adaptive Hybrid:**
- "Hello": Phoneme (4 patterns)
- "world": Phoneme (4 patterns)
- "!": Character (1 pattern)
- "Visit": Phoneme (4 patterns)
- "https://example.com": Character (19 patterns - URL)
- **Total**: ~32 patterns, ~4800ms
- **Accuracy**: ~98% (phoneme for words, character for URL)

**Result**: Hybrid provides best balance of efficiency and accuracy.

---

## Implementation Recommendations

### Phase 1: Basic Hybrid
1. Implement adaptive mode switching
2. Word detection logic
3. G2P fallback handling

### Phase 2: Enhanced Hybrid
1. G2P confidence scoring
2. Common word dictionary
3. User preference settings

### Phase 3: Advanced Hybrid
1. Context-aware switching
2. Dual output mode (learning)
3. Pattern merging for layered encoding

---

## User Experience Considerations

### Consistency
- **Issue**: Same word might encode differently
- **Solution**: Cache encoding decisions, use consistent mode per word

### Learning Curve
- **Issue**: Mode switching may confuse users
- **Solution**: Visual indicator showing which mode is active
- **Alternative**: Let users choose pure mode initially

### Feedback
- **Issue**: Users may not understand why mode switched
- **Solution**: Show mode indicator, explain switching logic

---

## Conclusion

**Yes, combining modes is possible and beneficial!**

**Recommended Approach**: **Adaptive Mode Switching**
- Automatically uses phoneme mode for words
- Falls back to character mode for non-words
- Provides best balance of efficiency and accuracy
- User-friendly (no manual switching needed)

**Alternative**: **User-Selectable Hybrid**
- Let users choose strategy
- Supports pure modes and hybrid modes
- Maximum flexibility

**Key Benefits:**
- ✅ Best of both worlds
- ✅ Automatic optimization
- ✅ Handles edge cases
- ✅ Better efficiency than pure character
- ✅ Better accuracy than pure phoneme (for non-words)

---

## Related Documents

- [Encoding Mode Comparison](encoding_mode_comparison.md)
- [Phoneme Encoding Design](phoneme_encoding.md)
- [Encoding System Design](encoding_system.md)

