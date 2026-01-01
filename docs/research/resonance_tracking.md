# Resonance Tracking: What It Is and Why It Matters

## Overview

Explanation of resonance tracking for LRA motors and its relevance to the Teletypathy project.

## What Is Resonance Tracking?

### Basic Concept

**Resonance tracking** is an automatic process that detects and adjusts to the optimal resonant frequency of a Linear Resonant Actuator (LRA) motor in real-time.

### How LRA Motors Work

**LRA Physics**:
- LRA motors have a **mechanical resonance frequency** (typically ~175 Hz)
- At resonance, the motor achieves **maximum vibration amplitude** with **minimum energy input**
- Operating off-resonance reduces amplitude and increases power consumption

**Resonance Characteristics**:
- **Narrow band**: Optimal performance within ~5-10 Hz of resonance
- **Peak efficiency**: At resonance, amplitude is 2-3x higher than off-resonance
- **Power efficiency**: At resonance, power consumption is significantly lower

### The Problem: Resonance Frequency Varies

**Why Resonance Changes**:

1. **Manufacturing Tolerances**
   - Each LRA has slightly different resonance frequency
   - Typical range: 150-200 Hz, but individual motors vary
   - Example: Motor A = 172 Hz, Motor B = 178 Hz

2. **Temperature Effects**
   - Resonance frequency shifts with temperature
   - Typical drift: ~0.1-0.5 Hz per °C
   - Example: 175 Hz at 20°C → 173 Hz at 40°C

3. **Aging and Wear**
   - Mechanical properties change over time
   - Resonance frequency can drift with use
   - Example: 175 Hz initially → 173 Hz after months of use

4. **Mounting Conditions**
   - How motor is attached affects resonance
   - Stiffness of mounting changes frequency
   - Example: Different enclosure materials affect resonance

**Impact of Frequency Mismatch**:
- **10 Hz off-resonance**: ~30-50% amplitude reduction
- **20 Hz off-resonance**: ~50-70% amplitude reduction
- **Power consumption**: Increases significantly off-resonance
- **User experience**: Inconsistent vibration strength

## How Resonance Tracking Works

### Automatic Detection

**DRV2605 Method**:
1. **Back-EMF Detection**: Monitors back electromotive force from LRA
2. **Frequency Sweep**: Tests different frequencies to find peak response
3. **Peak Detection**: Identifies frequency with maximum amplitude
4. **Continuous Monitoring**: Periodically re-checks and adjusts

**Process**:
```
1. Driver sends test signal at different frequencies
2. Measures LRA response (back-EMF or current)
3. Identifies frequency with maximum response
4. Sets drive frequency to detected resonance
5. Periodically re-checks (every few seconds or on command)
```

### Manual Alternative (Without Tracking)

**Fixed Frequency Approach**:
- Set drive frequency to nominal value (e.g., 175 Hz)
- Assume all motors match specification
- **Problem**: Motors vary, frequency drifts

**Calibration Approach**:
- Manually measure each motor's resonance frequency
- Store frequency in firmware/config
- **Problem**: Doesn't account for temperature/aging drift
- **Problem**: Requires calibration equipment and process

**Feedback-Based Approach**:
- Use accelerometer to measure vibration amplitude
- Adjust frequency to maximize amplitude
- **Problem**: Adds cost and complexity (accelerometer per motor)
- **Problem**: Requires calibration algorithm

## Why Resonance Tracking Matters

### Performance Benefits

#### 1. Consistent Vibration Strength
- **Without tracking**: Vibration strength varies between motors and conditions
- **With tracking**: Consistent amplitude across all motors and conditions
- **Impact**: Reliable tactile patterns, consistent user experience

#### 2. Maximum Efficiency
- **Without tracking**: Operating off-resonance wastes power
- **With tracking**: Always at peak efficiency
- **Impact**: Longer battery life, lower power consumption

#### 3. Optimal Amplitude
- **Without tracking**: May get 50-70% of maximum amplitude
- **With tracking**: Gets 100% of maximum amplitude
- **Impact**: Stronger, more noticeable vibrations

### Practical Benefits

#### 1. No Manual Calibration
- **Without tracking**: Must calibrate each motor individually
- **With tracking**: Automatic, no calibration needed
- **Impact**: Faster production, lower manufacturing cost

#### 2. Temperature Compensation
- **Without tracking**: Vibration strength changes with temperature
- **With tracking**: Automatically compensates for temperature
- **Impact**: Consistent performance in all conditions

#### 3. Aging Compensation
- **Without tracking**: Performance degrades over time
- **With tracking**: Automatically adjusts for aging
- **Impact**: Consistent performance over device lifetime

## Is Resonance Tracking Needed for Teletypathy?

### Analysis

#### Project Requirements

**Key Requirements**:
1. **Consistent patterns**: Each character should feel the same every time
2. **Multiple motors**: 8 motors, each may have different resonance
3. **Battery operation**: Power efficiency important
4. **Wearable**: Temperature varies (body heat, environment)
5. **Long-term use**: Device used over months/years

#### Without Resonance Tracking

**Problems**:
1. **Motor variation**: 8 motors with different resonance frequencies
   - Motor 0: 172 Hz
   - Motor 1: 178 Hz
   - Motor 2: 175 Hz
   - ... etc.
   - **Impact**: Different vibration strengths for same pattern

