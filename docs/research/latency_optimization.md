# Latency Optimization Research

## Overview

Strategies for minimizing end-to-end latency in tactile communication systems, targeting <10ms total latency.

## Latency Components

### System Latency Breakdown

#### Target: <10ms End-to-End

**Component Breakdown (Target)**:
1. **Input capture**: <1ms (keystroke detection)
2. **Pattern generation**: <1ms (character → pattern mapping)
3. **Protocol serialization**: <0.5ms (message encoding)
4. **Wireless transmission**: <5ms (BLE/WiFi)
5. **Protocol deserialization**: <0.5ms (message decoding)
6. **Pattern execution**: <2ms (motor control)
7. **Motor response**: <1ms (LRA startup)

**Total Target**: ~10ms

### Current Technology Limits

#### Wireless Communication Latency

**Bluetooth Low Energy (BLE)**:
- **Connection interval**: 7.5-4000ms (configurable)
- **Minimum latency**: ~7.5ms (with 7.5ms interval)
- **Typical latency**: 20-50ms (default settings)
- **Optimized latency**: ~5-10ms (aggressive settings)
- **Trade-off**: Lower latency = higher power consumption

**WiFi**:
- **Theoretical latency**: <1ms
- **Practical latency**: 5-20ms (depends on network)
- **Advantages**: Lower latency potential
- **Disadvantages**: Higher power consumption

**Custom Protocols**:
- **Enhanced ShockBurst (ESB)**: ~505μs device-to-device
- **Custom 2.4GHz**: <1ms possible
- **Advantages**: Very low latency
- **Disadvantages**: Requires custom hardware/software

#### Actuator Response Time

**LRA Motors**:
- **Response time**: 10-20ms typical
- **Optimized**: ~5-10ms (with driver optimization)
- **Startup delay**: ~5ms to begin vibration
- **Full amplitude**: ~10-20ms total

**ERM Motors**:
- **Response time**: 50-100ms typical
- **Startup delay**: ~30-50ms
- **Full amplitude**: ~50-100ms total
- **Not suitable**: For <10ms target

## Optimization Strategies

### Input Layer Optimization

#### Keystroke Capture
- **Polling rate**: High frequency (1000Hz+)
- **Interrupt-based**: Immediate on keypress
- **Filtering**: Minimal processing
- **Latency**: <1ms achievable

#### Text Processing
- **Direct mapping**: Character → pattern (no processing)
- **Lookup table**: O(1) pattern retrieval
- **Pre-computed**: Patterns ready to send
- **Latency**: <1ms achievable

### Communication Layer Optimization

#### Protocol Design

**Minimal Overhead**:
- **Header**: 2-4 bytes (address, type, length)
- **Payload**: Pattern data only
- **Checksum**: 1-2 bytes (minimal)
- **Total overhead**: <10 bytes per message

**Message Format (Proposed)**:
```
[Header: 2 bytes] [Pattern Data: variable] [Checksum: 1 byte]
```

**Optimization**:
- No acknowledgment (for lowest latency)
- Or: Fast acknowledgment (minimal overhead)
- Batch multiple patterns if possible
- Compress patterns if beneficial

#### Wireless Protocol Selection

**BLE Optimization**:
- **Connection interval**: 7.5ms (minimum)
- **Slave latency**: 0 (no skipping)
- **Timeout**: Minimal
- **MTU**: Maximum (reduce overhead)
- **Latency**: ~5-10ms achievable

**WiFi Optimization**:
- **UDP**: Lower latency than TCP
- **Local network**: Avoid internet routing
- **QoS**: High priority
- **Latency**: ~2-5ms achievable

**Custom Protocol**:
- **2.4GHz custom**: <1ms possible
- **Requires**: Custom hardware/software
- **Complexity**: Higher development effort
- **Latency**: Best option if feasible

### Hardware Layer Optimization

#### Motor Control

**Pre-computed Patterns**:
- Store patterns in firmware
- Direct execution (no computation)
- Hardware timers for precise timing
- **Latency**: <1ms pattern start

**Driver Optimization**:
- DRV2605 library effects (pre-optimized)
- Or: Custom drive signals (optimized)
- Immediate start (no delay)
- **Latency**: <1ms to begin vibration

