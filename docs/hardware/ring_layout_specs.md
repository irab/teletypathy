# Ring Layout Hardware Specifications

## Overview

Hardware specifications for ring/bracelet layout with 8 actuators arranged in two circular rings around the arm.

## Design: Two Rings (4+4 Actuators)

### Configuration

**Upper Ring (Wrist):**
- **Location**: Wrist/forearm junction
- **Actuators**: 4 (IDs 0-3)
- **Spacing**: 90° apart (top, right, bottom, left)
- **Diameter**: Adjustable (fits arm circumference)

**Lower Ring (Forearm):**
- **Location**: 5-10cm below upper ring
- **Actuators**: 4 (IDs 4-7)
- **Spacing**: 90° apart (top, right, bottom, left)
- **Diameter**: Adjustable (matches upper ring)

**Total**: 8 actuators

## Physical Specifications

### Ring Dimensions

**Ring Width:**
- **Actuator section**: 15-20mm (accommodates LRA motor)
- **Band section**: 10-15mm (flexible, comfortable)
- **Total width**: 25-35mm per ring

**Ring Diameter:**
- **Adjustable**: 50-80mm (fits different arm sizes)
- **Typical**: ~65mm (average adult forearm)
- **Adjustment mechanism**: Velcro, elastic, or clasp

**Ring Separation:**
- **Vertical distance**: 5-10cm between rings
- **Optimal**: 7-8cm (clear spatial separation)

### Actuator Placement

**Angular Positions (per ring):**
```
    0 (Top - 12 o'clock)
    │
3───┼───1 (Right - 3 o'clock)
(Left│
9 o')│
    │
    2 (Bottom - 6 o'clock)
```

