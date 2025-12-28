# Knowledge Base

This document serves as a cross-referenced knowledge repository for AI-assisted development continuity. It contains key information, learnings, and relationships between concepts that inform development decisions.

## Structure

- **Key Concepts**: Core ideas and terminology
- **Research Findings**: Summaries of research with references
- **Technical Specifications**: Hardware and software specifications
- **Design Patterns**: Reusable design solutions
- **Lessons Learned**: Important insights from development
- **Cross-References**: Links between related documents

---

## Key Concepts

### Tactile Communication
- **Definition**: Communication through touch-based sensory feedback
- **Actuators**: Devices that produce tactile sensations (vibration motors, electrotactile, etc.)
- **Pattern Encoding**: Method of representing information as tactile patterns
- **Latency**: Time delay between input and tactile output
- **Target**: <10ms end-to-end latency

### System Components
- **Input Layer**: Keystroke capture and text message input
- **Translation Layer**: Character-to-pattern mapping and encoding
- **Communication Layer**: Wireless protocol and transmission
- **Hardware Control Layer**: Motor control and pattern execution

### Hardware Platform
- **Microcontroller**: ESP32 (dual-core 240MHz, BLE)
- **Actuators**: 8× LRA motors (Linear Resonant Actuator)
- **Drivers**: 8× DRV2605 haptic driver ICs
- **Communication**: Bluetooth Low Energy (BLE)
- **Power**: 2000mAh Li-ion battery

### Encoding System
- **Strategy**: Direct character mapping with frequency optimization
- **Dimensions**: Spatial (actuator location) + Temporal (timing)
- **Pattern Library**: Pre-computed patterns for all characters
- **Latency**: <1ms pattern generation (lookup table)

---

## Research Findings

### Linguistics & Language Interfaces
- **Character Frequency**: English text has predictable frequency distribution
- **Tactile Systems**: Braille and Morse code provide design insights
- **Encoding Efficiency**: Variable-length encoding can optimize common characters
- **Learning**: Spatial + temporal patterns are learnable with practice

**Key Documents**:
- [Linguistics Research](research/linguistics.md)
- [Language Interfaces Research](research/language_interfaces.md)
- [Information Theory Research](research/information_theory.md)

### HCI & Learning Theory
- **Motor Learning**: Three stages (cognitive, associative, autonomous)
- **Muscle Memory**: Repetition creates durable patterns
- **Cognitive Load**: Minimize extraneous load, manage intrinsic load
- **Pattern Recognition**: 100-300ms per pattern element optimal

**Key Documents**:
- [HCI Systems Research](research/hci_systems.md)
- [Learning Theory Research](research/learning_theory.md)
- [Haptic Feedback Research](research/haptic_feedback.md)

### Hardware & Actuators
- **LRA vs ERM**: LRA faster (10-20ms) but more expensive
- **DRV2605**: Optimal driver for LRA motors
- **ESP32**: Best cost/performance for BLE applications
- **Power Consumption**: ~200-300mA active, 6-10h battery life

**Key Documents**:
- [Actuator Technologies Research](research/actuator_technologies.md)
- [Latency Optimization Research](research/latency_optimization.md)
- [Hardware Comparison](hardware/comparison.md)

---

## Technical Specifications

### Hardware Specifications
- **Platform**: ESP32-WROOM-32
- **Actuators**: 8× LRA motors (3-10mm)
- **Drivers**: 8× DRV2605 (I2C)
- **Battery**: 2000mAh Li-ion
- **Communication**: BLE (7.5ms connection interval)

**Key Documents**:
- [Hardware Specifications](hardware/specs.md)
- [Hardware Architecture](hardware/architecture.md)
- [Bill of Materials](hardware/bom.md)

### Software Specifications
- **Encoding**: Python core library
- **Protocol**: Binary message format
- **Desktop**: Python application
- **Firmware**: C/C++ (ESP-IDF or Arduino)

**Key Documents**:
- [Encoding System Design](design/encoding_system.md)
- [Protocol Specification](design/protocol_spec.md)
- [API Reference](api/encoding.md)

### Performance Targets
- **Latency**: <10ms end-to-end (target)
- **Throughput**: 10+ patterns/second
- **Battery Life**: 6-10 hours active use
- **Range**: 10m+ BLE communication

---

## Design Patterns

### Pattern Encoding Pattern
- **Lookup Table**: O(1) character-to-pattern conversion
- **Pre-computation**: All patterns computed at initialization
- **Frequency Optimization**: Shorter patterns for common characters

### Protocol Pattern
- **Message-Based**: Structured message format
- **Serialization**: Binary format for efficiency
- **Error Handling**: Checksum validation

### Queue Pattern
- **FIFO Queue**: Pattern execution queue
- **Buffering**: Smooth pattern execution
- **Flow Control**: Queue full handling

### Hardware Abstraction Pattern
- **Platform Independence**: Abstract hardware interfaces
- **Driver Abstraction**: Motor driver abstraction
- **Communication Abstraction**: BLE abstraction

---

## Lessons Learned

### Design Phase
- **Start Simple**: Direct character mapping easier than compression
- **Frequency Matters**: Common characters should have simpler patterns
- **Spatial + Temporal**: Multi-dimensional encoding effective
- **Research Informs Design**: Linguistics and HCI research valuable

### Hardware Selection
- **Cost vs Performance**: ESP32 best balance
- **Response Time Critical**: LRA necessary for <10ms target
- **Power Matters**: Battery life important for wearables
- **Community Support**: Large community valuable

### Development Approach
- **Incremental**: Start simple, optimize later
- **Documentation**: Comprehensive docs aid development
- **Testing**: Unit tests important for reliability
- **Examples**: Examples help understanding

---

## Cross-References

### Documents
- [Decision Log](decisions.md): All major decisions
- [Research Findings](research/): All research documents
- [Hardware Specifications](hardware/): Hardware details
- [Architecture Documentation](architecture/): System design
- [API Documentation](api/): API reference

### Key Relationships

#### Hardware → Software
- ESP32 selection → Firmware development approach
- LRA motors → Pattern execution requirements
- DRV2605 drivers → I2C communication protocol

#### Research → Design
- Linguistics research → Encoding system design
- HCI research → Pattern design principles
- Learning theory → Learning support features

#### Design → Implementation
- Encoding design → Core library implementation
- Protocol design → Communication implementation
- Architecture → Component structure

### Decision Relationships

- [DEC-001] ESP32 → [DEC-004] BLE (ESP32 has BLE)
- [DEC-002] LRA → [DEC-003] DRV2605 (LRA needs driver)
- [DEC-005] Encoding → [DEC-006] Pattern Design (encoding informs patterns)
- [DEC-006] Patterns → [DEC-007] Actuators (patterns need actuators)

---

## Quick Reference

### Character Encoding
- **E, T, A, O, I**: Single actuator, 150ms pulse
- **N, S, H, R, D, L**: Two actuators, sequential
- **Others**: Three+ actuators, complex patterns

### Protocol Messages
- **Pattern**: Single character pattern
- **Pattern Batch**: Multiple patterns
- **Config**: Device configuration
- **Status**: Device status response

### Hardware Pins (ESP32)
- **GPIO 21**: I2C SDA (motor drivers)
- **GPIO 22**: I2C SCL (motor drivers)
- **GPIO 2**: Status LED (optional)
- **GPIO 35**: Battery monitoring (ADC)

---

## Related Documents

- [Decision Log](decisions.md): Decision records
- [Research Findings](research/): Research documents
- [Hardware Specifications](hardware/): Hardware details
- [Architecture Documentation](architecture/): System design
