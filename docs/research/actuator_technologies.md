# Actuator Technologies Research

## Overview

Comparison of vibration motor types (ERM vs LRA) and other actuator technologies for tactile communication.

## Vibration Motor Types

### Eccentric Rotating Mass (ERM) Motors

#### Physical Principle
- Unbalanced mass rotates around motor shaft
- Centrifugal force creates vibration
- Vibration frequency = rotation frequency
- Amplitude controlled by voltage/PWM duty cycle

#### Technical Specifications

**Typical Characteristics**:
- **Frequency range**: 50-300 Hz (depends on voltage)
- **Amplitude**: 0.5-5.0 m/s² (varies with voltage)
- **Response time**: 50-100ms to full amplitude
- **Voltage range**: 1.5-5V typical
- **Current consumption**: 50-150mA at 3V
- **Size**: 3-12mm diameter typical
- **Weight**: 0.5-5g typical
- **Cost**: $0.50-$2.00 per unit

**Control**:
- Simple PWM control
- Duty cycle controls amplitude
- Frequency follows voltage (not independently controllable)
- No driver IC required (direct drive possible)

#### Advantages
- **Very low cost**: Most economical option
- **Simple control**: Direct PWM, no driver needed
- **Good amplitude range**: Wide vibration strength
- **Widely available**: Many suppliers and sizes
- **Robust**: Mechanical simplicity, durable
- **Proven technology**: Extensive use in mobile devices

#### Disadvantages
- **Slower response**: 50-100ms response time
- **Limited frequency control**: Frequency tied to voltage
- **Mechanical wear**: Moving parts degrade over time
- **Power consumption**: Higher than LRA for same output
- **Less precise**: Less control over vibration characteristics
- **Startup delay**: Takes time to reach full amplitude

#### Applications
- Mobile phone vibration
- Game controller rumble
- Low-cost wearables
- Notification devices
- Prototyping and testing

### Linear Resonant Actuator (LRA)

#### Physical Principle
- Voice coil moves mass linearly
- Operates at mechanical resonance frequency
- Resonance frequency typically ~175 Hz
- Amplitude controlled by drive signal strength
- Requires AC drive signal at resonance

#### Technical Specifications

**Typical Characteristics**:
- **Frequency range**: Narrow band (~150-200 Hz, resonance)
- **Amplitude**: 0.5-3.0 m/s² (varies with drive)
- **Response time**: 10-20ms to full amplitude
- **Drive voltage**: 1.8-3.6V typical
- **Current consumption**: 30-80mA at 3V
- **Size**: 3-10mm typical
- **Weight**: 0.3-3g typical
- **Cost**: $1-$3 per unit

**Control**:
- Requires driver IC (e.g., DRV2605, DRV2604)
- AC drive signal at resonance frequency
- Amplitude controlled by drive signal
- More complex control than ERM

#### Advantages
- **Faster response**: 10-20ms response time
- **Lower power**: More efficient than ERM
- **Precise control**: Better frequency and amplitude control
- **Consistent performance**: Less variation
- **Better frequency control**: Fixed resonance frequency
- **Premium feel**: Used in high-end devices

#### Disadvantages
- **Higher cost**: 2-3x more expensive than ERM
- **Requires driver IC**: Additional component and cost
- **Narrow frequency range**: Limited to resonance
- **Less amplitude range**: Smaller maximum amplitude
- **More complex**: Requires driver and control circuitry
- **Fragility**: More sensitive to damage

#### Applications
- Premium mobile devices (iPhone, Apple Watch)
- High-quality wearables
- Precise haptic feedback systems
- Applications requiring fast response

### Comparison Summary

| Characteristic | ERM | LRA |
|----------------|-----|-----|
| Cost | Low ($0.50-$2) | Moderate ($1-$3) |
| Response Time | 50-100ms | 10-20ms |
| Power Consumption | Higher | Lower |
| Control Complexity | Simple | Moderate |
| Frequency Control | Limited | Good |
| Amplitude Range | Wide | Moderate |
| Driver Required | No | Yes |
| Durability | Good | Moderate |

## Other Actuator Technologies

### Piezoelectric Actuators

#### Characteristics
- **Principle**: Piezoelectric material deforms with voltage
- **Frequency range**: DC to kHz (very wide)
- **Response time**: <1ms (very fast)
- **Amplitude**: Small displacement
- **Cost**: Moderate to high
- **Power**: Low consumption
- **Control**: Requires high voltage driver

