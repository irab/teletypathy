# Component Diagram

## Overview

Detailed component relationships and interfaces in the Teletypathy system.

## Desktop Application Components

```
┌─────────────────────────────────────────────────┐
│           Desktop Application                   │
├─────────────────────────────────────────────────┤
│                                                  │
│  ┌──────────────┐    ┌──────────────┐         │
│  │ Keyboard     │    │ Text         │         │
│  │ Capture      │    │ Processing   │         │
│  │              │    │              │         │
│  │ - OS hooks   │    │ - Input      │         │
│  │ - Events     │    │ - Validation │         │
│  └──────┬───────┘    └──────┬───────┘         │
│         │                    │                  │
│         └──────────┬─────────┘                  │
│                    │                            │
│         ┌──────────▼──────────┐                 │
│         │  Device Manager     │                 │
│         │                      │                 │
│         │ - BLE discovery     │                 │
│         │ - Connection        │                 │
│         │ - Status monitoring │                 │
│         └──────────┬──────────┘                 │
│                    │                            │
│         ┌──────────▼──────────┐                 │
│         │  Pattern Encoder    │                 │
│         │  (Core Library)     │                 │
│         │                      │                 │
│         │ - Character mapping │                 │
│         │ - Pattern generation│                 │
│         └──────────┬──────────┘                 │
│                    │                            │
│         ┌──────────▼──────────┐                 │
│         │  Protocol           │                 │
│         │  Serialization      │                 │
│         │                      │                 │
│         │ - Message creation  │                 │
│         │ - Serialization     │                 │
│         └──────────┬──────────┘                 │
│                    │                            │
└────────────────────┼────────────────────────────┘
                     │ BLE
                     │
┌────────────────────▼────────────────────────────┐
│           Wearable Device                        │
├─────────────────────────────────────────────────┤
│                                                  │
│  ┌──────────────┐    ┌──────────────┐          │
│  │ BLE Handler  │    │ Pattern     │          │
│  │              │    │ Queue       │          │
│  │ - Reception  │───▶│              │          │
│  │ - Parsing    │    │ - Storage   │          │
│  │ - Validation │    │ - FIFO     │          │
│  └──────────────┘    └──────┬───────┘          │
│                              │                   │
│                    ┌─────────▼─────────┐        │
│                    │ Pattern Executor   │        │
│                    │                    │        │
│                    │ - Timing control   │        │
│                    │ - Event scheduling │        │
│                    │ - Motor coordination│        │
│                    └──────┬────────────┘        │
│                            │                      │
│                    ┌───────▼────────┐            │
│                    │ Motor Drivers   │            │
│                    │ (DRV2605 × 8)  │            │
│                    │                 │            │
│                    │ - I2C control   │            │
│                    │ - Pattern exec  │            │
│                    └──────┬──────────┘            │
│                           │                       │
│                    ┌──────▼──────┐                │
│                    │ LRA Motors  │                │
│                    │ (8×)        │                │
│                    └─────────────┘                │
│                                                  │
└──────────────────────────────────────────────────┘
```

## Core Library Components

```
┌─────────────────────────────────────────┐
│         Core Library                     │
├─────────────────────────────────────────┤
│                                          │
│  ┌──────────────────┐                   │
│  │ Encoding Module  │                   │
│  │                  │                   │
│  │ - PatternEncoder │                   │
│  │ - Pattern        │                   │
│  │ - ActuatorEvent  │                   │
│  └──────────────────┘                   │
│                                          │
│  ┌──────────────────┐                   │
│  │ Protocol Module  │                   │
│  │                  │                   │
│  │ - Message        │                   │
│  │ - PatternMessage │                   │
│  │ - ConfigMessage  │                   │
│  │ - StatusMessage  │                   │
│  └──────────────────┘                   │
│                                          │
│  ┌──────────────────┐                   │
│  │ Hardware Module  │                   │
│  │                  │                   │
│  │ - Platform       │                   │
│  │   abstraction    │                   │
│  └──────────────────┘                   │
│                                          │
└──────────────────────────────────────────┘
```

## Component Interfaces

### Pattern Encoder Interface

```python
class PatternEncoder:
    def encode_character(self, char: str) -> Optional[Pattern]
    def encode_text(self, text: str) -> List[Pattern]
```

### Protocol Interface

```python
class Message:
    def serialize(self) -> bytes
    @staticmethod
    def deserialize(data: bytes) -> Optional[Message]

class PatternMessage(Message):
    def __init__(self, char: str, pattern_events: List[dict])
```

### Device Manager Interface

```python
class DeviceManager:
    def discover_devices(self) -> List[Device]
    def connect(self, device: Device) -> bool
    def send_pattern(self, pattern: Pattern) -> bool
    def get_status(self) -> DeviceStatus
```

### Pattern Executor Interface

```c
// Firmware interface (C/C++)
void pattern_executor_init(void);
void pattern_executor_add_pattern(pattern_t* pattern);
void pattern_executor_process(void);
bool pattern_executor_is_busy(void);
```

## Component Dependencies

### Desktop Application Dependencies

```
Desktop Application
    ├── Core Library
    │   ├── Encoding Module
    │   ├── Protocol Module
    │   └── Hardware Module (abstraction)
    ├── Platform BLE Library
    │   ├── Windows: bleak
    │   ├── macOS: Core Bluetooth / bleak
    │   └── Linux: bluez / bleak
    └── Platform Keyboard Library
        ├── Windows: win32api
        ├── macOS: Quartz
        └── Linux: X11
```

### Firmware Dependencies

```
Firmware
    ├── ESP-IDF / Arduino Framework
    ├── BLE Stack (ESP32)
    ├── I2C Driver (ESP32)
    ├── Timer Driver (ESP32)
    └── DRV2605 Library (if using drivers)
```

## Data Structures

### Pattern Structure

```python
@dataclass
class Pattern:
    events: List[ActuatorEvent]
    total_duration_ms: int

class ActuatorEvent:
    actuator_id: int
    time_offset_ms: int
    duration_ms: int
    intensity: int
```

### Message Structure

```python
class Message:
    msg_type: MessageType
    payload: bytes
    
class PatternMessage(Message):
    char: str
    pattern_events: List[dict]
```

### Device Status Structure

```python
@dataclass
class DeviceStatus:
    battery_level: int
    connection_quality: int
    error_code: int
    queue_length: int
```

## Communication Patterns

### Request-Response Pattern

```
Desktop                    Device
   │                         │
   │── Status Request ──────▶│
   │                         │
   │◀── Status Response ─────│
   │                         │
```

### Fire-and-Forget Pattern

```
Desktop                    Device
   │                         │
   │── Pattern Message ──────▶│
   │   (No ACK)              │
   │                         │
```

### Notification Pattern

```
Desktop                    Device
   │                         │
   │◀── Status Notification ──│
   │   (Battery low, etc.)   │
   │                         │
```

## Related Documents

- [System Overview](system_overview.md): High-level architecture
- [Data Flow](data_flow.md): Data flow details
- [Protocol Specification](../design/protocol_spec.md): Message protocol


