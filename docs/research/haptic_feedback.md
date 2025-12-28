# Haptic Feedback Research

## Overview

Survey of existing haptic feedback systems and best practices for tactile communication.

## Haptic Actuator Technologies

### Vibration Motors

#### Eccentric Rotating Mass (ERM) Motors

**Characteristics**:
- **Principle**: Unbalanced mass rotates, creating vibration
- **Frequency range**: 50-300 Hz typical
- **Amplitude**: Variable with voltage/PWM
- **Response time**: ~50-100ms to full amplitude
- **Cost**: Very low ($0.50-$2.00)
- **Power**: Moderate consumption
- **Control**: Simple PWM control

**Advantages**:
- Very low cost
- Simple control
- Good amplitude range
- Widely available

**Disadvantages**:
- Slower response time
- Less precise frequency control
- Mechanical wear over time
- Limited frequency range

**Applications**:
- Mobile phone vibration
- Game controllers
- Wearable notifications
- Low-cost haptic systems

#### Linear Resonant Actuator (LRA)

**Characteristics**:
- **Principle**: Voice coil moves mass linearly at resonance
- **Frequency range**: Narrow band (~175 Hz typical)
- **Amplitude**: Variable with drive signal
- **Response time**: ~10-20ms (faster than ERM)
- **Cost**: Low ($1-$3)
- **Power**: Lower consumption than ERM
- **Control**: Requires driver IC (e.g., DRV2605)

**Advantages**:
- Faster response
- More precise control
- Lower power consumption
- Better frequency control

**Disadvantages**:
- Higher cost than ERM
- Requires driver IC
- Narrow frequency range
- Less amplitude range

**Applications**:
- Premium mobile devices
- Apple Watch haptics
- High-quality wearables
- Precise haptic feedback

### Other Actuator Technologies

#### Piezoelectric Actuators

**Characteristics**:
- **Principle**: Piezoelectric material deforms with voltage
- **Frequency range**: Very wide (DC to kHz)
- **Amplitude**: Small displacement
- **Response time**: Very fast (<1ms)
- **Cost**: Moderate to high
- **Power**: Low consumption
- **Control**: Requires high voltage driver

**Advantages**:
- Very fast response
- Wide frequency range
- Precise control
- Low power

**Disadvantages**:
- Higher cost
- Complex drive circuitry
- Small displacement
- High voltage required

#### Electrotactile Stimulation

**Characteristics**:
- **Principle**: Electrical current stimulates nerves
- **Frequency range**: 1-1000 Hz
- **Intensity**: Current amplitude (mA range)
- **Response time**: Instantaneous
- **Cost**: Low (electrodes + driver)
- **Power**: Very low
- **Control**: Current-controlled driver

**Advantages**:
- Very fast response
- Precise control
- Low power
- Can encode frequency/intensity

**Disadvantages**:
- Safety concerns (electrical)
- Skin irritation possible
- Individual variation in sensitivity
- Requires good electrode contact

#### Pneumatic Actuators

**Characteristics**:
- **Principle**: Air pressure creates force/displacement
- **Frequency range**: Limited by air flow
- **Amplitude**: Large displacement possible
- **Response time**: Moderate (50-200ms)
- **Cost**: Moderate (pump + valves + actuators)
- **Power**: High (compressor)
- **Control**: Valves and pressure regulation

**Advantages**:
- Large forces possible
- Comfortable (air pressure)
- Good for pressure patterns

**Disadvantages**:
- Bulky (compressor needed)
- High power consumption
- Slower response
- Complex system

### Recommendation for Teletypathy

**Primary Choice: LRA Motors**
- Fast response time (10-20ms) supports <10ms latency goal
- Precise control for pattern encoding
- Lower power than ERM
- Good balance of cost and performance

**Alternative: ERM Motors**
- If cost is primary constraint
- Acceptable for initial prototypes
- Can upgrade to LRA later

## Haptic Pattern Design

### Temporal Patterns

#### Pulse Patterns
- **Single pulse**: On/off pattern
- **Double pulse**: Two pulses with gap
- **Triple pulse**: Three pulses
- **Rhythm patterns**: Complex timing sequences

#### Timing Parameters
- **Pulse duration**: 50-500ms typical
- **Inter-pulse interval**: 50-200ms
- **Pattern duration**: 200-2000ms
- **Repetition rate**: 1-5 Hz for alerts

### Spatial Patterns

#### Single Actuator
- **Location**: One motor at specific position
- **Pattern**: Temporal only
- **Simplicity**: Easiest to recognize
- **Information**: Limited to timing

