# Symbol Mapping

## Overview

Detailed character-to-tactile pattern mappings for the Teletypathy system. This document provides the complete mapping table and pattern definitions.

## Actuator Layout

### Standard Layout (8 Actuators)

```
Actuator positions (left to right):
[0] [1] [2] [3] [4] [5] [6] [7]
```

**Body placement**: Forearm or wrist, linear array
**Spacing**: 40-50mm between actuators
**Numbering**: 0 = leftmost, 7 = rightmost

### Alternative Layouts

#### 6 Actuators
- Use actuators 0-5
- Actuator 5 reserved for number marker

#### 4 Actuators
- Use actuators 0-3
- Reduced spatial encoding capability

## Pattern Notation

### Notation Format
```
Pattern: [Actuators] Duration(ms) [Details]
```

**Examples**:
- `[0] 150` = Actuator 0, 150ms pulse
- `[0→1] 100+50+100` = Actuator 0 (100ms), gap (50ms), Actuator 1 (100ms)
- `[0,4] 150` = Actuators 0 and 4 simultaneously, 150ms
- `[0→1→2→3→4] 80×5` = Sequential across 5 actuators, 80ms each

## Alphabet Mappings

### High-Frequency Letters (Single Actuator, Short Pulse)

| Character | Frequency | Pattern | Description |
|-----------|-----------|---------|-------------|
| **E** | 12.7% | `[0] 150` | Leftmost actuator, short pulse |
| **T** | 9.1% | `[1] 150` | Second actuator, short pulse |
| **A** | 8.2% | `[2] 150` | Center-left, short pulse |
| **O** | 7.5% | `[3] 150` | Center, short pulse |
| **I** | 7.0% | `[4] 150` | Center-right, short pulse |

**Rationale**: Most common letters get simplest, fastest patterns

### Medium-High Frequency Letters (Two Actuator Sequential)

| Character | Frequency | Pattern | Description |
|-----------|-----------|---------|-------------|
| **N** | 6.7% | `[0→1] 100+50+100` | Left sequence, two pulses |
| **S** | 6.3% | `[1→2] 100+50+100` | Left-center sequence |
| **H** | 6.1% | `[2→3] 100+50+100` | Center sequence |
| **R** | 6.0% | `[3→4] 100+50+100` | Center-right sequence |
| **D** | 4.3% | `[4→5] 100+50+100` | Right sequence |
| **L** | 4.0% | `[5→6] 100+50+100` | Far-right sequence |

**Rationale**: Common letters use two-actuator patterns for distinction

### Medium Frequency Letters (Three Actuator Patterns)

| Character | Frequency | Pattern | Description |
|-----------|-----------|---------|-------------|
| **C** | 2.8% | `[0→1→2] 80+40+80+40+80` | Left three-actuator sequence |
| **U** | 2.8% | `[1→2→3] 80+40+80+40+80` | Center-left sequence |
| **M** | 2.4% | `[2→3→4] 80+40+80+40+80` | Center sequence |
| **W** | 2.4% | `[3→4→5] 80+40+80+40+80` | Center-right sequence |
| **F** | 2.2% | `[4→5→6] 80+40+80+40+80` | Right sequence |
| **G** | 2.0% | `[5→6→7] 80+40+80+40+80` | Far-right sequence |
| **Y** | 2.0% | `[0→2→4] 80+40+80+40+80` | Alternating left pattern |
| **P** | 1.9% | `[1→3→5] 80+40+80+40+80` | Alternating center pattern |
| **B** | 1.5% | `[2→4→6] 80+40+80+40+80` | Alternating right pattern |
| **V** | 1.0% | `[3→5→7] 80+40+80+40+80` | Alternating far-right pattern |

**Rationale**: Medium frequency uses three-actuator patterns

### Low Frequency Letters (Complex Patterns)

| Character | Frequency | Pattern | Description |
|-----------|-----------|---------|-------------|
| **K** | 0.8% | `[0→1→2→3] 70+30+70+30+70+30+70` | Four-actuator sequence |
| **J** | 0.15% | `[4→3→2→1] 70+30+70+30+70+30+70` | Reverse four-actuator |
| **X** | 0.15% | `[0,7]→[1,6]→[2,5]→[3,4] 100×3` | Simultaneous inward |
| **Q** | 0.10% | `[0→1→2→3→4→5→6→7] 60×8` | Full sequence |
| **Z** | 0.07% | `[7→6→5→4→3→2→1→0] 60×8` | Full reverse sequence |

**Rationale**: Rare letters can use longer, more complex patterns

## Number Mappings

### Number Encoding Strategy

**Marker**: All numbers start with actuator 5 (or rightmost available)
**Encoding**: Sequential pulses on actuators 0-4 represent number value

| Number | Pattern | Description |
|--------|---------|-------------|
| **0** | `[5] 200` | Marker only (long pulse) |
| **1** | `[5] 100 + [0] 150` | Marker + actuator 0 |
| **2** | `[5] 100 + [0→1] 100+50+100` | Marker + actuators 0,1 |
| **3** | `[5] 100 + [0→1→2] 80×3` | Marker + actuators 0,1,2 |
| **4** | `[5] 100 + [0→1→2→3] 70×4` | Marker + actuators 0,1,2,3 |
| **5** | `[5] 100 + [0→1→2→3→4] 60×5` | Marker + all left actuators |
| **6** | `[5] 100 + [4→3→2→1→0] 60×5` | Marker + reverse sequence |
| **7** | `[5] 100 + [0,4]→[1,3]→[2] 100×3` | Marker + simultaneous pattern |
| **8** | `[5] 100 + [0→2→4→1→3] 80×5` | Marker + alternating pattern |
| **9** | `[5] 100 + [0→1→2→3→4] 50×5 + [0] 100` | Marker + sequence + repeat |

