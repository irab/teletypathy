# Protocol API Reference

## Overview

API reference for the Teletypathy communication protocol.

## Message Classes

### Message

Base message class for all protocol messages.

#### Methods

##### serialize

```python
data = message.serialize() -> bytes
```

Serializes the message to bytes for transmission.

**Returns**:
- Bytes representation of the message

##### deserialize

```python
message = Message.deserialize(data: bytes) -> Optional[Message]
```

Deserializes a message from bytes.

**Parameters**:
- `data` (bytes): Serialized message data

**Returns**:
- `Message` object if valid, `None` otherwise

### PatternMessage

Message for sending a single character pattern.

#### Constructor

```python
message = PatternMessage(char: str, pattern_events: List[dict])
```

Creates a pattern message.

**Parameters**:
- `char` (str): Character being sent
- `pattern_events` (List[dict]): List of actuator events
  - Each event: `{'actuator': int, 'time_offset': int, 'duration': int, 'intensity': int}`

**Example**:
```python
from src.core.protocol import PatternMessage

events = [
    {'actuator': 0, 'time_offset': 0, 'duration': 150, 'intensity': 200}
]
message = PatternMessage('E', events)
data = message.serialize()
```

### PatternBatchMessage

Message for sending multiple patterns in one message.

#### Constructor

```python
message = PatternBatchMessage(patterns: List[tuple])
```

Creates a pattern batch message.

**Parameters**:
- `patterns` (List[tuple]): List of (char, pattern_events) tuples

**Example**:
```python
from src.core.protocol import PatternBatchMessage

patterns = [
    ('H', [{'actuator': 0, 'time_offset': 0, 'duration': 150}]),
    ('E', [{'actuator': 1, 'time_offset': 0, 'duration': 150}]),
    ('L', [{'actuator': 2, 'time_offset': 0, 'duration': 150}])
]
message = PatternBatchMessage(patterns)
data = message.serialize()
```

### ConfigMessage

Message for device configuration.

#### Constructor

```python
message = ConfigMessage(config_type: ConfigType, value: int)
```

Creates a configuration message.

**Parameters**:
- `config_type` (ConfigType): Configuration type
- `value` (int): Configuration value

**Example**:
```python
from src.core.protocol import ConfigMessage, ConfigType

message = ConfigMessage(ConfigType.INTENSITY, 200)
data = message.serialize()
```

### StatusResponseMessage

Message for device status response.

#### Constructor

```python
message = StatusResponseMessage(
    battery_level: int,
    connection_quality: int,
    error_code: int,
    queue_length: int
)
```

Creates a status response message.

**Parameters**:
- `battery_level` (int): Battery level (0-100)
- `connection_quality` (int): Connection quality (RSSI)
- `error_code` (int): Error code (0 = no error)
- `queue_length` (int): Number of patterns in queue

### ErrorMessage

Message for error reporting.

#### Constructor

```python
message = ErrorMessage(error_code: ErrorCode, message: str = '')
```

Creates an error message.

**Parameters**:
- `error_code` (ErrorCode): Error code
- `message` (str): Optional error message

## Enumerations

### MessageType

Message type enumeration.

```python
class MessageType(IntEnum):
    PATTERN = 0x01
    PATTERN_BATCH = 0x02
    CONFIG = 0x03
    STATUS_REQUEST = 0x04
    STATUS_RESPONSE = 0x05
    HEARTBEAT = 0x06
    ERROR = 0x07
    RESET = 0x08
```

### ConfigType

Configuration type enumeration.

```python
class ConfigType(IntEnum):
    INTENSITY = 0x01
    SPEED = 0x02
    PATTERN_SPACING = 0x03
```

### ErrorCode

Error code enumeration.

```python
class ErrorCode(IntEnum):
    INVALID_MESSAGE = 0x01
    QUEUE_FULL = 0x02
    INVALID_ACTUATOR = 0x03
    INVALID_PATTERN = 0x04
    DEVICE_BUSY = 0x05
    LOW_BATTERY = 0x06
```

## Usage Examples

### Sending a Pattern

```python
from src.core.encoding import PatternEncoder
from src.core.protocol import PatternMessage

encoder = PatternEncoder()
pattern = encoder.encode_character('E')

# Convert pattern to message format
events = [
    {
        'actuator': event.actuator_id,
        'time_offset': event.time_offset_ms,
        'duration': event.duration_ms,
        'intensity': event.intensity
    }
    for event in pattern.events
]

message = PatternMessage('E', events)
data = message.serialize()

# Send via BLE
# ble_client.write(data)
```

### Receiving a Message

```python
from src.core.protocol import Message, MessageType, PatternMessage

# Receive data from BLE
# data = ble_client.read()

message = Message.deserialize(data)
if message and message.msg_type == MessageType.PATTERN:
    char, events = PatternMessage.deserialize_pattern(message.payload)
    print(f"Received pattern for character: {char}")
```

### Configuration

```python
from src.core.protocol import ConfigMessage, ConfigType

# Set vibration intensity
intensity_message = ConfigMessage(ConfigType.INTENSITY, 200)
data = intensity_message.serialize()
# ble_client.write(data)

# Set pattern speed
speed_message = ConfigMessage(ConfigType.SPEED, 120)  # 120% speed
data = speed_message.serialize()
# ble_client.write(data)
```

## Message Format

### Binary Format

All messages follow this format:

```
[Header: 2 bytes] [Payload: variable] [Checksum: 1 byte]
```

**Header**:
- Byte 0: Message type
- Byte 1: Payload length

**Checksum**: Simple sum checksum

### Pattern Message Format

```
[Header: 2 bytes]
[Character: 1 byte]
[Actuator count: 1 byte]
[Event 1: 5 bytes] (actuator, time_offset, duration, intensity)
[Event 2: 5 bytes]
...
[Checksum: 1 byte]
```

## Related Documents

- [Protocol Specification](../design/protocol_spec.md): Complete protocol specification
- [Encoding API](encoding.md): Pattern encoding API


