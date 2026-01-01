# Communication Protocol Specification

## Overview

Specification for the wireless communication protocol between the desktop application and wearable hardware, optimized for ultra-low latency (<10ms end-to-end).

## Protocol Requirements

### Functional Requirements
- **Character transmission**: Send character patterns to hardware
- **Pattern queuing**: Support pattern queues for text sequences
- **Device management**: Discovery, pairing, connection management
- **Status reporting**: Device status, battery level, errors
- **Configuration**: Pattern intensity, speed, other settings

### Non-Functional Requirements
- **Latency**: <10ms end-to-end (target)
- **Reliability**: Error detection and handling
- **Efficiency**: Minimal overhead, optimized for small messages
- **Power**: Low power consumption for battery operation
- **Robustness**: Handle connection drops, errors gracefully

## Protocol Selection

### Primary: Bluetooth Low Energy (BLE)

#### Rationale
- **Latency**: ~5-10ms achievable with optimization
- **Power**: Low power consumption
- **Range**: Adequate for wearable (10m+)
- **Standard**: Widely supported, well-documented
- **Hardware**: Integrated in ESP32, Raspberry Pi Pico W

#### Optimization Strategy
- **Connection interval**: 7.5ms (minimum)
- **Slave latency**: 0 (no connection event skipping)
- **Timeout**: Minimal (7.5s default)
- **MTU**: Maximum (247 bytes)
- **No acknowledgment**: For lowest latency (or fast ACK)

### Alternative: WiFi (UDP)

#### Use Case
- If BLE latency insufficient
- If power consumption acceptable
- If local network available

#### Characteristics
- **Latency**: ~2-5ms (local network)
- **Power**: Higher consumption
- **Range**: WiFi range
- **Complexity**: Network setup required

## Message Format

### Basic Message Structure

```
[Header: 2 bytes] [Payload: variable] [Checksum: 1 byte]
```

### Header Format (2 bytes)

```
Bit layout:
  Byte 0:
    Bit 0-3: Message type (0-15)
    Bit 4-7: Flags (reserved)
  
  Byte 1:
    Bit 0-7: Payload length (0-255 bytes)
```

### Message Types

| Type | Value | Description |
|------|-------|-------------|
| PATTERN | 0x01 | Single pattern message |
| PATTERN_BATCH | 0x02 | Multiple patterns in one message |
| CONFIG | 0x03 | Configuration update |
| STATUS_REQUEST | 0x04 | Request device status |
| STATUS_RESPONSE | 0x05 | Device status response |
| HEARTBEAT | 0x06 | Keep-alive message |
| ERROR | 0x07 | Error message |
| RESET | 0x08 | Reset device |

### Pattern Message Format

#### Single Pattern (Type 0x01)

```
Header: 2 bytes
Payload:
  [Character: 1 byte] (ASCII/Unicode)
  [Pattern data: variable]
Checksum: 1 byte
```

#### Pattern Batch (Type 0x02)

```
Header: 2 bytes
Payload:
  [Count: 1 byte] (number of patterns)
  [Pattern 1: variable]
  [Pattern 2: variable]
  ...
  [Pattern N: variable]
Checksum: 1 byte
```

### Pattern Data Format

#### Basic Pattern Structure

```
[Actuator count: 1 byte] (N actuators)
For each actuator event:
  [Actuator ID: 1 byte] (0-7)
  [Time offset: 2 bytes] (ms, little-endian)
  [Duration: 1 byte] (ms, 0-255)
  [Intensity: 1 byte] (0-255, optional)
```

#### Example Pattern (Letter 'E')

```
Actuator count: 1
  Actuator ID: 0
  Time offset: 0 (ms)
  Duration: 150 (ms)
  Intensity: 200 (default)
```

#### Example Pattern (Letter 'N')

```
Actuator count: 2
  Actuator ID: 0
  Time offset: 0 (ms)
  Duration: 100 (ms)
  Intensity: 200
  Actuator ID: 1
  Time offset: 150 (ms)  (100ms pulse + 50ms gap)
  Duration: 100 (ms)
  Intensity: 200
```

### Configuration Message (Type 0x03)

```
Header: 2 bytes
Payload:
  [Config type: 1 byte]
  [Config value: variable]
Checksum: 1 byte
```

#### Configuration Types

| Type | Value | Description | Value Format |
|------|-------|-------------|--------------|
| INTENSITY | 0x01 | Vibration intensity | 1 byte (0-255) |
| SPEED | 0x02 | Pattern speed multiplier | 1 byte (50-200%, 100=normal) |
| PATTERN_SPACING | 0x03 | Inter-pattern spacing | 1 byte (ms, 0-255) |

### Status Message (Type 0x05)

```
Header: 2 bytes
Payload:
  [Battery level: 1 byte] (0-100%)
  [Connection quality: 1 byte] (RSSI, -128 to 127)
  [Error code: 1 byte] (0=no error)
  [Queue length: 1 byte] (patterns in queue)
Checksum: 1 byte
```

### Error Message (Type 0x07)

```
Header: 2 bytes
Payload:
  [Error code: 1 byte]
  [Error message: variable] (optional, ASCII)
Checksum: 1 byte
```

#### Error Codes