**Rationale**: Distinctive marker distinguishes numbers from letters

## Punctuation Mappings

### Common Punctuation

| Symbol | Frequency | Pattern | Description |
|--------|-----------|---------|-------------|
| **Space** | ~18% | `[pause] 300` | 300ms pause (no vibration) |
| **.** (Period) | High | `[0,1,2,3,4,5,6,7] 200` | All actuators, long pulse |
| **,** (Comma) | High | `[0,7] 150` | Outer actuators, short pulse |
| **?** (Question) | Medium | `[0→4→0] 100+50+100+50+100` | Three-pulse sequence |
| **!** (Exclamation) | Medium | `[0,1,2,3,4,5,6,7] 150+50+150` | All actuators, double pulse |
| **:** (Colon) | Low | `[2,5] 100+50+100` | Center actuators, double pulse |
| **;** (Semicolon) | Low | `[1,6] 100+50+100` | Side actuators, double pulse |
| **-** (Hyphen) | Medium | `[3,4] 200` | Center actuators, long pulse |
| **'** (Apostrophe) | Medium | `[0] 100` | Single short pulse |
| **"** (Quote) | Medium | `[0→7] 100+50+100` | Outer sequence |

### Less Common Punctuation

| Symbol | Pattern | Description |
|--------|---------|-------------|
| **(** | `[0→1→2] 80×3` | Left sequence |
| **)** | `[2→1→0] 80×3` | Reverse left sequence |
| **[** | `[5→6→7] 80×3` | Right sequence |
| **]** | `[7→6→5] 80×3` | Reverse right sequence |
| **{** | `[0→2→4] 80×3` | Alternating left |
| **}** | `[4→2→0] 80×3` | Reverse alternating left |

## Control Characters

### Special Patterns

| Character | Pattern | Description |
|-----------|---------|-------------|
| **Enter/Return** | `[0,1,2,3,4,5,6,7] 100×3` | All actuators, triple pulse |
| **Backspace** | `[7→6→5→4→3→2→1→0] 50×8` | Fast reverse sequence |
| **Tab** | `[0→7] 150+100+150` | Outer sequence, longer |
| **Escape** | `[0,7]→[1,6]→[2,5]→[3,4] 100×4` | Simultaneous inward, 4 phases |
| **Delete** | `[0→1→2→3→4→5→6→7] 80×8 + [0,7] 200` | Full sequence + outer long |

## Pattern Timing Summary

### Timing Standards

- **Short pulse**: 100-150ms
- **Medium pulse**: 150-200ms
- **Long pulse**: 200-300ms
- **Inter-pulse gap**: 40-50ms (minimum), 50-100ms (recommended)
- **Inter-pattern spacing**: 150ms minimum
- **Pattern duration**: 200-500ms typical

### Pattern Complexity

- **Simple**: 1 actuator, 1 pulse (150ms) = ~150ms total
- **Medium**: 2-3 actuators, sequential (250-350ms total)
- **Complex**: 4+ actuators or simultaneous (400-600ms total)

## Implementation Notes

### Lookup Table Structure

```python
# Pseudocode structure
PATTERN_MAP = {
    'E': Pattern(actuators=[0], duration=150),
    'T': Pattern(actuators=[1], duration=150),
    # ... etc
}
```

### Pattern Serialization

Each pattern can be serialized as:
- **Actuator sequence**: List of actuator IDs
- **Timing**: List of (time_offset, duration) tuples
- **Total duration**: Sum of all timing events + gaps

### Optimization Notes

1. **Pre-compute**: All patterns in lookup table
2. **Cache**: Frequently used patterns in memory
3. **Batch**: Multiple patterns in one message if possible
4. **Compress**: If patterns repeat (future optimization)

## Learning Progression

### Stage 1: Common Letters
- Learn: E, T, A, O, I (single actuator patterns)
- Practice: Simple words using these letters
- Goal: Recognize 5 most common letters

### Stage 2: Medium Frequency
- Learn: N, S, H, R, D, L (two-actuator patterns)
- Practice: More words, simple sentences
- Goal: Recognize alphabet (letters)

### Stage 3: Full Alphabet
- Learn: Remaining letters (three+ actuator patterns)
- Practice: Full words, sentences
- Goal: Complete alphabet recognition

### Stage 4: Numbers and Punctuation
- Learn: Numbers 0-9, common punctuation
- Practice: Mixed text with numbers and punctuation
- Goal: Full character set

### Stage 5: Advanced
- Learn: Less common punctuation, control characters
- Practice: Complex text, code, special characters
- Goal: Full system proficiency

## Related Documents

- [Encoding System Design](encoding_system.md): Overall encoding strategy
- [Protocol Specification](protocol_spec.md): Communication protocol
- [Learning Theory Research](../research/learning_theory.md): Learning progression