#### Advantages
- Very fast response
- Wide frequency range
- Precise control
- Low power

#### Disadvantages
- Higher cost
- Complex drive circuitry
- Small displacement
- High voltage required

#### Application
- High-precision haptics
- Research applications
- Specialized systems

### Electrotactile Stimulation

#### Characteristics
- **Principle**: Electrical current stimulates nerves
- **Frequency range**: 1-1000 Hz
- **Response time**: Instantaneous
- **Intensity**: Current amplitude (mA range)
- **Cost**: Low (electrodes + driver)
- **Power**: Very low
- **Control**: Current-controlled driver

#### Advantages
- Very fast response
- Precise control
- Low power
- Can encode frequency/intensity

#### Disadvantages
- Safety concerns (electrical)
- Skin irritation possible
- Individual variation in sensitivity
- Requires good electrode contact

#### Application
- Research applications
- Specialized systems
- Not recommended for general use

## Driver ICs for LRA

### Texas Instruments DRV2605

#### Features
- **Actuator support**: LRA, ERM, piezo
- **Actuator count**: **One actuator per DRV2605** (single-channel driver)
- **Library**: Built-in haptic effect library
- **Control**: I2C interface
- **I2C address**: Base 0x5A, configurable to 0x5A-0x5D (4 addresses with ADDR pins)
- **Voltage**: 2.5-5.2V supply
- **Current**: Up to 2A peak
- **Package**: 3×3mm WQFN

#### Important Note
**Each DRV2605 can drive only ONE actuator at a time.** For 8 motors, you need 8 DRV2605 drivers. If more than 4 addresses are needed, use an I2C multiplexer (e.g., TCA9548A).

#### Advantages
- Easy to use (library effects)
- Good performance
- Flexible (multiple actuator types)
- Well-documented

#### Disadvantages
- Additional cost (~$1-2)
- Requires I2C interface
- Slightly more complex

### Alternative Drivers

#### DRV2604
- Similar to DRV2605
- Slightly different features
- Alternative option

#### Custom Drivers
- More complex
- More control
- Higher development effort

## Recommendation for Teletypathy

### Primary Choice: LRA with DRV2605

**Rationale**:
1. **Fast response**: 10-20ms supports <10ms latency goal
2. **Precise control**: Better pattern encoding
3. **Lower power**: Important for battery operation
4. **Good balance**: Cost vs. performance
5. **Proven**: Used in high-end devices

**Implementation**:
- 4-8 LRA motors
- DRV2605 driver IC per motor (or shared)
- I2C control interface
- PWM for amplitude control

### Alternative: ERM Motors

**Use Case**:
- Initial prototyping
- Cost-sensitive applications
- If latency requirements relaxed

**Implementation**:
- 4-8 ERM motors
- Direct PWM control
- Simpler circuitry
- Lower cost

## Power Considerations

### ERM Power Consumption
- **Typical**: 50-150mA at 3V per motor
- **8 motors**: 400-1200mA total (significant)
- **Battery impact**: High consumption
- **Solution**: Duty cycle control, not all motors simultaneously

### LRA Power Consumption
- **Typical**: 30-80mA at 3V per motor
- **8 motors**: 240-640mA total (better)
- **Battery impact**: Moderate consumption
- **Solution**: Still need power management

### Power Management Strategies
1. **Duty cycle**: Not all motors active simultaneously
2. **Intensity control**: Lower intensity = lower power
3. **Sleep modes**: Power down when not in use
4. **Battery selection**: High capacity battery needed
5. **Efficient patterns**: Minimize simultaneous activation

## Recommendations

### Actuator Selection
1. **Primary**: LRA motors (fast response, low power)
2. **Count**: 4-8 actuators (spatial encoding)
3. **Driver**: DRV2605 (easy control, library)
4. **Alternative**: ERM for prototyping/cost-sensitive

### Power Management
1. **Battery**: High capacity (2000mAh+)
2. **Management**: Duty cycle, sleep modes
3. **Optimization**: Efficient pattern design
4. **Monitoring**: Battery level tracking

### Control Design
1. **Interface**: I2C for DRV2605
2. **Timing**: Hardware timers for precise control
3. **Patterns**: Pre-defined library + custom patterns
4. **Intensity**: User-adjustable

## References

