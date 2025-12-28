# Decision Log

This document records all major decisions made during the Teletypathy project development, including rationale, alternatives considered, and trade-offs.

## Format

Each decision entry follows this structure:

- **Date**: YYYY-MM-DD
- **Decision**: Brief statement of the decision
- **Context**: Background and problem statement
- **Alternatives Considered**: List of options evaluated
- **Rationale**: Why this option was chosen
- **Trade-offs**: What was gained and lost
- **Related Decisions**: Links to other decisions
- **Status**: Proposed | Accepted | Rejected | Superseded

---

## Decisions

### [DEC-001] Hardware Platform: ESP32

**Date**: 2024  
**Status**: Accepted  
**Context**: Need to select microcontroller platform for wearable device with BLE support, low latency, and low cost.

**Alternatives Considered**:
1. ESP32 (selected)
2. Raspberry Pi Pico W
3. Arduino Nano 33 BLE
4. Raspberry Pi Zero 2 W

**Rationale**:
- Best cost/performance ratio (~$3-5)
- Native BLE support with good performance
- Can achieve <10ms latency with optimization
- Large community and excellent documentation
- Dual-core allows dedicated BLE core
- Sufficient GPIO for 8 actuators

**Trade-offs**:
- No integrated USB (requires USB-to-serial adapter)
- Moderate power consumption
- More complex than simpler MCUs

**Related Decisions**: [DEC-002], [DEC-003]

---

### [DEC-002] Actuator Type: LRA Motors

**Date**: 2024  
**Status**: Accepted  
**Context**: Need to select vibration motor type for tactile feedback with fast response time.

**Alternatives Considered**:
1. LRA (Linear Resonant Actuator) - selected
2. ERM (Eccentric Rotating Mass)
3. Piezoelectric actuators
4. Electrotactile stimulation

**Rationale**:
- Fast response time (10-20ms) supports <10ms latency goal
- Precise control with DRV2605 driver
- Lower power consumption than ERM
- Good balance of cost and performance
- Used in high-end devices (Apple Watch)

**Trade-offs**:
- Higher cost than ERM ($1-3 vs $0.50-2)
- Requires driver IC (DRV2605)
- Narrow frequency range (resonance)

**Related Decisions**: [DEC-001], [DEC-003]

---

### [DEC-003] Motor Driver: DRV2605

**Date**: 2024  
**Status**: Accepted  
**Context**: Need driver IC for LRA motor control. Each DRV2605 drives one LRA motor. Evaluated modern alternatives (DRV2624, DRV2625, DA7283, DA7282, CS40L25).

**Alternatives Evaluated**:
1. DRV2605 (selected) - Mature, well-supported
2. DRV2624/DRV2625 - Better power efficiency, less mature
3. DA7283 - Better latency, continuous tracking, less mature
4. DA7282 - Best power efficiency, less mature
5. CS40L25 - Ultra-low latency but overkill and expensive
6. PAM8016 - Lower cost but no resonance tracking (not viable)

**Modern Driver Findings**:
- **No multi-channel drivers**: All modern drivers still single-channel (need 8 drivers)
- **Similar cost**: Modern drivers cost similar ($1-2)
- **Improvements available**: Better power efficiency, lower latency, continuous tracking
- **Trade-offs**: Less mature, less community support than DRV2605

**Alternatives Considered**:
1. DRV2605 (selected) - 8 drivers for 8 motors
2. Direct PWM control - No drivers, but complex implementation
3. Multi-channel drivers - Not available commercially
4. Other single-channel drivers (DRV2604, TM6605) - Similar to DRV2605

**Rationale**:
- Designed specifically for LRA motors
- **Automatic resonance tracking** (critical for LRA performance):
  - Each of 8 motors has different resonance frequency (150-200 Hz range)
  - Resonance drifts with temperature (~0.1-0.5 Hz/°C) and aging
  - Without tracking: 10 Hz mismatch = 30-50% amplitude reduction
  - With tracking: Consistent vibration strength across all motors and conditions
  - Essential for reliable pattern recognition in Teletypathy
- Smart loop architecture (overdrive, braking for fast response)
- I2C interface (simple control)
- Built-in protection (overcurrent, overvoltage, thermal)
- Precise hardware timing (not software-dependent)
- Reduces CPU load (driver handles waveform generation)
- Faster development (2-3 weeks vs 4-8 weeks for direct PWM)
- Cost ($9-18 for 8 drivers) is small compared to development time savings

**Trade-offs**:
- Additional cost (~$1-2 per driver, $9-18 total for 8 motors)
- Requires I2C interface and address management
- One motor per driver (need 8 drivers for 8 motors)
- May need I2C multiplexer if more than 4 addresses needed

**Direct PWM Alternative Analysis**:
- **Cost savings**: $8-17 (no drivers needed)
- **Development time**: 4-8 weeks vs 2-3 weeks (extra 2-5 weeks)
- **Complexity**: High (AC generation, resonance tracking, calibration)
- **Performance**: May be inferior (no automatic resonance tracking)
- **Risk**: Higher risk of technical problems
- **Conclusion**: Cost savings don't justify development time and risk

**Modern Driver Alternatives**:
- Evaluated DRV2624, DRV2625, DA7283, DA7282, CS40L25
- **Finding**: All still single-channel (need 8 drivers), similar cost
- **Improvements**: Better power efficiency, lower latency in some cases
- **Trade-off**: Less mature, less community support
- **Decision**: Stick with DRV2605 for maturity and support
- **Future**: Consider DA7283 if latency critical, DRV2624/2625 if power critical

**Related Decisions**: [DEC-002], [DEC-009]

