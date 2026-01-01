# Encoding System Design

## Overview

Proposed encoding scheme for translating characters into tactile patterns, based on research findings from Phase 1.

## Design Principles

### Core Principles
1. **Simplicity**: Start with direct, learnable mappings
2. **Consistency**: Similar patterns for related characters
3. **Frequency optimization**: Shorter patterns for common characters
4. **Multi-dimensional**: Spatial + temporal encoding
5. **Learnability**: Designed for muscle memory development

### Design Constraints
- **Latency**: <10ms end-to-end target
- **Actuators**: 4-8 vibration motors (LRA)
- **Pattern duration**: 100-300ms per character
- **Recognition**: Must be reliably distinguishable
- **Learning**: Should be learnable with practice

## Encoding Dimensions

### Spatial Encoding

#### Actuator Layout
- **Number of actuators**: 4-8 (recommended: 6-8)
- **Layout**: Linear array or grid
- **Spacing**: 40-50mm between actuators (optimal)
- **Body location**: Forearm, wrist, or torso

#### Spatial Patterns
- **Single actuator**: One motor activates
- **Sequential**: Pattern moves across actuators
- **Simultaneous**: Multiple actuators at once
- **Combined**: Sequential + simultaneous

### Temporal Encoding

#### Timing Structure
- **Pulse duration**: 100-200ms per pulse
- **Inter-pulse interval**: 50-100ms
- **Pattern duration**: 200-500ms total
- **Inter-pattern spacing**: 150ms minimum

#### Rhythm Patterns
- **Single pulse**: One vibration
- **Double pulse**: Two pulses (dit-dit)
- **Triple pulse**: Three pulses
- **Long pulse**: Extended duration
- **Rhythm sequences**: Complex timing patterns

### Intensity Encoding (Optional)

#### Amplitude Levels
- **Levels**: 2-3 intensity levels
- **Discrimination**: ~20% difference detectable
- **Range**: 0.5-2.0 m/s² comfortable
- **Application**: Emphasis, word boundaries

## Character Mapping Strategy

### Direct Character Mapping

#### Alphabet (26 letters)
- **Pattern type**: Spatial + temporal
- **Structure**: Consistent across alphabet
- **Optimization**: Shorter patterns for common letters

#### Numbers (0-9)
- **Pattern type**: Distinct from letters
- **Structure**: Consistent numeric pattern
- **Encoding**: Spatial or temporal distinction

#### Punctuation
- **Pattern type**: Distinct markers
- **Common**: Space, period, comma
- **Structure**: Shorter patterns for common punctuation

#### Control Characters
- **Pattern type**: Special patterns
- **Examples**: Backspace, enter, tab
- **Structure**: Distinctive, memorable

### Frequency-Based Optimization

#### Common Characters (Shorter Patterns)
- **E, T, A, O, I**: Single actuator, short pulse
- **N, S, H, R**: Single actuator, medium pulse
- **D, L**: Two actuators, short sequence

#### Less Common Characters (Longer Patterns)
- **Z, Q, X**: Multi-actuator, longer sequence
- **J, K**: Distinctive patterns
- **Punctuation**: Varies by frequency

## Pattern Library Design

### Pattern Structure

#### Basic Pattern Format
```
Pattern {
    actuators: [actuator_ids],      // Which motors
    sequence: [timing_events],      // When to activate
    intensities: [intensity_levels], // How strong (optional)
    duration: total_ms              // Total pattern time
}
```

#### Timing Event Format
```
TimingEvent {
    time_offset: ms,        // Time from pattern start
    actuator: id,           // Which actuator
    duration: ms,           // How long
    intensity: level       // How strong (optional)
}
```

### Alphabet Patterns (Proposed)

#### High-Frequency Letters (Short Patterns)

**E** (12.7% frequency):
- Actuator: 0 (leftmost)
- Pattern: Single pulse, 150ms
- Rationale: Most common, simplest pattern

**T** (9.1% frequency):
- Actuator: 1
- Pattern: Single pulse, 150ms
- Rationale: Very common, simple pattern

**A** (8.2% frequency):
- Actuator: 2
- Pattern: Single pulse, 150ms
- Rationale: Common, simple pattern

**O** (7.5% frequency):
- Actuator: 3
- Pattern: Single pulse, 150ms
- Rationale: Common, simple pattern

**I** (7.0% frequency):
- Actuator: 4
- Pattern: Single pulse, 150ms
- Rationale: Common, simple pattern

#### Medium-Frequency Letters (Medium Patterns)

**N** (6.7% frequency):
- Actuators: 0 → 1 (sequential)
- Pattern: Two pulses, 100ms each, 50ms gap
- Rationale: Distinctive, still efficient

**S** (6.3% frequency):
- Actuators: 1 → 2 (sequential)
- Pattern: Two pulses, 100ms each, 50ms gap
- Rationale: Distinctive pattern

**H** (6.1% frequency):
- Actuators: 2 → 3 (sequential)
- Pattern: Two pulses, 100ms each, 50ms gap
- Rationale: Distinctive pattern

**R** (6.0% frequency):
- Actuators: 3 → 4 (sequential)
- Pattern: Two pulses, 100ms each, 50ms gap
- Rationale: Distinctive pattern

#### Lower-Frequency Letters (Longer Patterns)

**Z** (0.07% frequency):
- Actuators: 0 → 1 → 2 → 3 → 4 (sequential)
- Pattern: Five pulses, 80ms each, 40ms gaps
- Rationale: Rare, can use longer pattern

**Q** (0.10% frequency):
- Actuators: 4 → 3 → 2 → 1 → 0 (reverse)
- Pattern: Five pulses, 80ms each, 40ms gaps
- Rationale: Rare, distinctive reverse pattern