### Motor Driver Specifications
1. Texas Instruments. (2015). *DRV2605 Haptic Driver for ERM and LRA*. TI Datasheet SLOS773C. https://www.ti.com/lit/ds/symlink/drv2605.pdf
2. Texas Instruments. (2015). *DRV2605 Application Report: Haptic Driver ICs*. TI Application Report SLOA193. https://www.ti.com/lit/an/sloa193/sloa193.pdf
3. Texas Instruments. (2015). *DRV2604 Haptic Driver*. TI Datasheet SLOS772C. https://www.ti.com/lit/ds/symlink/drv2604.pdf

### Vibration Motor Technologies
4. Precision Microdrives. (2023). *ERM vs LRA: A Comparison Guide*. Precision Microdrives Ltd. https://www.precisionmicrodrives.com/content/erm-vs-lra-comparison-guide/
5. Precision Microdrives. (2023). *Linear Resonant Actuator (LRA) Motors*. Precision Microdrives Ltd. https://www.precisionmicrodrives.com/linear-resonant-actuator-lra/
6. Precision Microdrives. (2023). *Eccentric Rotating Mass (ERM) Motors*. Precision Microdrives Ltd. https://www.precisionmicrodrives.com/eccentric-rotating-mass-erm/

### Haptic Actuator Selection
7. Hayward, V., Astley, O. R., Cruz-Hernandez, M., Grant, D., & Robles-De-La-Torre, G. (2004). Haptic interfaces and devices. *Sensor Review*, 24(1), 16-29. https://doi.org/10.1108/02602280410515818
8. Jones, L. A., & Sarter, N. B. (2008). Tactile displays: Guidance for their design and application. *Human Factors*, 50(1), 90-111. https://doi.org/10.1518/001872008X250638

### Vibration Motor Control
9. Pabon, J., Saitis, C., & Fritz, G. (2017). Haptic feedback in virtual reality: A survey. *IEEE Transactions on Haptics*, 10(4), 463-475. https://doi.org/10.1109/TOH.2017.2702227
10. Okamura, A. M., Cutkosky, M. R., & Dennerlein, J. T. (2001). Reality-based models for vibration feedback in virtual environments. *IEEE/ASME Transactions on Mechatronics*, 6(3), 245-252. https://doi.org/10.1109/3516.951364

### Piezoelectric Actuators
11. Uchino, K. (2000). *Ferroelectric Devices*. Marcel Dekker.
12. Uchino, K. (2010). *Advanced Piezoelectric Materials: Science and Technology*. Woodhead Publishing.

### Electrotactile Stimulation
13. Kaczmarek, K. A., Webster, J. G., Bach-y-Rita, P., & Tompkins, W. J. (1991). Electrotactile and vibrotactile displays for sensory substitution systems. *IEEE Transactions on Biomedical Engineering*, 38(1), 1-16. https://doi.org/10.1109/10.68204
14. Kajimoto, H., Kanno, Y., & Tachi, S. (2006). Forehead electrotactile display for vision substitution. *EuroHaptics*, 135-140.

### Power Consumption and Efficiency
15. Texas Instruments. (2015). *Power Management for Haptic Drivers*. TI Application Report SLAA595. https://www.ti.com/lit/an/slaa595/slaa595.pdf
16. Espressif Systems. (2023). *ESP32 Power Consumption Guide*. ESP-IDF Programming Guide. https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/power-management.html

### Motor Response Characteristics
17. Cholewiak, R. W., & Collins, A. A. (2003). Vibrotactile localization on the arm: Effects of place, space, and age. *Perception & Psychophysics*, 65(7), 1058-1077. https://doi.org/10.3758/BF03194834
18. Van Erp, J. B., & Van Veen, H. A. (2004). Vibrotactile in-vehicle navigation system. *Transportation Research Part F: Traffic Psychology and Behaviour*, 7(4-5), 247-256. https://doi.org/10.1016/j.trf.2004.09.003

### Commercial Haptic Systems
19. Apple Inc. (2015). *Apple Watch Human Interface Guidelines: Haptics*. Apple Developer Documentation. https://developer.apple.com/design/human-interface-guidelines/haptics
20. Google. (2023). *Android Haptics: VibrationEffect API*. Android Developer Documentation. https://developer.android.com/reference/android/os/VibrationEffect

## Related Documents

- [Haptic Feedback Research](haptic_feedback.md)
- [Latency Optimization Research](latency_optimization.md)
- [Hardware Specifications](../hardware/specs.md)

