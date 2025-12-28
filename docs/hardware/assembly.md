# Assembly Instructions

## Overview

Step-by-step assembly instructions for the Teletypathy hardware prototype.

## Prerequisites

### Tools Required
- Soldering iron and solder
- Multimeter
- Wire cutters/strippers
- Screwdriver set
- Breadboard (for initial testing)
- USB cable (micro USB)

### Skills Required
- Basic soldering
- Basic electronics knowledge
- Ability to read circuit diagrams
- Patience and attention to detail

## Assembly Steps

### Step 1: Prepare Components

#### Component Check
- [ ] Verify all components received
- [ ] Check component values (resistors, capacitors)
- [ ] Inspect for damage
- [ ] Organize components by type

#### ESP32 Preparation
- [ ] Verify ESP32 module received
- [ ] Check for any visible damage
- [ ] Note pin assignments
- [ ] Prepare for breadboard or PCB mounting

### Step 2: Power System Assembly

#### Battery and Charging
1. **TP4056 Module**:
   - Solder wires to TP4056 module
   - Connect battery to B+/B- terminals
   - Connect USB for charging test
   - Verify charging LED operation

2. **Voltage Regulation**:
   - Solder AMS1117 regulator
   - Connect input from battery (via TP4056)
   - Connect output (3.3V) to power rail
   - Add decoupling capacitors (100nF, 10µF)

3. **Power Testing**:
   - Measure battery voltage (should be ~3.7-4.2V)
   - Measure 3.3V output (should be 3.3V ±0.1V)
   - Verify no shorts
   - Test charging functionality

### Step 3: Motor Driver Assembly

#### DRV2605 Drivers (If Using LRA)

1. **I2C Bus Setup**:
   - Solder 4.7kΩ pull-up resistors on SDA and SCL
   - Connect SDA and SCL to ESP32 GPIO 21 and 22
   - Verify I2C bus continuity

2. **Driver Connections**:
   - For each DRV2605:
     - Connect VDD to 3.3V
     - Connect GND to ground
     - Connect SDA to I2C bus
     - Connect SCL to I2C bus
     - Connect OUT to LRA motor
     - Connect GND to motor ground

3. **I2C Address Configuration**:
   - Configure different I2C addresses if needed
   - Or use I2C multiplexer if addresses conflict
   - Document addresses for each driver

#### Direct PWM (If Using ERM)

1. **GPIO Connections**:
   - Connect each motor to separate GPIO pin
   - Add current-limiting resistor if needed
   - Connect motor ground to common ground

2. **Motor Connections**:
   - Connect motor positive to GPIO (via resistor if needed)
   - Connect motor negative to ground
   - Verify motor polarity

### Step 4: Actuator Connections

#### LRA Motor Connections
1. **Motor Placement**:
   - Plan actuator layout (linear array)
   - Ensure 40-50mm spacing
   - Mark positions on strap/band

2. **Wiring**:
   - Connect each motor to corresponding DRV2605 OUT
   - Keep wires as short as possible
   - Secure wires to prevent movement
   - Test each motor individually

#### ERM Motor Connections
1. **Direct Connection**:
   - Connect motors directly to GPIO pins
   - Add protection diodes if needed
   - Test each motor with PWM signal

### Step 5: ESP32 Integration

#### ESP32 Connections
1. **Power**:
   - Connect 3.3V to ESP32 VIN (or 3.3V pin)
   - Connect GND to ESP32 ground
   - Verify power LED (if present)

2. **I2C** (for DRV2605):
   - Connect GPIO 21 to SDA
   - Connect GPIO 22 to SCL
   - Verify pull-up resistors present

3. **GPIO** (for ERM or status):
   - Connect status LED to GPIO 2 (optional)
   - Connect button to GPIO 0 (optional)
   - Reserve GPIO pins for motors (if direct PWM)

4. **USB**:
   - Connect USB cable for programming
   - Verify USB communication

### Step 6: Enclosure Assembly

#### 3D Printed Enclosure
1. **Print Enclosure**:
   - Print main enclosure parts
   - Print actuator mounting brackets
   - Verify fit of all components

