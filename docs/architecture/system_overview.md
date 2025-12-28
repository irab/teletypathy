# System Overview

## Overview

High-level architecture of the Teletypathy tactile communication system.

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Desktop Application                      │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │  Keyboard    │  │  Text        │  │  Device      │     │
│  │  Capture     │  │  Processing  │  │  Manager     │     │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘     │
│         │                  │                  │             │
│         └──────────────────┼──────────────────┘             │
│                            │                                 │
│                  ┌─────────▼─────────┐                      │
│                  │  Pattern Encoder   │                      │
│                  │  (Core Library)     │                      │
│                  └─────────┬─────────┘                      │
│                            │                                 │
│                  ┌─────────▼─────────┐                      │
│                  │  Protocol          │                      │
│                  │  Serialization     │                      │
│                  └─────────┬─────────┘                      │
│                            │                                 │
└────────────────────────────┼─────────────────────────────────┘
                             │ BLE/WiFi
                             │
┌────────────────────────────▼─────────────────────────────────┐
│                    Wearable Device                           │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐      ┌──────────────┐                    │
│  │  BLE         │      │  Pattern      │                    │
│  │  Handler      │─────▶│  Queue        │                    │
│  └──────────────┘      └──────┬───────┘                    │
│                                │                             │
│                       ┌─────────▼─────────┐                  │
│                       │  Pattern          │                  │
│                       │  Executor        │                  │
│                       └──────┬───────────┘                  │
│                               │                              │
│                    ┌───────────▼──────────┐                  │
│                    │  Motor Drivers       │                  │
│                    │  (DRV2605 × 8)       │                  │
│                    └──────┬───────────────┘                  │
│                            │                                  │
│                    ┌───────▼────────┐                        │
│                    │  LRA Motors    │                        │
│                    │  (8 actuators) │                        │
│                    └─────────────────┘                        │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

## Component Layers

### Desktop Application Layer

#### Input Modules
- **Keyboard Capture**: Real-time keystroke capture
- **Text Processing**: Text message input and processing
- **Device Manager**: BLE device discovery and connection

#### Core Library
- **Pattern Encoder**: Character-to-pattern conversion
- **Protocol**: Message serialization/deserialization
- **Hardware Abstraction**: Platform-agnostic interfaces

### Communication Layer

#### Wireless Protocol
- **BLE**: Primary communication protocol
- **Protocol Messages**: Pattern, configuration, status
- **Latency Optimization**: Optimized connection parameters

### Hardware Layer

#### Embedded Firmware
- **BLE Handler**: Wireless communication
- **Pattern Queue**: Pattern buffering
- **Pattern Executor**: Pattern execution engine
- **Motor Control**: Actuator control

#### Hardware Components
- **ESP32**: Microcontroller
- **DRV2605**: Motor drivers (8×)
- **LRA Motors**: Actuators (8×)

## Data Flow

### Keystroke to Vibration Flow

1. **Input**: User types character
2. **Capture**: Keyboard capture module detects keystroke
3. **Encoding**: Pattern encoder converts character to pattern
4. **Serialization**: Protocol module serializes pattern message
5. **Transmission**: BLE transmits message to device
6. **Reception**: Device receives message via BLE handler
7. **Queueing**: Pattern added to execution queue
8. **Execution**: Pattern executor executes pattern
9. **Motor Control**: Motor drivers activate actuators
10. **Vibration**: User feels tactile pattern

### Text Message Flow

1. **Input**: User enters text message
2. **Processing**: Text processing module handles input
3. **Encoding**: Each character encoded to pattern
4. **Batching**: Patterns batched into message
5. **Transmission**: Batch message sent to device
6. **Queueing**: Patterns added to queue sequentially
7. **Execution**: Patterns executed in order
8. **Vibration**: User feels sequence of patterns

## Key Design Decisions

### Architecture Decisions

1. **Layered Architecture**: Clear separation of concerns
2. **Core Library**: Reusable encoding and protocol
3. **Platform Abstraction**: Platform-specific implementations
4. **Message-Based**: Protocol-based communication

### Performance Decisions

1. **Pre-computed Patterns**: Fast lookup, no computation
2. **Optimized BLE**: Low-latency connection parameters
3. **Hardware Timers**: Precise motor control timing
4. **Pattern Queue**: Buffering for smooth execution

### Design Patterns

1. **Encoder Pattern**: Character-to-pattern conversion
2. **Protocol Pattern**: Message serialization
3. **Queue Pattern**: Pattern buffering and execution
4. **Hardware Abstraction**: Platform-independent interfaces

## Related Documents

- [Data Flow Diagram](data_flow.md): Detailed data flow
- [Component Diagram](component_diagram.md): Component relationships
- [Protocol Specification](../design/protocol_spec.md): Communication protocol


