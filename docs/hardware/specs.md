# Hardware Specifications

## Overview

Final hardware specifications for the Teletypathy system, based on platform selection and design decisions.

## Selected Platform: ESP32

### Microcontroller Specifications

#### ESP32-WROOM-32 Module
- **MCU**: ESP32-D0WDQ6
- **CPU**: Dual-core Xtensa LX6, 240MHz
- **RAM**: 520KB SRAM
- **Flash**: 4MB (typical modules)
- **GPIO**: 34 GPIO pins
- **Wireless**: WiFi 802.11 b/g/n + Bluetooth 4.2 (BLE)
- **Operating Voltage**: 3.0-3.6V
- **Operating Current**: 80-150mA (active, BLE)
- **Sleep Current**: <1mA (deep sleep)

#### Pin Assignments
- **GPIO 21**: I2C SDA (motor drivers)
- **GPIO 22**: I2C SCL (motor drivers)
- **GPIO 2**: Status LED (optional)
- **GPIO 0**: Button (optional)
- **GPIO 35**: Battery voltage monitoring (ADC)

## Actuator System

### Motor Drivers: DRV2605

#### Specifications
- **Type**: Haptic driver IC
- **Quantity**: 8 units
- **Interface**: I2C (shared bus)
- **Supply Voltage**: 2.5-5.2V
- **Operating Current**: ~5mA (idle per driver)
- **Peak Current**: Up to 2A (per driver, for motors)
- **Package**: 3×3mm WQFN

#### Features
- LRA and ERM support
- Built-in haptic effect library
- Automatic resonance tracking (LRA)
- Real-time playback mode
- I2C control interface

### Actuators: LRA Motors

#### Specifications
- **Type**: Linear Resonant Actuator
- **Quantity**: 6-8 units (recommended: 8)
- **Size**: 3-10mm diameter
- **Resonance Frequency**: ~175 Hz (typical)
- **Operating Voltage**: 1.8-3.6V
- **Operating Current**: 30-80mA per motor
- **Response Time**: 10-20ms
- **Vibration Amplitude**: 0.5-3.0 m/s²

#### Placement
- **Layout**: Linear array
- **Spacing**: 40-50mm between actuators
- **Location**: Forearm or wrist
- **Attachment**: Adjustable strap/band

## Power System

### Battery

#### Specifications
- **Type**: Lithium-ion or Lithium-polymer
- **Capacity**: 2000mAh (recommended)
- **Voltage**: 3.7V nominal (4.2V max charged)
- **Size**: Compact, wearable form factor
- **Weight**: ~40-50g (typical)

### Power Management

#### Charging Circuit
- **IC**: TP4056 or equivalent
- **Input**: USB (5V)
- **Charging Current**: 1A (typical)
- **Protection**: Overcharge, overdischarge protection

#### Voltage Regulation
- **Regulator**: AMS1117-3.3 or equivalent
- **Input**: 3.7V (battery)
- **Output**: 3.3V (for ESP32 and drivers)
- **Current Capacity**: 500mA+

### Power Consumption

#### Active Operation
- **ESP32 (BLE)**: 80-150mA
- **DRV2605 drivers (idle)**: ~40mA (8 × 5mA)
- **LRA motors (active)**: ~200-400mA (peak, not all simultaneously)
- **Total average**: ~200-300mA

#### Idle Operation
- **ESP32 (idle)**: 10-20mA
- **DRV2605 (idle)**: ~40mA
- **Total idle**: ~50-60mA

#### Sleep Mode
- **ESP32 (deep sleep)**: <1mA
- **Total sleep**: <2mA

#### Battery Life Estimates
- **Active use**: ~6-10 hours (2000mAh battery)
- **Idle**: ~30-40 hours
- **Sleep**: Weeks to months

## Communication

### Bluetooth Low Energy (BLE)

#### Specifications
- **Standard**: Bluetooth 4.2 (BLE)
- **Range**: 10m+ (typical)
- **Frequency**: 2.4 GHz ISM band
- **Data Rate**: Up to 1 Mbps
- **Latency**: 5-10ms (optimized)