| Code | Description |
|------|-------------|
| 0x01 | Invalid message format |
| 0x02 | Pattern queue full |
| 0x03 | Invalid actuator ID |
| 0x04 | Invalid pattern data |
| 0x05 | Device busy |
| 0x06 | Low battery |

## Communication Flow

### Connection Establishment

1. **Discovery**: Desktop scans for Teletypathy devices
2. **Pairing**: Establish BLE connection
3. **Configuration**: Exchange capabilities, set parameters
4. **Ready**: Device ready to receive patterns

### Pattern Transmission

1. **Character input**: User types character or sends text
2. **Pattern generation**: Character → pattern mapping (<1ms)
3. **Message creation**: Pattern → protocol message (<0.5ms)
4. **Transmission**: BLE send (~5ms)
5. **Reception**: Device receives message (~0.5ms)
6. **Pattern execution**: Execute pattern on motors (~2ms)
7. **Motor response**: Vibration starts (~1ms)

**Total**: ~10ms target

### Error Handling

#### Transmission Errors
- **Timeout**: Retry transmission (up to 3 times)
- **Checksum error**: Request retransmission
- **Connection loss**: Reconnect automatically

#### Device Errors
- **Queue full**: Pause transmission, wait for space
- **Invalid pattern**: Skip pattern, report error
- **Low battery**: Warn user, reduce intensity if needed

## BLE Service Definition

### Service UUID
- **Teletypathy Service**: `0000FF00-0000-1000-8000-00805F9B34FB`

### Characteristics

#### Pattern Characteristic (Write)
- **UUID**: `0000FF01-0000-1000-8000-00805F9B34FB`
- **Properties**: Write, Write Without Response
- **Use**: Send patterns to device
- **Write Without Response**: For lowest latency (no ACK)

#### Status Characteristic (Notify)
- **UUID**: `0000FF02-0000-1000-8000-00805F9B34FB`
- **Properties**: Notify
- **Use**: Device status updates (battery, errors)

#### Configuration Characteristic (Write/Read)
- **UUID**: `0000FF03-0000-1000-8000-00805F9B34FB`
- **Properties**: Read, Write
- **Use**: Get/set device configuration

## Implementation Notes

### Desktop Side (Client)

#### BLE Library
- **Platform**: Use platform-specific BLE libraries
  - Windows: Windows.Devices.Bluetooth
  - macOS: Core Bluetooth
  - Linux: BlueZ/bluepy

#### Connection Management
- **Auto-reconnect**: Handle disconnections gracefully
- **Connection pooling**: Maintain connection when idle
- **Heartbeat**: Send periodic keep-alive (every 5s)

#### Pattern Queue
- **Local queue**: Queue patterns before transmission
- **Flow control**: Pause if device queue full
- **Batching**: Send multiple patterns if beneficial

### Device Side (Server)

#### BLE Stack
- **Platform**: Use platform BLE stack
  - ESP32: ESP-IDF BLE or Arduino BLE
  - Raspberry Pi Pico: CYW43 BLE

#### Pattern Queue
- **Device queue**: Queue received patterns
- **Execution**: Execute patterns sequentially
- **Size**: ~10-20 patterns (adjustable)

#### Timing
- **Hardware timers**: Use hardware timers for precise timing
- **Interrupts**: Timer interrupts for pattern execution
- **Synchronization**: Coordinate multiple actuators

## Latency Optimization

### Minimize Overhead
1. **Small messages**: Minimal header, efficient encoding
2. **No ACK**: Use Write Without Response (or fast ACK)
3. **Direct transmission**: No queuing delays
4. **Pre-computed patterns**: No computation on device

### BLE Optimization
1. **7.5ms interval**: Minimum connection interval
2. **No slave latency**: Immediate connection events
3. **Maximum MTU**: Reduce per-message overhead
4. **Connection parameters**: Optimize for latency

### Hardware Optimization
1. **Fast execution**: Pre-computed patterns, hardware timers
2. **Parallel control**: Control multiple actuators simultaneously
3. **Immediate start**: No delays in pattern execution

## Security Considerations

### Pairing
- **Just Works**: Simple pairing for initial version
- **Future**: Add encryption/authentication if needed

### Message Validation
- **Checksum**: Detect transmission errors
- **Format validation**: Validate message structure
- **Range checks**: Validate actuator IDs, timing values

## Future Enhancements

### Compression
- **Pattern compression**: If patterns repeat
- **Dictionary encoding**: Common patterns as tokens
- **Trade-off**: Latency vs. bandwidth

### Reliability
- **Acknowledgment**: Add ACK for reliability (if latency acceptable)
- **Retransmission**: Automatic retry on error
- **Error correction**: Forward error correction (if needed)

### Advanced Features
- **Bidirectional communication**: Device → desktop feedback
- **Multi-device**: Support multiple devices
- **Synchronization**: Synchronize multiple devices

## References

- Bluetooth SIG: BLE Specification
- ESP32 BLE Documentation
- Raspberry Pi Pico BLE Documentation

## Related Documents

- [Encoding System Design](encoding_system.md): Pattern encoding
- [Symbol Mapping](symbol_mapping.md): Character patterns
- [Latency Optimization Research](../research/latency_optimization.md): Latency strategies



