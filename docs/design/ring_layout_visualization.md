# Ring Layout Visualization: Single-Byte Encoding

## Ring Layout Design

### Two Rings Configuration

```
        Upper Ring (Wrist)
        ┌─────────┐
        │   4     │  Top (12 o'clock)
        │         │
    7   │  ESP32  │   5
  Left  │         │  Right
  (9o') │         │  (3o')
        │   6     │  Bottom (6 o'clock)
        └─────────┘
            │
        5-10cm
            │
        Lower Ring (Forearm)
        ┌─────────┐
        │   0     │  Top (12 o'clock)
        │         │
    3   │  Power  │   1
  Left  │         │  Right
  (9o') │         │  (3o')
        │   2     │  Bottom (6 o'clock)
        └─────────┘
```

## Single-Byte Encoding with Ring Layout

### Bit Mapping

**Lower 4 bits (0-3) → Lower Ring (Actuators 0-3)**
- Bit 0 → Actuator 0 (Top)
- Bit 1 → Actuator 1 (Right)
- Bit 2 → Actuator 2 (Bottom)
- Bit 3 → Actuator 3 (Left)

**Upper 4 bits (4-7) → Upper Ring (Actuators 4-7)**
- Bit 4 → Actuator 4 (Top)
- Bit 5 → Actuator 5 (Right)
- Bit 6 → Actuator 6 (Bottom)
- Bit 7 → Actuator 7 (Left)

### Example: Character 'Y' = 89 = 0b01111001

**Lower Ring (bits 0-3 = 1001):**
```
        ┌─────────┐
        │   0     │  OFF (bit 0 = 1, but... wait, let me check)
        │         │
    3   │         │   1
  ON    │         │  OFF
        │   2     │
        └─────────┘
```

Actually, let me recalculate:
- Lower bits: 1001 (binary) = bits 0,3 set
- Upper bits: 0111 (binary) = bits 4,5,6 set

**Visualization:**
```
Upper Ring:        Lower Ring:
    4 (ON)             0 (ON)
    │                  │
7   5 (ON)         3   1 (OFF)
│   │              │   │
│   6 (ON)         │   2 (OFF)
└───┘              └───┘
```

## Perception Advantages

### Why Ring Layout Helps

**3D Spatial Encoding:**
- **Vertical dimension**: Ring position (upper vs. lower)
- **Angular dimension**: Position around ring (0-3, 90° apart)
- **Combined**: More spatial information than linear

**Discrimination:**
- **Ring separation**: Easy to tell which ring is active
- **Angular position**: Clear spatial cues (top, right, bottom, left)
- **Max simultaneous**: 4 actuators per ring (within perception limits)

### Comparison

**Linear Array (8 actuators in line):**
- All in one plane
- Hard to distinguish 8 simultaneous
- Only horizontal position

**Ring Layout (4+4 in two rings):**
- 3D spatial arrangement
- Max 4 simultaneous per ring
- Vertical + angular position

## Pattern Examples

### Character 'E' = 69 = 0b01000101

**Lower Ring (0101):**
- Actuator 0: ON (top)
- Actuator 1: OFF (right)
- Actuator 2: ON (bottom)
- Actuator 3: OFF (left)
- **Pattern**: Top + Bottom (vertical line)

**Upper Ring (0100):**
- Actuator 4: OFF (top)
- Actuator 5: ON (right)
- Actuator 6: OFF (bottom)
- Actuator 7: OFF (left)
- **Pattern**: Right only

**User feels**: Lower ring (top+bottom), Upper ring (right)

### Character 'T' = 84 = 0b01010100

**Lower Ring (0100):**
- Actuator 2: ON (bottom only)

**Upper Ring (0101):**
- Actuator 4: ON (top)
- Actuator 5: OFF (right)
- Actuator 6: ON (bottom)
- Actuator 7: OFF (left)
- **Pattern**: Top + Bottom (vertical line)

**User feels**: Lower ring (bottom), Upper ring (top+bottom)

## Encoding Benefits

### Single-Byte with Ring Layout

**Advantages:**
- ✅ **Fast**: 80ms duration (all simultaneous)
- ✅ **Perceptible**: Max 4 actuators per ring
- ✅ **Natural mapping**: 4+4 bit split matches ring layout
- ✅ **3D spatial cues**: Vertical + angular information
- ✅ **Better discrimination**: Ring position provides strong cue

**Result**: Enables single-byte encoding with acceptable perception!

## Implementation

The `SingleByteEncoder` now supports ring-based encoding:

```python
encoder = SingleByteEncoder(mode='ring_based', layout='ring')
pattern = encoder.encode_character('y')
# Lower ring: actuators 0,3
# Upper ring: actuators 4,5,6
# Duration: 80ms
```

This design enables:
- **Single-byte encoding** (fast, 80ms)
- **Better perception** (ring layout)
- **Passive learning** (non-intrusive patterns)
- **Natural form factor** (bracelet/armband)