#### Configuration
- **Connection Interval**: 7.5ms (minimum for low latency)
- **Slave Latency**: 0 (no connection event skipping)
- **Supervision Timeout**: 500ms
- **MTU Size**: 247 bytes (maximum)

#### Service Definition
- **Service UUID**: `0000FF00-0000-1000-8000-00805F9B34FB`
- **Pattern Characteristic**: Write, Write Without Response
- **Status Characteristic**: Notify
- **Config Characteristic**: Read, Write

## Mechanical Specifications

### Dimensions

#### Control Unit
- **Length**: ~60-80mm
- **Width**: ~40-50mm
- **Height**: ~15-20mm
- **Weight**: ~50-80g (including battery)

#### Actuator Array
- **Length**: ~280-400mm (8 actuators, 40-50mm spacing)
- **Width**: ~20-30mm
- **Height**: ~10-15mm
- **Weight**: ~30-50g

#### Total System
- **Total Weight**: <200g (target)
- **Form Factor**: Wearable, unobtrusive

### Enclosure

#### Materials
- **3D Printed**: PLA or PETG (prototype)
- **Production**: Injection molded plastic (future)
- **Strap**: Fabric, adjustable

#### Requirements
- **Comfort**: Comfortable for extended wear
- **Durability**: Withstand daily use
- **Ventilation**: Adequate cooling
- **Access**: USB charging access

## Performance Specifications

### Latency

#### Target Performance
- **End-to-end**: <10ms (keystroke to vibration)
- **Pattern generation**: <1ms
- **BLE transmission**: <5ms
- **Pattern execution**: <4ms
- **Motor response**: <1ms

#### Measured Performance (To Be Validated)
- **Initial target**: <50ms (Phase 1)
- **Optimized target**: <20ms (Phase 2)
- **Final target**: <10ms (Phase 3)

### Throughput

#### Pattern Rate
- **Maximum**: 10+ patterns per second
- **Typical**: 5-8 patterns per second
- **Queue capacity**: 10-20 patterns

### Reliability

#### Connection
- **Uptime**: 99%+ during active use
- **Range**: 10m+ reliable connection
- **Reconnection**: Automatic reconnection on drop

#### Error Handling
- **Error detection**: Checksum validation
- **Error recovery**: Automatic retry
- **Graceful degradation**: Continue operation on errors

## Environmental Specifications

### Operating Conditions
- **Temperature**: 0-40°C operating range
- **Humidity**: Normal indoor conditions (non-condensing)
- **Altitude**: Sea level to 2000m

### Storage Conditions
- **Temperature**: -20 to 60°C
- **Humidity**: <85% relative humidity

### Durability
- **Drop resistance**: 1m drop onto hard surface
- **Wear resistance**: Daily wear for 1+ year
- **Water resistance**: Basic splash resistance (optional)

## Safety Specifications

### Electrical Safety
- **Operating Voltage**: <5V (low voltage, safe)
- **Current**: <500mA maximum
- **Protection**: Overcurrent, overvoltage protection
- **Isolation**: Basic isolation from mains

### Battery Safety
- **Protection**: Overcharge, overdischarge protection
- **Temperature**: Thermal protection
- **Handling**: Standard Li-ion safety practices

### Physical Safety
- **Materials**: Skin-friendly materials
- **Temperature**: Components stay within safe limits
- **Sharp edges**: Rounded edges, no sharp points

## Compliance

### Regulatory (Future)
- **FCC**: Radio frequency compliance (if required)
- **CE**: European compliance (if required)
- **RoHS**: Restriction of hazardous substances

### Standards
- **Bluetooth**: Bluetooth SIG compliance
- **USB**: USB specification compliance
- **Battery**: UN38.3 transportation safety (if shipped)

## Revision History

### Version 1.0 (Initial Specification)
- **Date**: 2024
- **Platform**: ESP32 selected
- **Actuators**: LRA with DRV2605 drivers
- **Status**: Specification complete, prototype pending

## Related Documents

- [Hardware Requirements](requirements.md): Requirements
- [Hardware Comparison](comparison.md): Platform selection
- [Hardware Architecture](architecture.md): System design
- [Bill of Materials](bom.md): Component list