**X** (0.15% frequency):
- Actuators: 0, 4 (simultaneous) → 1, 3 (simultaneous) → 2
- Pattern: Three-phase, 100ms each phase
- Rationale: Rare, distinctive simultaneous pattern

### Numbers (0-9)

#### Pattern Strategy
- **Distinctive marker**: All numbers start with specific actuator
- **Numeric encoding**: Binary or sequential encoding
- **Structure**: Consistent numeric pattern

**Proposed Encoding**:
- **Marker**: Actuator 5 (rightmost, if 6+ actuators)
- **Numbers**: Sequential pulses on actuators 0-4
  - 0: No pulses (just marker)
  - 1: Actuator 0
  - 2: Actuators 0, 1
  - 3: Actuators 0, 1, 2
  - ... (binary or sequential)

### Punctuation

#### Common Punctuation

**Space** (18% of text):
- Pattern: 300ms pause (no vibration)
- Rationale: Most common, clear boundary

**Period** (.):
- Actuator: All (simultaneous)
- Pattern: Single pulse, 200ms
- Rationale: Distinctive, word ending

**Comma** (,):
- Actuators: 0, 4 (simultaneous)
- Pattern: Single pulse, 150ms
- Rationale: Distinctive, shorter than period

**Question Mark** (?):
- Actuators: 0 → 4 → 0 (sequence)
- Pattern: Three pulses, 100ms each
- Rationale: Distinctive, memorable

**Exclamation** (!):
- Actuators: All (simultaneous)
- Pattern: Double pulse, 150ms each, 50ms gap
- Rationale: Distinctive, emphasis

## Pattern Generation Algorithm

### Character → Pattern Mapping

#### Lookup Table
- **Primary method**: Direct lookup table
- **Structure**: Character code → Pattern definition
- **Size**: ~100-200 entries (alphabet + numbers + punctuation)
- **Latency**: O(1) lookup, <1ms

#### Pattern Selection
1. **Input**: Character (Unicode/ASCII)
2. **Lookup**: Pattern definition from table
3. **Output**: Pattern structure ready for transmission
4. **Latency**: <1ms total

### Pattern Serialization

#### Binary Format (Proposed)
```
[Header: 1 byte] [Pattern Data: variable] [Checksum: 1 byte]

Header:
  Bit 0-3: Actuator count (0-15)
  Bit 4-7: Pattern type flags

Pattern Data:
  For each timing event:
    [Actuator ID: 1 byte]
    [Time offset: 2 bytes] (ms)
    [Duration: 1 byte] (ms, 0-255)
    [Intensity: 1 byte] (optional, 0-255)
```

#### Optimization
- **Compression**: If patterns repeat
- **Batching**: Multiple patterns in one message
- **Pre-computation**: Patterns ready to send

## Implementation Considerations

### Latency Optimization

#### Pattern Generation
- **Pre-computed**: All patterns in lookup table
- **No computation**: Direct retrieval
- **Latency**: <1ms

#### Pattern Transmission
- **Minimal overhead**: Efficient binary format
- **Direct serialization**: No complex encoding
- **Latency**: <0.5ms serialization

### Memory Requirements

#### Pattern Storage
- **Per pattern**: ~20-50 bytes (depends on complexity)
- **Total patterns**: ~100-200 patterns
- **Total storage**: ~2-10 KB
- **Feasible**: Fits in microcontroller memory

#### Runtime Memory
- **Pattern buffer**: ~100-200 bytes per pattern
- **Queue**: ~1-2 KB for pattern queue
- **Total**: ~2-5 KB runtime memory
- **Feasible**: Fits in microcontroller memory

### Learning Support

#### Pattern Visualization
- **Visual representation**: Show pattern during learning
- **Actuator diagram**: Visual actuator layout
- **Timing diagram**: Show pulse timing
- **Help**: Pattern explanation

#### Practice Mode
- **Guided learning**: Show pattern, then test
- **Repetition**: Practice specific patterns
- **Progress tracking**: Monitor learning progress
- **Adaptive difficulty**: Adjust to user level

## Future Enhancements

### Advanced Encoding

#### Word-Level Patterns
- **Common words**: "the", "be", "to" as single patterns
- **Compression**: Significant bandwidth reduction
- **Learning**: Additional pattern learning required
- **Trade-off**: Complexity vs. efficiency

#### Context-Aware Encoding
- **Language models**: Predict next character
- **Adaptive patterns**: Optimize based on context
- **Compression**: Further bandwidth reduction
- **Latency**: Processing overhead

#### User Customization
- **Personal patterns**: User-defined mappings
- **Optimization**: Adapt to user preferences
- **Learning**: User-specific optimizations
- **Flexibility**: High customization

## Recommendations

### Initial Implementation
1. **Direct character mapping**: Simple, learnable
2. **Spatial + temporal**: Multi-dimensional encoding
3. **Frequency optimization**: Shorter patterns for common characters
4. **Lookup table**: Fast pattern generation
5. **Binary format**: Efficient transmission

### Pattern Design
1. **Start simple**: Single actuator patterns for common characters
2. **Add complexity**: Multi-actuator for less common
3. **Consistent structure**: Similar patterns for related characters
4. **Clear boundaries**: Adequate spacing between patterns
5. **Learnable**: Designed for muscle memory

### Future Optimization
1. **Word-level patterns**: After basic system works
2. **Context-aware**: Advanced optimization
3. **User customization**: Personal preferences
4. **Adaptive compression**: Based on usage

## Related Documents

- [Symbol Mapping](symbol_mapping.md): Detailed character-to-pattern mappings
- [Protocol Specification](protocol_spec.md): Communication protocol
- [Linguistics Research](../research/linguistics.md): Character frequency analysis
- [Information Theory Research](../research/information_theory.md): Encoding efficiency