---

### [DEC-004] Communication Protocol: BLE

**Date**: 2024  
**Status**: Accepted  
**Context**: Need wireless communication protocol with low latency.

**Alternatives Considered**:
1. Bluetooth Low Energy (BLE) - selected
2. WiFi (UDP)
3. Custom 2.4GHz protocol

**Rationale**:
- Low latency achievable (~5-10ms with optimization)
- Low power consumption
- Standard protocol, widely supported
- Integrated in ESP32
- Good range (10m+)

**Trade-offs**:
- Latency may require optimization
- Connection management complexity
- May not achieve <10ms without optimization

**Related Decisions**: [DEC-001]

---

### [DEC-005] Encoding Strategy: Direct Character Mapping

**Date**: 2024  
**Status**: Accepted  
**Context**: Need encoding strategy for character-to-pattern conversion.

**Alternatives Considered**:
1. Direct character mapping (selected)
2. Frequency-based Huffman encoding
3. Dictionary-based encoding
4. Context-aware encoding

**Rationale**:
- Simple and learnable
- Low latency (lookup table, <1ms)
- Easy to implement and debug
- Can optimize later (frequency-based)
- Good for initial implementation

**Trade-offs**:
- Less efficient than compressed encoding
- No bandwidth optimization
- All characters treated similarly (initially)

**Related Decisions**: None

---

### [DEC-006] Pattern Design: Spatial + Temporal Encoding

**Date**: 2024  
**Status**: Accepted  
**Context**: Need to design tactile patterns for character encoding.

**Alternatives Considered**:
1. Spatial + temporal (selected)
2. Temporal only
3. Spatial only
4. Multi-dimensional (spatial + temporal + intensity)

**Rationale**:
- Spatial encoding intuitive (actuator location)
- Temporal encoding adds information density
- Good balance of simplicity and information
- Learnable with practice
- Supports frequency optimization

**Trade-offs**:
- More complex than single dimension
- Requires multiple actuators
- Learning curve for users

**Related Decisions**: [DEC-002]

---

### [DEC-007] Number of Actuators: 8

**Date**: 2024  
**Status**: Accepted  
**Context**: Need to determine optimal number of actuators.

**Alternatives Considered**:
1. 8 actuators (selected)
2. 4 actuators
3. 6 actuators
4. 10+ actuators

**Rationale**:
- Good spatial resolution
- Supports complex patterns
- Reasonable cost and complexity
- Good balance for encoding
- Manageable power consumption

**Trade-offs**:
- Higher cost than fewer actuators
- More complex control
- Higher power consumption
- Larger form factor

**Related Decisions**: [DEC-002], [DEC-006]

---

### [DEC-008] Programming Language: Python (Desktop), C/C++ (Firmware)

**Date**: 2024  
**Status**: Accepted  
**Context**: Need to select programming languages for desktop and firmware.

**Alternatives Considered**:
1. Python (desktop) + C/C++ (firmware) - selected
2. JavaScript/TypeScript (desktop)
3. Rust (both)
4. C/C++ (both)

**Rationale**:
- Python: Easy development, good libraries, cross-platform
- C/C++: Required for ESP32, performance, standard
- Good tooling and community support
- Balance of development speed and performance

**Trade-offs**:
- Python: Slower than compiled languages
- C/C++: More complex development
- Language barrier between desktop and firmware

**Related Decisions**: None

---

### [DEC-009] Modern Driver Alternatives Considered

**Date**: 2024  
**Status**: Evaluated, Not Selected  
**Context**: Evaluation of modern LRA driver alternatives to DRV2605.

**Alternatives Considered**:
1. **DA7283** (Renesas): Low-latency, continuous tracking, wide bandwidth (up to 300 Hz)
2. **DRV2624/DRV2625** (TI): Ultra-low power, internal memory, resonance reporting
3. **DA7282** (Renesas): Ultra-low power, continuous tracking
4. **CS40L25** (Cirrus Logic): Ultra-low latency, integrated DSP (overkill, expensive)
5. **PAM8016** (Diodes): Lower cost but no resonance tracking (not viable)

**Decision**: Stick with DRV2605

**Rationale**:
- **Maturity**: DRV2605 most mature, proven reliability
- **Support**: Extensive documentation and community examples
- **Performance**: Good enough for application requirements
- **Cost**: Similar to modern alternatives ($1-2)
- **Risk**: Lowest risk option
- **No multi-channel**: All modern drivers still single-channel (no advantage)
- **No cost advantage**: Modern drivers cost similar

**Modern Driver Findings**:
- **No multi-channel drivers**: All modern drivers still single-channel (need 8 drivers)
- **Improvements available**: Better power efficiency (DA7282, DRV2624/2625), lower latency (DA7283), continuous tracking (DA7283/DA7282)
- **Trade-offs**: Less mature, less community support than DRV2605

**Future Consideration**:
- **DA7283**: Consider if latency becomes critical (<10ms hard requirement)
- **DRV2624/DRV2625**: Consider if power consumption becomes critical
- **DA7282**: Consider if ultra-low power essential

**Related Decisions**: [DEC-003]

---

## Decision Template

### [DEC-XXX] Decision Title

**Date**: YYYY-MM-DD  
**Status**: Proposed  
**Context**:  
**Alternatives Considered**:  
**Rationale**:  
**Trade-offs**:  
**Related Decisions**:  

---

## Related Documents

- [Hardware Comparison](../hardware/comparison.md): Platform evaluation
- [Encoding System Design](../design/encoding_system.md): Encoding decisions
- [Protocol Specification](../design/protocol_spec.md): Protocol decisions