#### GPIO and Timing

**Hardware Timers**:
- Precise timing (microsecond accuracy)
- No software delay overhead
- Parallel motor control
- **Latency**: Minimal (<0.1ms)

**Direct GPIO Control**:
- Fast pin toggling
- Minimal software overhead
- **Latency**: <0.1ms per operation

## Latency Measurement

### Measurement Methodology

#### End-to-End Measurement
1. **Input trigger**: Keystroke event timestamp
2. **Output detection**: Vibration sensor or accelerometer
3. **Time difference**: End-to-end latency
4. **Statistics**: Mean, median, p95, p99

#### Component Measurement
1. **Input → Pattern**: Time to generate pattern
2. **Pattern → Transmission**: Serialization time
3. **Transmission**: Wireless latency
4. **Reception → Execution**: Deserialization + execution
5. **Execution → Vibration**: Motor response time

### Benchmarking Tools

#### Software Timestamps
- High-resolution timers (microsecond precision)
- Log timestamps at each stage
- Analyze latency distribution
- Identify bottlenecks

#### Hardware Measurement
- Oscilloscope: Input trigger to output signal
- Accelerometer: Detect vibration start
- Logic analyzer: Protocol timing
- **Most accurate**: Hardware measurement

## Recommendations

### Protocol Selection

#### Primary: Optimized BLE
- **Rationale**: Good balance of latency and complexity
- **Configuration**: 7.5ms connection interval
- **Expected latency**: ~5-10ms
- **Power**: Moderate consumption

#### Alternative: WiFi (UDP)
- **Rationale**: Lower latency potential
- **Configuration**: Local network, UDP
- **Expected latency**: ~2-5ms
- **Power**: Higher consumption

#### Future: Custom Protocol
- **Rationale**: Lowest latency
- **Configuration**: Custom 2.4GHz
- **Expected latency**: <1ms
- **Power**: Variable
- **Complexity**: High

### System Optimization

#### Software
1. **Minimal processing**: Direct mapping, lookup tables
2. **Pre-computation**: Patterns ready to send
3. **Efficient protocols**: Minimal overhead
4. **Hardware timers**: Precise timing

#### Hardware
1. **LRA motors**: Fast response (10-20ms)
2. **Driver ICs**: Optimized control (DRV2605)
3. **Hardware timers**: Precise motor control
4. **Efficient power**: Minimize processing overhead

#### Communication
1. **Optimized BLE**: 7.5ms interval, minimal overhead
2. **Or WiFi UDP**: Lower latency if power acceptable
3. **Message batching**: If multiple patterns
4. **No acknowledgment**: For lowest latency (or fast ACK)

### Measurement Strategy
1. **Hardware measurement**: Most accurate
2. **Software timestamps**: For development/debugging
3. **Component analysis**: Identify bottlenecks
4. **Continuous monitoring**: Track performance

## Target Performance

### Phase 1: Initial Implementation
- **Target**: <50ms end-to-end
- **Focus**: Functional system
- **Measurement**: Software timestamps
- **Optimization**: Basic protocol optimization

### Phase 2: Optimization
- **Target**: <20ms end-to-end
- **Focus**: Protocol and hardware optimization
- **Measurement**: Hardware measurement
- **Optimization**: Aggressive BLE settings

### Phase 3: Ultra-Low Latency
- **Target**: <10ms end-to-end
- **Focus**: All optimizations
- **Measurement**: Hardware measurement
- **Optimization**: Custom protocol if needed

## References

### Bluetooth Low Energy (BLE) Latency
1. Bluetooth Special Interest Group. (2023). *Bluetooth Core Specification Version 5.4*. Bluetooth SIG. https://www.bluetooth.com/specifications/specs/core-specification-5-4/
2. Bluetooth Special Interest Group. (2017). *Bluetooth Low Energy: Developer's Guide*. Bluetooth SIG.
3. Gomez, C., Oller, J., & Paradells, J. (2012). Overview and evaluation of Bluetooth Low Energy: An emerging low-power wireless technology. *Sensors*, 12(9), 11734-11753. https://doi.org/10.3390/s120911734

