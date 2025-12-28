# Getting Started

## Overview

Quick start guide for developing with the Teletypathy system.

## Prerequisites

### Software
- Python 3.8+ (for desktop application)
- ESP-IDF or Arduino IDE (for firmware development)
- Git

### Hardware
- ESP32 development board
- LRA motors (or ERM for prototyping)
- DRV2605 drivers (if using LRA)
- USB cable
- Breadboard and jumper wires (for prototyping)

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd teletypathy
```

### Python Dependencies

```bash
pip install -r requirements.txt
```

(Note: requirements.txt to be created with dependencies)

### ESP32 Development Setup

#### Option 1: ESP-IDF

```bash
# Install ESP-IDF (follow official guide)
# https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/

# Set up environment
. $HOME/esp/esp-idf/export.sh
```

#### Option 2: Arduino IDE

1. Install Arduino IDE
2. Add ESP32 board support:
   - File → Preferences → Additional Board Manager URLs
   - Add: `https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json`
3. Tools → Board → Boards Manager → Install "ESP32"

## Quick Start

### 1. Encode a Character

```python
from src.core.encoding import PatternEncoder

encoder = PatternEncoder()
pattern = encoder.encode_character('E')
print(f"Pattern duration: {pattern.get_duration()}ms")
```

### 2. Create a Protocol Message

```python
from src.core.encoding import PatternEncoder
from src.core.protocol import PatternMessage

encoder = PatternEncoder()
pattern = encoder.encode_character('E')

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
```

### 3. Run Examples

```bash
# Basic encoding example
python examples/basic_encoding.py

# Protocol example
python examples/protocol_example.py
```

## Project Structure

```
teletypathy/
├── docs/           # Documentation
├── src/            # Source code
│   ├── core/       # Core library
│   └── desktop/    # Desktop application
├── firmware/       # Embedded firmware
├── tests/          # Test suites
└── examples/       # Example code
```

## Next Steps

1. **Read Documentation**:
   - [API Reference](../api/encoding.md)
   - [Protocol Specification](../design/protocol_spec.md)
   - [Architecture Overview](../architecture/system_overview.md)

2. **Run Tests**:
   ```bash
   python -m pytest tests/
   ```

3. **Explore Examples**:
   - `examples/basic_encoding.py`
   - `examples/protocol_example.py`

4. **Build Hardware**:
   - See [Hardware Assembly](../hardware/assembly.md)
   - Follow [Hardware Architecture](../hardware/architecture.md)

## Development Workflow

1. **Make Changes**: Edit source code
2. **Run Tests**: Verify functionality
3. **Test Examples**: Test with examples
4. **Document**: Update documentation
5. **Commit**: Commit changes

## Getting Help

- **Documentation**: Check `docs/` directory
- **Examples**: See `examples/` directory
- **Issues**: Report issues in repository

## Related Documents

- [API Reference](../api/encoding.md): API documentation
- [Architecture Overview](../architecture/system_overview.md): System design
- [Hardware Assembly](../hardware/assembly.md): Hardware setup