2. **Temperature effects**: Device warms up during use
   - Initial: 175 Hz (room temperature)
   - After 30 min: 173 Hz (warmed up)
   - **Impact**: Vibration strength decreases over time

3. **Inconsistent patterns**: Same character feels different
   - Pattern on Motor 0 (172 Hz): Strong vibration
   - Pattern on Motor 1 (178 Hz): Weak vibration (if driving at 175 Hz)
   - **Impact**: Pattern recognition becomes difficult

4. **Power waste**: Operating off-resonance
   - Higher current consumption
   - Shorter battery life
   - **Impact**: Reduced battery life, may need larger battery

#### With Resonance Tracking

**Benefits**:
1. **Consistent patterns**: All motors operate at optimal frequency
   - Each motor automatically tuned to its resonance
   - **Impact**: Consistent vibration strength across all motors

2. **Temperature compensation**: Automatically adjusts
   - As device warms, frequency adjusts
   - **Impact**: Consistent performance regardless of temperature

3. **Pattern reliability**: Same character always feels the same
   - Consistent amplitude across all conditions
   - **Impact**: Easier pattern recognition and learning

4. **Power efficiency**: Always at peak efficiency
   - Lower power consumption
   - **Impact**: Longer battery life

### Conclusion: **YES, Resonance Tracking Is Needed**

**Rationale**:
1. **Critical for consistency**: 8 motors with varying resonance need individual tuning
2. **Temperature compensation**: Wearable device experiences temperature changes
3. **Pattern recognition**: Consistent vibration strength essential for learning
4. **Power efficiency**: Important for battery operation
5. **No calibration needed**: Simplifies production and maintenance

**Without resonance tracking**:
- Would need manual calibration of each motor
- Would need temperature compensation algorithm
- Would have inconsistent vibration strength
- Would waste power
- **Result**: Poor user experience, unreliable patterns

## Implementation Options

### Option 1: DRV2605 (Automatic Tracking)

**How it works**:
- Built-in automatic resonance tracking
- Detects resonance on startup and periodically
- No firmware code needed (driver handles it)

**Benefits**:
- Automatic, no code required
- Handles all 8 motors independently
- Compensates for temperature and aging
- Proven, reliable solution

**Cost**: Included in DRV2605 ($1-2 per driver)

### Option 2: Direct PWM (Manual Tracking)

**How it would work**:
- Firmware measures resonance (back-EMF or accelerometer)
- Firmware adjusts PWM frequency
- Requires calibration algorithm

**Challenges**:
- Need to implement resonance detection algorithm
- Need feedback mechanism (back-EMF or accelerometer)
- Need calibration code for each motor
- Need temperature compensation algorithm
- Significant firmware complexity

**Cost**: Additional development time (weeks), possibly accelerometers

### Option 3: Fixed Frequency (No Tracking)

**How it would work**:
- Set all motors to nominal frequency (e.g., 175 Hz)
- Assume motors match specification

**Problems**:
- Motors vary (150-200 Hz range)
- Temperature drift
- Aging drift
- Inconsistent performance
- **Not recommended** for this project

## Recommendation

### Use DRV2605 with Automatic Resonance Tracking

**Why**:
1. **Automatic**: No firmware code needed
2. **Reliable**: Proven solution used in commercial products
3. **Independent**: Each motor tracked separately
4. **Comprehensive**: Handles all variation sources
5. **Cost-effective**: Included in driver cost ($1-2)

**Alternative (Direct PWM)**:
- Would require significant firmware development
- Would need feedback sensors (accelerometers) for reliable tracking
- Would add complexity and development time
- **Not worth the cost savings** ($8-17) given development effort

## Technical Details

### DRV2605 Resonance Tracking

**Process**:
1. **Initialization**: On startup, driver detects resonance
2. **Periodic updates**: Re-checks resonance periodically (configurable)
3. **On-demand**: Can trigger resonance detection via I2C command
4. **Automatic adjustment**: Driver adjusts drive frequency automatically

**Configuration**:
- Can enable/disable tracking
- Can set update frequency
- Can manually trigger detection
- Can read detected resonance frequency

**Performance**:
- Detection time: ~10-50ms
- Accuracy: ±1-2 Hz typical
- Update rate: Configurable (seconds to minutes)

### Direct PWM Implementation (If Needed)

**Would require**:
1. **Back-EMF measurement**: Measure voltage/current to detect resonance
2. **Frequency sweep**: Test different frequencies
3. **Peak detection**: Find frequency with maximum response
4. **Calibration storage**: Store frequency for each motor
5. **Temperature compensation**: Adjust for temperature changes
6. **Periodic re-calibration**: Re-check periodically

**Complexity**: High (weeks of development)

## References

1. Texas Instruments. (2015). *DRV2605 Haptic Driver for ERM and LRA*. TI Datasheet SLOS773C. https://www.ti.com/lit/ds/symlink/drv2605.pdf
2. Texas Instruments. (2015). *DRV2605 Application Report: Auto-Resonance Tracking*. TI Application Report.
3. Precision Microdrives. (2023). *LRA Resonance Frequency and Tracking*. Precision Microdrives Technical Notes.

## Related Documents

- [Driver Comparison](driver_comparison.md): DRV2605 vs Direct PWM
- [Actuator Technologies Research](actuator_technologies.md): LRA motor characteristics
- [DRV2605 Technical Note](drv2605_technical_note.md): Driver details