#### Multi-Actuator Sequential
- **Sequence**: Patterns across multiple actuators
- **Movement**: Creates sense of motion
- **Information**: Location + timing
- **Complexity**: Moderate

#### Multi-Actuator Simultaneous
- **Parallel**: Multiple actuators at once
- **Spatial pattern**: Shape/configuration
- **Information**: High density
- **Complexity**: High recognition challenge

### Intensity Patterns

#### Amplitude Modulation
- **Variable strength**: Different vibration intensities
- **Discrimination**: ~20% difference detectable
- **Range**: 0.1-10 m/s² comfortable
- **Control**: PWM duty cycle or drive voltage

#### Frequency Modulation
- **Variable frequency**: Different vibration frequencies
- **Discrimination**: Limited (narrow range for ERM/LRA)
- **Range**: 50-300 Hz typical
- **Control**: Drive frequency (LRA) or fixed (ERM)

## Best Practices

### Pattern Recognition

#### Minimum Duration
- **Detection**: ~50ms minimum pulse
- **Recognition**: ~200ms for simple patterns
- **Complex patterns**: 500-1000ms
- **Recommendation**: 100-300ms per pattern element

#### Spacing
- **Between pulses**: ~50ms minimum
- **Between patterns**: ~100-200ms recommended
- **Word boundaries**: ~300-500ms for clarity
- **Recommendation**: 150ms inter-pattern spacing

#### Complexity
- **Simple patterns**: 1-2 dimensions (time + location)
- **Moderate patterns**: 2-3 dimensions
- **Complex patterns**: 3-4 dimensions maximum
- **Recommendation**: Start simple, add complexity gradually

### User Comfort

#### Intensity Levels
- **Minimum**: Just above detection threshold
- **Comfortable**: 0.5-2.0 m/s²
- **Maximum**: ~5 m/s² (varies by user)
- **Recommendation**: User-adjustable intensity

#### Duration Limits
- **Continuous**: Fatigue after 30-60 seconds
- **Patterns**: Comfortable for longer periods
- **Breaks**: Important for extended use
- **Recommendation**: Pattern-based, not continuous

#### Skin Contact
- **Pressure**: Light contact sufficient
- **Movement**: Secure attachment prevents irritation
- **Materials**: Skin-friendly materials important
- **Recommendation**: Comfortable wearable design

## Existing Haptic Systems

### Mobile Devices

#### iPhone Haptics
- **Actuator**: Taptic Engine (LRA)
- **Patterns**: System-defined library
- **Control**: Haptic Feedback API
- **Performance**: <10ms response time

#### Android Haptics
- **Actuator**: Varies by device (ERM/LRA)
- **Patterns**: VibrationEffect API
- **Control**: Vibration API
- **Performance**: Varies by device

### Gaming Controllers

#### PlayStation DualSense
- **Actuators**: Dual LRAs
- **Features**: Adaptive triggers, haptic feedback
- **Patterns**: Game-specific patterns
- **Performance**: Very responsive

#### Xbox Controller
- **Actuators**: ERM motors
- **Features**: Rumble feedback
- **Patterns**: Intensity-based
- **Performance**: Good for gaming

### Wearable Devices

#### Apple Watch
- **Actuator**: Taptic Engine (LRA)
- **Features**: Notification patterns, haptic alerts
- **Patterns**: Rich pattern library
- **Performance**: Excellent response time

#### Fitbit Devices
- **Actuators**: ERM motors
- **Features**: Activity alerts, notifications
- **Patterns**: Simple patterns
- **Performance**: Adequate for notifications

## Recommendations for Teletypathy

### Actuator Selection
1. **Primary**: LRA motors with DRV2605 driver
2. **Count**: 4-8 actuators for spatial encoding
3. **Placement**: Optimal spacing (~40-50mm)
4. **Control**: PWM with driver IC for precision

### Pattern Design
1. **Start simple**: Single actuator, temporal patterns
2. **Add spatial**: Multi-actuator sequential patterns
3. **Optimize timing**: 100-300ms per element
4. **Clear boundaries**: 150ms spacing between patterns

### System Design
1. **Low latency**: <10ms end-to-end target
2. **Precise timing**: Hardware timer-based control
3. **User control**: Adjustable intensity and speed
4. **Comfort**: Ergonomic wearable design

## References

