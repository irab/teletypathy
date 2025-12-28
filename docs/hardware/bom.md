# Bill of Materials (BOM)

## Overview

Complete bill of materials for the Teletypathy hardware prototype.

## Main Components

### Microcontroller

| Part | Description | Quantity | Unit Price | Total | Supplier |
|------|-------------|----------|------------|-------|----------|
| ESP32-DevKitC | ESP32 development board | 1 | $5.00 | $5.00 | Adafruit, SparkFun |
| *Alternative* | ESP32-WROOM-32 module | 1 | $3.00 | $3.00 | AliExpress, DigiKey |

### Motor Drivers

| Part | Description | Quantity | Unit Price | Total | Supplier |
|------|-------------|----------|------------|-------|----------|
| DRV2605 | Haptic driver IC | 8 | $1.50 | $12.00 | DigiKey, Mouser |
| *Alternative* | Direct PWM (no driver) | 0 | $0.00 | $0.00 | N/A (for ERM) |

### Actuators

| Part | Description | Quantity | Unit Price | Total | Supplier |
|------|-------------|----------|------------|-------|----------|
| LRA Motor 3mm | Linear resonant actuator | 8 | $1.50 | $12.00 | Precision Microdrives |
| *Alternative* | ERM Motor 3mm | 8 | $0.75 | $6.00 | AliExpress, SparkFun |

### Power System

| Part | Description | Quantity | Unit Price | Total | Supplier |
|------|-------------|----------|------------|-------|----------|
| LiPo Battery | 2000mAh 3.7V | 1 | $5.00 | $5.00 | Adafruit, SparkFun |
| TP4056 | USB charging module | 1 | $1.00 | $1.00 | AliExpress |
| Voltage Regulator | 3.3V LDO (AMS1117) | 1 | $0.50 | $0.50 | DigiKey, Mouser |

### Passive Components

| Part | Description | Quantity | Unit Price | Total | Supplier |
|------|-------------|----------|------------|-------|----------|
| Resistor 4.7kΩ | I2C pull-up | 2 | $0.01 | $0.02 | DigiKey, Mouser |
| Capacitor 100nF | Decoupling | 10 | $0.01 | $0.10 | DigiKey, Mouser |
| Capacitor 10µF | Power filtering | 5 | $0.05 | $0.25 | DigiKey, Mouser |

### Connectors and Hardware

| Part | Description | Quantity | Unit Price | Total | Supplier |
|------|-------------|----------|------------|-------|----------|
| Header Pins | Male headers | 2×20 | $0.50 | $0.50 | Adafruit, SparkFun |
| Jumper Wires | Breadboard wires | 20 | $0.05 | $1.00 | Adafruit, SparkFun |
| USB Cable | Micro USB | 1 | $2.00 | $2.00 | Various |

### Enclosure

| Part | Description | Quantity | Unit Price | Total | Supplier |
|------|-------------|----------|------------|-------|----------|
| 3D Printed Case | Custom enclosure | 1 | $10.00 | $10.00 | 3D printing service |
| *Alternative* | Fabric band/strap | 1 | $5.00 | $5.00 | Custom or purchased |
| Velcro/Strap | Attachment | 1 | $2.00 | $2.00 | Hardware store |

### Optional Components

| Part | Description | Quantity | Unit Price | Total | Supplier |
|------|-------------|----------|------------|-------|----------|
| Status LED | 3mm LED | 1 | $0.10 | $0.10 | DigiKey, Mouser |
| Resistor 220Ω | LED current limit | 1 | $0.01 | $0.01 | DigiKey, Mouser |
| Button | Tactile switch | 1 | $0.50 | $0.50 | DigiKey, Mouser |

## Cost Summary

### Primary Configuration (LRA + DRV2605)

| Category | Cost |
|----------|------|
| Microcontroller | $5.00 |
| Motor Drivers | $12.00 |
| Actuators (LRA) | $12.00 |
| Power System | $6.50 |
| Passive Components | $0.37 |
| Connectors | $3.50 |
| Enclosure | $12.00 |
| **Total** | **$51.37** |

### Alternative Configuration (ERM, No Drivers)

| Category | Cost |
|----------|------|
| Microcontroller | $5.00 |
| Motor Drivers | $0.00 |
| Actuators (ERM) | $6.00 |
| Power System | $6.50 |
| Passive Components | $0.37 |
| Connectors | $3.50 |
| Enclosure | $12.00 |
| **Total** | **$33.37** |

### Minimal Prototype (4 Actuators, ERM)

| Category | Cost |
|----------|------|
| Microcontroller | $5.00 |
| Motor Drivers | $0.00 |
| Actuators (ERM × 4) | $3.00 |
| Power System | $6.50 |
| Passive Components | $0.20 |
| Connectors | $2.00 |
| Enclosure | $10.00 |
| **Total** | **$32.70** |

## Component Notes

### ESP32 Module Options

#### ESP32-DevKitC
- **Pros**: Easy to use, includes USB-to-serial
- **Cons**: Slightly more expensive
- **Use**: Prototyping, development

#### ESP32-WROOM-32
- **Pros**: Lower cost, smaller form factor
- **Cons**: Requires external USB-to-serial
- **Use**: Final product, custom PCB

### Motor Driver Options

#### DRV2605 (Recommended for LRA)
- **Pros**: Optimized for LRA, library support
- **Cons**: Additional cost
- **Use**: Production system with LRA motors

#### Direct PWM (For ERM)
- **Pros**: No additional cost, simpler
- **Cons**: Less precise, slower response
- **Use**: Prototyping, cost-sensitive applications

### Actuator Options

#### LRA Motors (Recommended)
- **Pros**: Fast response, precise control
- **Cons**: Higher cost
- **Use**: Production system

#### ERM Motors
- **Pros**: Lower cost, simpler
- **Cons**: Slower response
- **Use**: Prototyping, cost-sensitive

### Power System Options

#### TP4056 Charging Module
- **Pros**: Simple, includes protection
- **Cons**: Additional board space
- **Use**: Prototyping

#### Custom Charging Circuit
- **Pros**: Integrated design
- **Cons**: More complex design
- **Use**: Final product, custom PCB

## Sourcing Recommendations

### For Prototyping
- **Adafruit/SparkFun**: Good quality, fast shipping (US)
- **DigiKey/Mouser**: Wide selection, reliable
- **AliExpress**: Lower cost, longer shipping

### For Production
- **Component distributors**: DigiKey, Mouser, Arrow
- **Direct from manufacturers**: For volume discounts
- **Local suppliers**: For faster delivery

## Assembly Notes

### Required Tools
- **Soldering iron**: For component assembly
- **Multimeter**: For testing
- **3D printer**: For enclosure (or use service)
- **Basic tools**: Screwdriver, pliers, etc.

### Assembly Complexity
- **Skill level**: Moderate (basic electronics)
- **Time**: 2-4 hours for first assembly
- **Testing**: 1-2 hours for validation

## Future Cost Reduction

### Volume Production
- **Component discounts**: 20-30% at volume
- **Custom PCB**: Lower cost than dev boards
- **Bulk purchasing**: Lower unit costs
- **Target**: <$30 per unit at volume

### Design Optimizations
- **Integrated design**: Custom PCB reduces connectors
- **Component reduction**: Eliminate unnecessary parts
- **Simplified enclosure**: Lower cost materials
- **Target**: <$25 per unit optimized

## Related Documents

- [Hardware Architecture](architecture.md): System design
- [Hardware Specifications](specs.md): Technical specifications
- [Assembly Instructions](assembly.md): Assembly guide


