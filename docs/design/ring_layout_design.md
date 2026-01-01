# Ring Layout Design: 8 Actuators in Circular Configuration

## Overview

This document explores a **ring/bracelet layout** with 8 actuators arranged in circular configurations around the arm, designed to improve spatial discrimination for single-byte encoding and passive learning.

## Design Concept

### Current Design: Linear Array

```
Linear Array (Current):
[0] [1] [2] [3] [4] [5] [6] [7]
─────────────────────────────────
Forearm (single line)
```

**Limitations:**
- All actuators in one plane
- Difficult to distinguish 8 simultaneous activations
- Limited spatial separation

### Proposed Design: Ring Configuration

```
Ring Layout (Proposed):
     ┌───┐
    ╱  4  ╲
   │   5   │  Upper Ring
    ╲  6  ╱
     └───┘
       │
     ┌───┐
    ╱  0  ╲
   │   1   │  Lower Ring
    ╲  2  ╱
     └───┘
       │
     Forearm
```

## Ring Layout Options

### Option 1: Two Rings (4+4 Actuators)

**Configuration:**
- **Upper Ring**: 4 actuators (0-3) at wrist/forearm junction
- **Lower Ring**: 4 actuators (4-7) ~5-10cm below upper ring
- **Total**: 8 actuators

**Actuator Distribution:**
```
Upper Ring (wrist):
    3
    │
2───┼───1
    │
    0

Lower Ring (forearm):
    7
    │
6───┼───5
    │
    4
```

**Benefits:**
- ✅ **Clear spatial separation**: Two distinct rings
- ✅ **Easier discrimination**: Max 4 actuators per ring
- ✅ **Natural wear**: Bracelet/armband form factor
- ✅ **3D spatial encoding**: Vertical + angular position

**Single-Byte Encoding:**
- Lower 4 bits → Lower ring (actuators 0-3)
- Upper 4 bits → Upper ring (actuators 4-7)
- **Max simultaneous per ring**: 4 actuators (within limits)

### Option 2: Single Ring (8 Actuators)

**Configuration:**
- **Single Ring**: 8 actuators evenly spaced around arm circumference
- **Spacing**: 45° apart (360° / 8 = 45°)

**Actuator Distribution:**
```
    7   0
  6      1
5        2
  4      3
```

**Benefits:**
- ✅ **Uniform spacing**: Equal angular separation
- ✅ **Circular encoding**: Angular position encodes information
- ✅ **Simple design**: Single ring/bracelet

**Single-Byte Encoding:**
- Each bit → One actuator position
- **Angular pattern**: Bit pattern creates spatial shape
- **Max simultaneous**: 8 actuators (challenge remains)

### Option 3: Three Rings (3+3+2 Actuators)

**Configuration:**
- **Upper Ring**: 3 actuators (0-2)
- **Middle Ring**: 3 actuators (3-5)
- **Lower Ring**: 2 actuators (6-7)
- **Total**: 8 actuators

**Benefits:**
- ✅ **Maximum separation**: Three distinct levels
- ✅ **Very easy discrimination**: Max 3 actuators per ring
- ✅ **Flexible encoding**: Can use ring position as dimension

## Recommended: Two Rings (4+4)

### Design Rationale

**Why Two Rings with 4 Actuators Each:**

1. **Perception Limits**: 4 actuators per ring is within reliable discrimination limits
2. **Single-Byte Encoding**: Natural split (lower 4 bits + upper 4 bits)
3. **Spatial Separation**: Clear vertical separation between rings
4. **Wearability**: Natural bracelet/armband form factor
5. **Manufacturing**: Easier than single ring with 8 actuators

### Physical Design

**Ring Specifications:**
- **Upper Ring**: Wrist/forearm junction
- **Lower Ring**: 5-10cm below upper ring
- **Ring Diameter**: Adjustable (fits different arm sizes)
- **Actuator Spacing**: 90° apart (4 actuators per ring)
- **Ring Width**: ~15-20mm (comfortable wear)

**Actuator Placement:**
```
Upper Ring (Actuators 0-3):
  Position 0: Top (12 o'clock)
  Position 1: Right (3 o'clock)
  Position 2: Bottom (6 o'clock)
  Position 3: Left (9 o'clock)

Lower Ring (Actuators 4-7):
  Position 4: Top (12 o'clock)
  Position 5: Right (3 o'clock)
  Position 6: Bottom (6 o'clock)
  Position 7: Left (9 o'clock)
```

## Single-Byte Encoding with Ring Layout

### Encoding Strategy

**Bit-to-Actuator Mapping:**
```
Lower 4 bits (0-3) → Lower Ring (Actuators 0-3)
Upper 4 bits (4-7) → Upper Ring (Actuators 4-7)
```