**Upper Ring (Actuators 0-3):**
- Actuator 0: Top (12 o'clock)
- Actuator 1: Right (3 o'clock)
- Actuator 2: Bottom (6 o'clock)
- Actuator 3: Left (9 o'clock)

**Lower Ring (Actuators 4-7):**
- Actuator 4: Top (12 o'clock)
- Actuator 5: Right (3 o'clock)
- Actuator 6: Bottom (6 o'clock)
- Actuator 7: Left (9 o'clock)

## Mechanical Design

### Form Factor Options

#### Option 1: Two Separate Bracelets

**Design:**
- Two independent bracelets connected by flexible band
- Each bracelet contains 4 actuators
- Central electronics unit between rings

**Pros:**
- Modular design
- Easy to adjust individually
- Can be worn separately

**Cons:**
- More complex assembly
- Requires connection between rings

#### Option 2: Single Armband with Two Rings

**Design:**
- Single continuous armband
- Two rigid sections (rings) with actuators
- Flexible band connecting rings

**Pros:**
- Simpler assembly
- Single unit
- Better integration

**Cons:**
- Less flexible adjustment
- More complex manufacturing

#### Option 3: Modular Ring System

**Design:**
- Modular rings that connect together
- Each ring contains 4 actuators
- Flexible connectors between rings

**Pros:**
- Highly adjustable
- Modular and repairable
- Flexible configuration

**Cons:**
- Most complex design
- More connection points

### Recommended: Option 2 (Single Armband)

**Rationale:**
- Simpler manufacturing
- Better user experience (single unit)
- Good balance of flexibility and simplicity

## Electronics Layout

### Component Placement

**Central Electronics Unit:**
- **Location**: Between rings or on one ring
- **Components**:
  - ESP32 microcontroller
  - 8× DRV2605 drivers (or shared bus)
  - Power management
  - Battery
  - BLE antenna

**Actuator Connections:**
- **Wiring**: Flexible wires from central unit to actuators
- **Routing**: Along band, protected from wear
- **Connectors**: Secure, reliable connections

### I2C Bus Design

**Option 1: Shared I2C Bus**
- Single I2C bus connects all 8 DRV2605 drivers
- Different I2C addresses for each driver
- Wires run along band to actuators

**Option 2: Ring-Based Buses**
- Separate I2C bus per ring (4 drivers each)
- Reduces wire count
- May need I2C multiplexer

**Recommended**: Shared I2C bus (simpler, proven design)

## Actuator Specifications

### LRA Motor Requirements

**Size:**
- **Diameter**: 3-10mm (compact for ring mounting)
- **Height**: 2-5mm (low profile)
- **Weight**: <1g per motor

**Performance:**
- **Resonance**: ~175Hz (typical LRA)
- **Response**: 10-20ms
- **Power**: 30-80mA per motor

**Mounting:**
- **Ring integration**: Embedded in ring material
- **Skin contact**: Direct contact with skin
- **Protection**: Water-resistant enclosure

## Power System

### Battery Placement

**Options:**
1. **Central unit**: Battery in electronics unit between rings
2. **Distributed**: Small batteries in each ring
3. **External**: Battery pack on band

**Recommended**: Central unit (easier charging, better weight distribution)

### Power Distribution

**Voltage Rails:**
- **3.3V**: ESP32, DRV2605 drivers
- **Motor power**: Via DRV2605 drivers
- **Distribution**: Along band to actuators

## Comfort and Wearability

### Materials

**Band:**
- **Flexible**: Silicone, fabric, or flexible plastic
- **Breathable**: Allows air circulation
- **Skin-friendly**: Hypoallergenic materials

**Rings:**
- **Rigid sections**: For actuator mounting
- **Smooth edges**: No sharp points
- **Lightweight**: Minimize weight

### Adjustability

**Size Adjustment:**
- **Velcro**: Simple, adjustable
- **Elastic**: Stretchy, one-size-fits-many
- **Clasp**: Secure, adjustable sizing
- **Modular**: Add/remove links

**Comfort:**
- **Padding**: Soft material against skin
- **Ventilation**: Gaps for air flow
- **Weight distribution**: Balanced weight

## Manufacturing Considerations

### 3D Printing

**Prototype:**
- **Rings**: 3D printed rigid sections
- **Band**: Flexible TPU material
- **Actuator mounts**: Integrated in ring design

**Production:**
- **Injection molding**: For mass production
- **Overmolding**: Combine rigid and flexible materials

### Assembly

**Steps:**
1. Mount actuators in ring sections
2. Route wires along band
3. Connect to central electronics unit
4. Secure connections and test
5. Add padding/comfort materials

## Comparison: Linear vs. Ring Layout

### Linear Array (Current)

**Dimensions:**
- Length: ~280-400mm (8 actuators × 40-50mm spacing)
- Width: ~20-30mm
- Single plane

**Actuator Spacing:**
- 40-50mm between actuators
- Linear arrangement

### Ring Layout (Proposed)

**Dimensions:**
- Ring diameter: ~50-80mm (adjustable)
- Ring width: ~25-35mm
- Ring separation: 5-10cm vertical
- 3D spatial arrangement

**Actuator Spacing:**
- 90° angular separation (within ring)
- 5-10cm vertical separation (between rings)
- Circular arrangement

## Perception Advantages

### Spatial Discrimination

**Linear Array:**
- **1D encoding**: Only horizontal position
- **8 simultaneous**: Difficult to distinguish
- **Confusion**: Similar patterns feel identical

**Ring Layout:**
- **3D encoding**: Vertical (ring) + Angular (position)
- **4 per ring**: Easier to distinguish
- **Clear separation**: Ring position provides strong cue

### Single-Byte Encoding Benefits

**With Ring Layout:**
- Lower 4 bits → Lower ring (max 4 simultaneous)
- Upper 4 bits → Upper ring (max 4 simultaneous)
- **Result**: Better discrimination while maintaining speed

## Testing and Validation

### Perception Studies Needed

1. **Discrimination test**: Compare linear vs. ring layout
2. **Error rate measurement**: Single-byte encoding accuracy
3. **Comfort study**: Long-term wear comfort
4. **Passive learning**: Measure improvement over time

### Prototype Requirements

1. **Functional prototype**: Two rings with 4 actuators each
2. **Electronics integration**: ESP32 + drivers
3. **Comfort testing**: Wearability and comfort
4. **Performance testing**: Pattern discrimination

## Implementation Roadmap

### Phase 1: Design and Prototype
1. Design ring/bracelet form factor
2. 3D print prototype rings
3. Mount actuators and test
4. Validate spatial discrimination

### Phase 2: Electronics Integration
1. Integrate ESP32 and drivers
2. Route wiring along band
3. Test I2C communication
4. Validate pattern execution

### Phase 3: User Testing
1. Perception studies (linear vs. ring)
2. Single-byte encoding accuracy
3. Comfort and wearability
4. Passive learning study

## Conclusion

**Ring layout enables single-byte encoding with better perception!**

**Key Advantages:**
- ✅ **3D spatial encoding**: Vertical + angular dimensions
- ✅ **Better discrimination**: Max 4 actuators per ring
- ✅ **Natural form factor**: Bracelet/armband design
- ✅ **Single-byte friendly**: Natural 4+4 bit split
- ✅ **Passive learning**: Fast, non-intrusive patterns

This design addresses perception limitations while maintaining the speed benefits needed for passive learning!

