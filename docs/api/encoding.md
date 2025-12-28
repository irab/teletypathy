# Encoding API Reference

## Overview

API reference for the Teletypathy pattern encoding library.

## PatternEncoder

### Class: PatternEncoder

Main encoder class for converting characters to tactile patterns.

#### Constructor

```python
encoder = PatternEncoder()
```

Creates a new pattern encoder instance with built-in character mappings.

#### Methods

##### encode_character

```python
pattern = encoder.encode_character(char: str) -> Optional[Pattern]
```

Encodes a single character into a tactile pattern.

**Parameters**:
- `char` (str): Single character to encode

**Returns**:
- `Pattern` object if character is supported, `None` otherwise

**Example**:
```python
encoder = PatternEncoder()
pattern = encoder.encode_character('E')
if pattern:
    print(f"Pattern duration: {pattern.get_duration()}ms")
```

##### encode_text

```python
patterns = encoder.encode_text(text: str) -> List[Pattern]
```

Encodes a text string into a list of patterns.

**Parameters**:
- `text` (str): Text string to encode

**Returns**:
- List of `Pattern` objects (one per character)

**Example**:
```python
encoder = PatternEncoder()
patterns = encoder.encode_text("HELLO")
for i, pattern in enumerate(patterns):
    print(f"Character {i}: {pattern.get_duration()}ms")
```

## Pattern

### Class: Pattern

Represents a tactile pattern with actuator events.

#### Properties

- `events` (List[ActuatorEvent]): List of actuator activation events
- `total_duration_ms` (int): Total pattern duration in milliseconds

#### Methods

##### get_duration

```python
duration = pattern.get_duration() -> int
```

Returns the total pattern duration in milliseconds.

**Returns**:
- Total duration (ms)

**Example**:
```python
pattern = encoder.encode_character('E')
duration = pattern.get_duration()  # e.g., 150
```

## ActuatorEvent

### Class: ActuatorEvent

Represents a single actuator activation event.

#### Constructor

```python
event = ActuatorEvent(
    actuator_id: int,
    time_offset_ms: int,
    duration_ms: int,
    intensity: int = 200
)
```

Creates a new actuator event.

**Parameters**:
- `actuator_id` (int): Actuator ID (0-7)
- `time_offset_ms` (int): Time offset from pattern start (ms)
- `duration_ms` (int): Duration of activation (ms)
- `intensity` (int): Vibration intensity (0-255), default 200

#### Properties

- `actuator_id` (int): Actuator ID
- `time_offset_ms` (int): Time offset from pattern start
- `duration_ms` (int): Duration of activation
- `intensity` (int): Vibration intensity

**Example**:
```python
event = ActuatorEvent(actuator_id=0, time_offset_ms=0, duration_ms=150, intensity=200)
print(f"Actuator {event.actuator_id} at {event.time_offset_ms}ms for {event.duration_ms}ms")
```

## Usage Examples

### Basic Character Encoding

```python
from src.core.encoding import PatternEncoder

encoder = PatternEncoder()

# Encode single character
pattern = encoder.encode_character('E')
if pattern:
    print(f"Pattern has {len(pattern.events)} events")
    for event in pattern.events:
        print(f"  Actuator {event.actuator_id}: {event.time_offset_ms}ms + {event.duration_ms}ms")
```

### Text Encoding

```python
from src.core.encoding import PatternEncoder

encoder = PatternEncoder()

# Encode text string
text = "HELLO WORLD"
patterns = encoder.encode_text(text)

print(f"Encoded {len(patterns)} patterns")
for i, pattern in enumerate(patterns):
    print(f"  {text[i]}: {pattern.get_duration()}ms")
```

### Pattern Inspection

```python
from src.core.encoding import PatternEncoder

encoder = PatternEncoder()

pattern = encoder.encode_character('N')
print(f"Total duration: {pattern.get_duration()}ms")
print(f"Number of events: {len(pattern.events)}")

for event in pattern.events:
    print(f"Event: actuator={event.actuator_id}, "
          f"time={event.time_offset_ms}ms, "
          f"duration={event.duration_ms}ms, "
          f"intensity={event.intensity}")
```

## Supported Characters

### Letters
- All uppercase and lowercase letters (A-Z, a-z)
- Case-insensitive (same pattern for upper/lowercase)

### Numbers
- Digits 0-9

### Punctuation
- Space (pause)
- Period (.)
- Comma (,)
- Question mark (?)
- Exclamation mark (!)
- And more (see symbol mapping)

## Related Documents

- [Symbol Mapping](../design/symbol_mapping.md): Complete character mappings
- [Encoding System Design](../design/encoding_system.md): Encoding strategy