**Example: 'Y' = 89 = 0b01011001**
```
Lower Ring (bits 0-3 = 1001):
  Actuator 0: ON  (bit 0 = 1, top)
  Actuator 1: OFF (bit 1 = 0, right)
  Actuator 2: OFF (bit 2 = 0, bottom)
  Actuator 3: ON  (bit 3 = 1, left)

Upper Ring (bits 4-7 = 0101):
  Actuator 4: ON  (bit 4 = 1, top)
  Actuator 5: OFF (bit 5 = 0, right)
  Actuator 6: ON  (bit 6 = 1, bottom)
  Actuator 7: OFF (bit 7 = 0, left)

Pattern: Lower ring (top+left) + Upper ring (top+bottom)
Duration: 80ms (all simultaneous)
```

### Perception Advantages

**Ring Layout Benefits:**

1. **Vertical Separation**: Two distinct rings = easier to distinguish
2. **Angular Position**: 4 positions per ring = clear spatial encoding
3. **3D Spatial Cues**: Vertical + angular = more information
4. **Reduced Confusion**: Max 4 actuators per ring (within limits)

**Comparison:**

| Layout | Max Simultaneous | Discrimination |
|--------|-----------------|----------------|
| **Linear (8)** | 8 actuators | Difficult |
| **Ring (4+4)** | 4 per ring | Easier |
| **Ring (3+3+2)** | 3 per ring | Easiest |

## Pattern Encoding Strategies

### Strategy 1: Ring-Based Encoding

**Use ring position as encoding dimension:**

```python
def encode_ring_based(char: str) -> Pattern:
    """Encode using ring position + angular position."""
    byte_value = ord(char)
    
    # Lower 4 bits → Lower ring
    lower_bits = byte_value & 0b1111
    # Upper 4 bits → Upper ring
    upper_bits = (byte_value >> 4) & 0b1111
    
    events = []
    
    # Lower ring (actuators 0-3)
    for i in range(4):
        if (lower_bits >> i) & 1:
            events.append(ActuatorEvent(
                actuator_id=i,
                time_offset_ms=0,
                duration_ms=80,
                intensity=200
            ))
    
    # Upper ring (actuators 4-7)
    for i in range(4):
        if (upper_bits >> i) & 1:
            events.append(ActuatorEvent(
                actuator_id=i + 4,
                time_offset_ms=0,
                duration_ms=80,
                intensity=200
            ))
    
    return Pattern(events)
```

**Benefits:**
- Natural bit-to-ring mapping
- Max 4 actuators per ring
- Clear spatial separation

### Strategy 2: Angular Pattern Encoding

**Use angular position to encode information:**

```python
def encode_angular(char: str) -> Pattern:
    """Encode using angular position around ring."""
    byte_value = ord(char)
    
    # Each bit → angular position
    # 8 bits = 8 positions around rings
    
    events = []
    for i in range(8):
        if (byte_value >> i) & 1:
            # Map bit to ring + angular position
            ring = i // 4  # 0 = lower, 1 = upper
            angle = i % 4  # 0-3 (top, right, bottom, left)
            actuator_id = ring * 4 + angle
            
            events.append(ActuatorEvent(
                actuator_id=actuator_id,
                time_offset_ms=0,
                duration_ms=80,
                intensity=200
            ))
    
    return Pattern(events)
```

### Strategy 3: Temporal Ring Activation

**Activate rings sequentially for better discrimination:**

```python
def encode_temporal_ring(char: str) -> Pattern:
    """Activate lower ring, then upper ring."""
    byte_value = ord(char)
    events = []
    
    # Lower ring (bits 0-3) at t=0ms
    lower_bits = byte_value & 0b1111
    for i in range(4):
        if (lower_bits >> i) & 1:
            events.append(ActuatorEvent(
                actuator_id=i,
                time_offset_ms=0,
                duration_ms=60,
                intensity=200
            ))
    
    # Upper ring (bits 4-7) at t=20ms
    upper_bits = (byte_value >> 4) & 0b1111
    for i in range(4):
        if (upper_bits >> i) & 1:
            events.append(ActuatorEvent(
                actuator_id=i + 4,
                time_offset_ms=20,
                duration_ms=60,
                intensity=200
            ))
    
    return Pattern(events)
```

**Duration**: 80ms total (60ms pulse + 20ms gap)
**Max simultaneous**: 4 actuators (one ring at a time)

## Hardware Design

### Bracelet/Armband Form Factor

**Design:**
- **Two separate rings/bracelets** connected by flexible band
- **Or**: Single armband with two distinct actuator rings
- **Adjustable**: Fits different arm sizes
- **Comfortable**: Lightweight, breathable materials

**Materials:**
- **Band**: Flexible fabric or silicone
- **Rings**: Rigid sections for actuator mounting
- **Actuators**: LRA motors (3-10mm diameter)
- **Electronics**: ESP32 + DRV2605 drivers in central unit

### Actuator Mounting