2. **Component Mounting**:
   - Mount ESP32 in enclosure
   - Mount motor drivers (if separate)
   - Mount battery securely
   - Ensure good ventilation

3. **Actuator Mounting**:
   - Mount actuators in linear array
   - Ensure proper spacing (40-50mm)
   - Secure actuators firmly
   - Test actuator contact with skin

#### Fabric Band Alternative
1. **Band Preparation**:
   - Cut fabric band to size
   - Add Velcro or buckle for attachment
   - Plan component placement

2. **Component Attachment**:
   - Attach control unit to band
   - Attach actuator array to band
   - Ensure secure attachment
   - Test comfort and fit

### Step 7: Final Assembly

#### Wiring Organization
1. **Cable Management**:
   - Organize all wires neatly
   - Secure wires to prevent movement
   - Label connections if needed
   - Ensure no pinched wires

2. **Strain Relief**:
   - Add strain relief at connection points
   - Secure battery connections
   - Protect motor wires

#### Final Checks
1. **Visual Inspection**:
   - Check all connections
   - Verify no loose wires
   - Check for shorts
   - Verify component orientation

2. **Continuity Testing**:
   - Test power connections
   - Test signal connections
   - Verify ground connections
   - Check for shorts

### Step 8: Initial Testing

#### Power-On Test
1. **Battery Test**:
   - Connect battery
   - Measure battery voltage
   - Verify power LED (if present)
   - Check for excessive current draw

2. **ESP32 Test**:
   - Connect USB for programming
   - Upload test firmware
   - Verify serial communication
   - Check ESP32 operation

#### Motor Test
1. **Individual Motor Test**:
   - Test each motor individually
   - Verify motor response
   - Check motor timing
   - Verify motor intensity control

2. **Pattern Test**:
   - Test simple patterns
   - Verify timing accuracy
   - Check multi-motor coordination
   - Test pattern queue

#### BLE Test
1. **Connection Test**:
   - Enable BLE on ESP32
   - Scan for device from phone/computer
   - Verify device discovery
   - Test connection establishment

2. **Communication Test**:
   - Send test patterns via BLE
   - Verify pattern reception
   - Check latency
   - Test error handling

## Troubleshooting

### Common Issues

#### Power Problems
- **No power**: Check battery connection, verify voltage
- **Low voltage**: Check regulator, verify 3.3V output
- **High current**: Check for shorts, verify component values

#### Motor Problems
- **Motor not working**: Check connections, verify power
- **Wrong intensity**: Check driver configuration, verify I2C
- **Timing issues**: Check timer configuration, verify clock

#### Communication Problems
- **BLE not found**: Check antenna, verify BLE enabled
- **Connection fails**: Check BLE parameters, verify firmware
- **High latency**: Optimize BLE settings, check processing

### Testing Procedures

#### Systematic Testing
1. **Power system**: Test each power rail independently
2. **Components**: Test each component individually
3. **Integration**: Test components together
4. **System**: Test complete system operation

#### Measurement Tools
- **Multimeter**: Voltage, current, continuity
- **Oscilloscope**: Signal timing, waveforms (if available)
- **BLE scanner**: BLE device discovery and connection

## Safety Considerations

### Electrical Safety
- **Low voltage**: System uses low voltage (<5V), relatively safe
- **Battery safety**: Handle Li-ion batteries carefully
- **Short circuits**: Avoid short circuits, use fuses if needed

### Physical Safety
- **Heat**: Components may get warm, ensure ventilation
- **Sharp edges**: Be careful with enclosure edges
- **Wearable**: Ensure comfortable fit, no pressure points

## Next Steps

### After Assembly
1. **Firmware development**: Develop and upload firmware
2. **Software integration**: Connect to desktop application
3. **Testing**: Comprehensive system testing
4. **Optimization**: Fine-tune for performance

### Documentation
1. **Record issues**: Document any problems encountered
2. **Modifications**: Note any design changes
3. **Improvements**: Suggest improvements for next version

## Related Documents

- [Hardware Architecture](architecture.md): System design
- [Bill of Materials](bom.md): Component list
- [Hardware Specifications](specs.md): Technical details


