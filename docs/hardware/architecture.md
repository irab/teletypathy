# Hardware Architecture

## Overview

System block diagram and hardware architecture for the Teletypathy wearable device.

## System Block Diagram

```
┌─────────────────────────────────────────────────────────┐
│                    Teletypathy Device                    │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  ┌──────────────┐      ┌──────────────┐                │
│  │  ESP32       │      │  Power       │                │
│  │  Micro-      │◄─────┤  Management  │                │
│  │  controller  │      │  Circuit     │                │
│  └──────┬───────┘      └──────┬───────┘                │
│         │                      │                         │
│         │ BLE                  │ 3.3V / 5V              │
│         │                      │                         │
│  ┌──────▼───────┐      ┌──────▼───────┐                │
│  │  BLE         │      │  Battery     │                │
│  │  Antenna     │      │  (Li-ion)    │                │
│  └──────────────┘      └──────┬───────┘                │
│                                │                         │
│  ┌────────────────────────────▼──────────────┐         │
│  │  Motor Drivers (DRV2605 × 8)              │         │
│  │  ┌────┐ ┌────┐ ┌────┐ ... ┌────┐        │         │
│  │  │ I2C│ │ I2C│ │ I2C│     │ I2C│        │         │
│  │  └─┬──┘ └─┬──┘ └─┬──┘     └─┬──┘        │         │
│  └────┼──────┼──────┼──────────┼────────────┘         │
│       │      │      │          │                       │
│  ┌────▼──┐ ┌▼────┐ ┌▼────┐ ┌─▼────┐                  │
│  │ LRA 0 │ │LRA 1│ │LRA 2│ │LRA 7 │                  │
│  └───────┘ └─────┘ └─────┘ └──────┘                  │
│                                                           │
│  ┌──────────────┐      ┌──────────────┐                │
│  │  Status LED  │      │  USB         │                │
│  │  (Optional)  │      │  Charging    │                │
│  └──────────────┘      └──────────────┘                │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

## Component Details

### Microcontroller: ESP32

#### Selection Rationale
- **Cost**: Low cost (~$3-5)
- **Performance**: 240MHz dual-core
- **BLE**: Native BLE support
- **GPIO**: 34 GPIO pins available
- **Community**: Excellent support

#### Pin Assignment (Proposed)

**I2C Bus (Motor Drivers)**:
- SDA: GPIO 21
- SCL: GPIO 22
- **Note**: DRV2605 drivers share I2C bus

**Status/Control**:
- Status LED: GPIO 2
- Button (optional): GPIO 0

**Power**:
- USB: Via USB-to-serial (or integrated USB on some modules)
- Battery monitoring: ADC on GPIO 35

**BLE**:
- Antenna: Integrated on ESP32 module

### Motor Drivers: DRV2605

#### Selection Rationale
- **LRA support**: Designed for LRA motors
- **Library**: Built-in haptic effect library
- **Control**: I2C interface (simple)
- **Performance**: Fast response, precise control
- **Cost**: ~$1-2 per driver

#### Configuration
- **I2C address**: Configurable (0x5A-0x5D base, 4 addresses with ADDR pins)
- **Multiple drivers**: Use different I2C addresses or I2C multiplexer
- **One motor per driver**: Each DRV2605 drives one LRA motor
- **8 motors require**: 8 DRV2605 drivers (one per motor)
- **I2C multiplexer**: May need TCA9548A if more than 4 addresses needed
- **Control**: I2C commands for pattern execution
- **Timing**: Hardware-based timing (precise)

#### Alternative: Direct PWM Control
- **For ERM motors**: Direct PWM from ESP32
- **Simpler**: No driver IC needed
- **Trade-off**: Less precise control, slower response

### Actuators: LRA Motors

#### Specifications
- **Type**: Linear Resonant Actuator
- **Count**: 4-8 motors (recommended: 6-8)
- **Size**: 3-10mm diameter
- **Voltage**: 1.8-3.6V typical
- **Current**: 30-80mA per motor
- **Response**: 10-20ms response time

#### Placement
- **Layout**: Linear array
- **Spacing**: 40-50mm between motors
- **Location**: Forearm or wrist
- **Attachment**: Strap or band

### Power System

#### Battery
- **Type**: Lithium-ion or Lithium-polymer
- **Capacity**: 2000mAh+ recommended
- **Voltage**: 3.7V nominal (4.2V max)
- **Size**: Compact, wearable

#### Power Management
- **Charging**: USB charging circuit (TP4056 or similar)
- **Regulation**: 3.3V for ESP32, 5V for motors (if needed)
- **Monitoring**: Battery voltage monitoring (ADC)
- **Protection**: Overcharge/overdischarge protection

#### Power Consumption Estimate
- **ESP32 (BLE active)**: ~80-150mA
- **DRV2605 (idle)**: ~5mA × 8 = 40mA
- **LRA motors (active)**: ~50mA × 8 = 400mA (peak, not all simultaneously)
- **Total (active)**: ~200-300mA average
- **Battery life**: ~6-10 hours (2000mAh battery)

### Communication: BLE

#### BLE Configuration
- **Service UUID**: Custom Teletypathy service
- **Characteristics**: Pattern, status, configuration
- **Connection interval**: 7.5ms (minimum for low latency)
- **MTU**: 247 bytes (maximum)
- **Power**: Optimized for low power

#### Antenna
- **Type**: Integrated PCB antenna (ESP32 module)
- **Range**: 10m+ typical
- **Performance**: Adequate for wearable use

## Circuit Design Considerations

### I2C Bus Design

#### Multiple DRV2605 Drivers
- **Shared bus**: All drivers on same I2C bus
- **Addresses**: Configure different I2C addresses
- **Pull-ups**: 4.7kΩ pull-up resistors on SDA/SCL
- **Speed**: 400kHz I2C speed (fast mode)

#### Address Configuration
- **DRV2605**: Base address 0x5A
- **Address pins**: ADDR0, ADDR1 (if available)
- **Or**: Use different I2C addresses if supported
- **Or**: Use I2C multiplexer if needed

### Power Distribution

#### Voltage Rails
- **3.3V**: ESP32, DRV2605 drivers
- **5V**: Optional for motors (if needed)
- **Battery**: 3.7V nominal

#### Current Capacity
- **3.3V rail**: ~500mA capacity needed
- **5V rail**: Optional, if used
- **Battery**: 2000mAh+ capacity

### Signal Integrity

#### Motor Control Signals
- **I2C**: Keep traces short, proper termination
- **Motor connections**: Keep motor wires short
- **Ground**: Common ground plane
- **Noise**: Decoupling capacitors near ICs

## Mechanical Design

### Enclosure

#### Requirements
- **Wearable**: Comfortable on forearm/wrist
- **Size**: Compact, unobtrusive
- **Weight**: <200g total
- **Materials**: Skin-friendly materials

#### Design Options
- **3D printed**: Custom enclosure
- **Fabric band**: Integrated into strap/band
- **Modular**: Separate control unit and actuator array

### Actuator Mounting

#### Placement
- **Linear array**: Actuators in line
- **Spacing**: 40-50mm between actuators
- **Contact**: Good skin contact for vibration
- **Flexibility**: Allow for different arm sizes

#### Attachment
- **Strap**: Adjustable strap/band
- **Secure**: Prevent movement during use
- **Comfort**: Comfortable for extended wear

## Assembly Considerations

### Single-Person Assembly

#### Complexity Level
- **Soldering**: Through-hole or SMD components
- **Assembly**: Mechanical assembly of enclosure
- **Testing**: Basic functionality testing
- **Skills**: Moderate electronics skills needed

#### Tools Required
- **Soldering iron**: For component assembly
- **Multimeter**: For testing
- **3D printer**: For enclosure (or pre-made)
- **Basic tools**: Screwdriver, etc.

### Component Sourcing

#### Availability
- **ESP32**: Widely available
- **DRV2605**: Available from major distributors
- **LRA motors**: Available from various suppliers
- **Battery**: Standard Li-ion/LiPo batteries

#### Cost Estimate (BOM)
- **ESP32 module**: $3-5
- **DRV2605 × 8**: $8-16
- **LRA motors × 8**: $8-24
- **Battery**: $3-5
- **Other components**: $5-10
- **Enclosure**: $5-10
- **Total**: ~$32-70 per unit

## Testing and Validation

### Functional Testing
- **Actuator control**: Test each motor independently
- **Pattern execution**: Verify pattern timing
- **BLE communication**: Test wireless communication
- **Power management**: Test battery and charging

### Performance Testing
- **Latency**: Measure end-to-end latency
- **Power consumption**: Measure current draw
- **Battery life**: Test continuous operation
- **Reliability**: Test connection stability

### Environmental Testing
- **Temperature**: Test in various temperatures
- **Durability**: Test wear and tear
- **Comfort**: Test extended wear comfort

## Future Enhancements

### Additional Features
- **Display**: Small OLED display for status
- **Buttons**: User input buttons
- **Sensors**: Accelerometer, gyroscope
- **Haptic feedback**: Confirmation vibrations

### Optimization
- **Power**: Further power optimization
- **Size**: Smaller form factor
- **Cost**: Reduce BOM cost
- **Performance**: Further latency optimization

## Related Documents

- [Hardware Requirements](requirements.md): Requirements
- [Hardware Comparison](comparison.md): Platform comparison
- [Hardware Specifications](specs.md): Final specifications
- [Bill of Materials](bom.md): Component list