### BLE Latency Optimization
4. Siekkinen, M., Hiienkari, M., Nurminen, J. K., & Nieminen, J. (2012). How low energy is Bluetooth Low Energy? Comparative measurements with ZigBee/802.15.4. *2012 IEEE Wireless Communications and Networking Conference Workshops* (WCNCW), 232-237. https://doi.org/10.1109/WCNCW.2012.6215496
5. Darroudi, S. M., & Gomez, C. (2017). Bluetooth Low Energy mesh networks: A survey. *Sensors*, 17(7), 1467. https://doi.org/10.3390/s17071467

### WiFi Latency
6. IEEE 802.11 Working Group. (2021). *IEEE Standard for Information Technology—Telecommunications and Information Exchange between Systems—Local and Metropolitan Area Networks—Specific Requirements—Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications*. IEEE Std 802.11-2020.
7. Gast, M. S. (2013). *802.11 Wireless Networks: The Definitive Guide* (2nd ed.). O'Reilly Media.

### Low-Latency Wireless Protocols
8. Nordic Semiconductor. (2023). *Enhanced ShockBurst (ESB) Protocol*. nRF24 Series Product Specification. https://infocenter.nordicsemi.com/
9. Nordic Semiconductor. (2023). *Gazell Link Layer Protocol*. nRF51 Series Product Specification. https://infocenter.nordicsemi.com/

### ESP32 BLE Performance
10. Espressif Systems. (2023). *ESP32 Bluetooth Low Energy (BLE) Developer Guide*. ESP-IDF Programming Guide. https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/esp_ble.html
11. Espressif Systems. (2023). *ESP32 BLE Connection Parameters*. ESP-IDF API Reference. https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/esp_gap_ble_api.html

### Motor Driver Latency
12. Texas Instruments. (2015). *DRV2605 Haptic Driver for ERM and LRA*. TI Datasheet SLOS773C. https://www.ti.com/lit/ds/symlink/drv2605.pdf
13. Texas Instruments. (2015). *DRV2605 Application Report: Response Time Optimization*. TI Application Report SLOA193. https://www.ti.com/lit/an/sloa193/sloa193.pdf

### Real-Time Systems and Latency
14. Liu, C. L., & Layland, J. W. (1973). Scheduling algorithms for multiprogramming in a hard-real-time environment. *Journal of the ACM*, 20(1), 46-61. https://doi.org/10.1145/321738.321743
15. Buttazzo, G. C. (2011). *Hard Real-Time Computing Systems: Predictable Scheduling Algorithms and Applications* (3rd ed.). Springer.

### Latency Measurement Techniques
16. Jain, R. (1991). *The Art of Computer Systems Performance Analysis: Techniques for Experimental Design, Measurement, Simulation, and Modeling*. Wiley.
17. Musolesi, M., & Mascolo, C. (2009). A community-based mobility model for ad hoc network research. *Proceedings of the 2nd International Workshop on Multi-hop Ad Hoc Networks* (REALMAN '06), 31-38. https://doi.org/10.1145/1132983.1132990

### Haptic Latency Requirements
18. Hayward, V., Astley, O. R., Cruz-Hernandez, M., Grant, D., & Robles-De-La-Torre, G. (2004). Haptic interfaces and devices. *Sensor Review*, 24(1), 16-29. https://doi.org/10.1108/02602280410515818
19. Jones, L. A., & Sarter, N. B. (2008). Tactile displays: Guidance for their design and application. *Human Factors*, 50(1), 90-111. https://doi.org/10.1518/001872008X250638

### Power-Latency Trade-offs
20. Espressif Systems. (2023). *ESP32 Power Management Guide*. ESP-IDF Programming Guide. https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/power-management.html
21. Texas Instruments. (2015). *Power Management for Haptic Drivers*. TI Application Report SLAA595. https://www.ti.com/lit/an/slaa595/slaa595.pdf

## Related Documents

- [Actuator Technologies Research](actuator_technologies.md)
- [Protocol Specification](../design/protocol_spec.md)
- [Hardware Specifications](../hardware/specs.md)