### Haptic Interfaces and Devices
1. Hayward, V., Astley, O. R., Cruz-Hernandez, M., Grant, D., & Robles-De-La-Torre, G. (2004). Haptic interfaces and devices. *Sensor Review*, 24(1), 16-29. https://doi.org/10.1108/02602280410515818
2. Jones, L. A., & Sarter, N. B. (2008). Tactile displays: Guidance for their design and application. *Human Factors*, 50(1), 90-111. https://doi.org/10.1518/001872008X250638
3. ISO 9241-910:2011. *Ergonomics of human-system interaction — Part 910: Framework for tactile and haptic interactions*. International Organization for Standardization.

### Vibration Motor Technologies
4. Precision Microdrives. (2023). *ERM vs LRA: A Comparison Guide*. Precision Microdrives Ltd. https://www.precisionmicrodrives.com/
5. Texas Instruments. (2015). *DRV2605 Haptic Driver for ERM and LRA*. TI Datasheet SLOS773C.
6. Texas Instruments. (2015). *DRV2605 Application Report: Haptic Driver ICs*. TI Application Report SLOA193.

### Tactile Pattern Design
7. Cholewiak, R. W., & Collins, A. A. (2003). Vibrotactile localization on the arm: Effects of place, space, and age. *Perception & Psychophysics*, 65(7), 1058-1077. https://doi.org/10.3758/BF03194834
8. Van Erp, J. B., & Van Veen, H. A. (2004). Vibrotactile in-vehicle navigation system. *Transportation Research Part F: Traffic Psychology and Behaviour*, 7(4-5), 247-256. https://doi.org/10.1016/j.trf.2004.09.003
9. Jones, L. A., & Lederman, S. J. (2006). *Human Hand Function*. Oxford University Press.

### Haptic Feedback in Mobile Devices
10. Apple Inc. (2019). *Human Interface Guidelines: Haptics*. Apple Developer Documentation.
11. Google. (2023). *Android Haptics: VibrationEffect API*. Android Developer Documentation.
12. Pielot, M., & Boll, S. (2010). Tactile wayfinder: A non-visual support system for wayfinding. *Proceedings of the 5th Nordic Conference on Human-Computer Interaction* (NordiCHI '10), 157-166. https://doi.org/10.1145/1868914.1868936

### Gaming Controllers
13. Sony Interactive Entertainment. (2020). *DualSense Wireless Controller Technical Specifications*. Sony.
14. Microsoft Corporation. (2020). *Xbox Wireless Controller Specifications*. Microsoft.

### Wearable Haptic Devices
15. Apple Inc. (2015). *Apple Watch Human Interface Guidelines: Haptics*. Apple Developer Documentation.
16. Fitbit Inc. (2023). *Fitbit Device Specifications*. Fitbit Developer Documentation.

### Tactile Perception and Thresholds
17. Weinstein, S. (1968). Intensive and extensive aspects of tactile sensitivity as a function of body part, sex, and laterality. In D. R. Kenshalo (Ed.), *The Skin Senses* (pp. 195-222). Charles C. Thomas.
18. Van Boven, R. W., & Johnson, K. O. (1994). The limit of tactile spatial resolution in humans: Grating orientation discrimination with the finger pad and its relation to innervation density. *Journal of Neuroscience*, 14(5), 2825-2835. https://doi.org/10.1523/JNEUROSCI.14-05-02825.1994
19. Cholewiak, R. W., & Witteveen, H. (2008). Vibrotactile pattern recognition on the arm and torso. *Proceedings of the 10th International Conference on Haptics* (EuroHaptics '08), 90-99.

### Haptic Pattern Recognition
20. Tan, H. Z., Durlach, N. I., Reed, C. M., & Rabinowitz, W. M. (1999). Optimum information transfer rates for communication through haptic and other sensory modalities. *IEEE Transactions on Haptics*, 2(2), 84-95. https://doi.org/10.1109/TOH.2009.3
21. Geldard, F. A. (1960). Some neglected possibilities of communication. *Science*, 131(3413), 1583-1588. https://doi.org/10.1126/science.131.3413.1583

### User Comfort and Safety
22. ISO 9241-910:2011. *Ergonomics of human-system interaction — Part 910: Framework for tactile and haptic interactions*. International Organization for Standardization.
23. Pasquero, J., Hayward, V., & Smith, J. (2006). Haptic interfaces: A study of their potential for improving communication. *Proceedings of the 14th International Conference on Haptics* (EuroHaptics '06), 1-8.

## Related Documents

- [Actuator Technologies Research](actuator_technologies.md)
- [Latency Optimization Research](latency_optimization.md)
- [HCI Systems Research](hci_systems.md)