**Ring Configuration:**
```
Upper Ring:
  ┌─────────┐
  │    [3]   │  Top
  │         │
[2]  ESP32  [1]  Right/Left
  │         │
  │    [0]   │  Bottom
  └─────────┘

Lower Ring:
  ┌─────────┐
  │    [7]   │  Top
  │         │
[6]  Power  [5]  Right/Left
  │         │
  │    [4]   │  Bottom
  └─────────┘
```

**Spacing:**
- **Within ring**: 90° apart (4 actuators)
- **Between rings**: 5-10cm vertical separation
- **Actuator size**: 3-10mm diameter LRA motors

## Perception Research

### Why Ring Layout Helps

**3D Spatial Encoding:**
- **Vertical dimension**: Ring position (upper vs. lower)
- **Angular dimension**: Position around ring (0-3)
- **Combined**: More spatial information than linear array

**Perception Benefits:**
- **Ring separation**: Easier to distinguish which ring is active
- **Angular position**: Clear spatial cues (top, right, bottom, left)
- **Reduced confusion**: Max 4 actuators per ring (within limits)

### Research Support

**Spatial Tactile Perception:**
- **2D arrays**: Better than 1D linear arrays
- **3D spatial cues**: Vertical + angular improves discrimination
- **Ring configurations**: Used in haptic research for better perception

## Comparison: Linear vs. Ring Layout

### Linear Array (Current)

**Pros:**
- ✅ Simple design
- ✅ Easy to manufacture
- ✅ Familiar layout

**Cons:**
- ❌ All actuators in one plane
- ❌ Difficult to distinguish 8 simultaneous
- ❌ Limited spatial encoding

### Ring Layout (Proposed)

**Pros:**
- ✅ **Better spatial discrimination**: 3D spatial cues
- ✅ **Natural for single-byte**: 4+4 split
- ✅ **Bracelet form factor**: More natural wear
- ✅ **Reduced confusion**: Max 4 per ring
- ✅ **Angular encoding**: Additional dimension

**Cons:**
- ⚠️ More complex manufacturing
- ⚠️ Requires adjustable sizing
- ⚠️ May need different enclosure design

## Implementation Impact

### Pattern Encoding Changes

**Current (Linear):**
```python
# Actuators 0-7 in single line
Actuator 0: Leftmost
Actuator 7: Rightmost
```

**Ring Layout:**
```python
# Actuators 0-3: Lower ring (angular positions)
# Actuators 4-7: Upper ring (angular positions)
Actuator 0: Lower ring, top (12 o'clock)
Actuator 1: Lower ring, right (3 o'clock)
Actuator 2: Lower ring, bottom (6 o'clock)
Actuator 3: Lower ring, left (9 o'clock)
Actuator 4: Upper ring, top (12 o'clock)
...
```

### Single-Byte Encoding Benefits

**With Ring Layout:**
- **Lower 4 bits** → Lower ring (max 4 simultaneous)
- **Upper 4 bits** → Upper ring (max 4 simultaneous)
- **Total**: 8 actuators, but split into two perceptible groups
- **Duration**: 80ms (all simultaneous, or 80ms with micro-temporal)

**Result**: Better discrimination while maintaining speed!

## Recommendations

### Design Choice: Two Rings (4+4)

**Rationale:**
1. **Perception**: Max 4 per ring (within limits)
2. **Encoding**: Natural 4+4 bit split
3. **Wearability**: Natural bracelet form factor
4. **Manufacturing**: Reasonable complexity

### Encoding Strategy: Ring-Based Single-Byte

**Implementation:**
1. **Lower 4 bits** → Lower ring (actuators 0-3)
2. **Upper 4 bits** → Upper ring (actuators 4-7)
3. **Duration**: 80ms (all simultaneous)
4. **Max simultaneous**: 4 actuators (one ring)

**Alternative**: Micro-temporal (lower ring → upper ring, 80ms total)

### Next Steps

1. **Update hardware specifications** for ring layout
2. **Modify pattern encoder** for ring-based mapping
3. **Create ring layout visualization** tools
4. **Conduct perception studies** comparing linear vs. ring
5. **Prototype ring/bracelet design**

## Conclusion

**Ring layout is a game-changer for single-byte encoding!**

**Key Benefits:**
- ✅ **Better discrimination**: 3D spatial cues (vertical + angular)
- ✅ **Natural for 8 actuators**: Two rings of 4
- ✅ **Single-byte friendly**: Natural 4+4 bit split
- ✅ **Bracelet form factor**: More natural wear
- ✅ **Reduced confusion**: Max 4 actuators per ring

**This design enables:**
- Single-byte encoding with better perception
- 80ms patterns (fast, non-intrusive)
- Passive learning through constant exposure
- Natural bracelet/armband form factor

The ring layout addresses the perception limitations while maintaining the speed benefits of single-byte encoding!

