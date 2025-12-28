# DRV2605 Technical Note: Multiple Motor Control

## Overview

Clarification on DRV2605 capabilities for driving multiple LRA motors.

## Key Finding

**A single DRV2605 can drive only ONE LRA motor at a time.**

The DRV2605 is designed as a single-channel haptic driver. Each DRV2605 IC can control one actuator (LRA, ERM, or piezo) simultaneously.

## Implications for Teletypathy Design

### Current Design (8 Motors)

**Requirement**: 8 LRA motors for spatial encoding

**Solution**: **8 DRV2605 drivers** (one per motor)

**Configuration**:
- Each DRV2605 needs unique I2C address
- Base address: 0x5A
- Address range: 0x5A-0x5D (4 addresses with ADDR pins)
- **Problem**: Only 4 addresses available with ADDR pins

**I2C Address Options**:
1. **Use I2C multiplexer**: TCA9548A (8-channel) to create multiple I2C buses
2. **Use different I2C addresses**: If DRV2605 supports more than 4 addresses
3. **Sequential control**: Drive motors sequentially (not simultaneously)
4. **Alternative driver**: Consider drivers with more address options

### Cost Impact

**Current Design**:
- 8 × DRV2605: $8-16 (at $1-2 each)
- I2C multiplexer (if needed): ~$1-2
- **Total driver cost**: $9-18

**Alternative Approaches**:

#### Option 1: Analog Multiplexer + Single DRV2605
- **1 × DRV2605**: $1-2
- **Analog switches/multiplexer**: ~$2-5
- **Complexity**: Higher (need switching control)
- **Limitation**: Can only drive one motor at a time
- **Cost savings**: $6-13
- **Trade-off**: Cannot drive motors simultaneously

#### Option 2: Multiple DRV2605 with I2C Multiplexer
- **8 × DRV2605**: $8-16
- **I2C multiplexer (TCA9548A)**: ~$1-2
- **Complexity**: Moderate
- **Capability**: Can drive all motors simultaneously
- **Total cost**: $9-18

#### Option 3: Direct PWM Control (ERM only)
- **No drivers needed**: $0
- **Direct ESP32 PWM**: Free (built-in)
- **Limitation**: ERM motors only (slower response)
- **Trade-off**: Cannot achieve <10ms latency target

## I2C Bus Considerations

### Bandwidth Analysis

**I2C Speed**:
- Standard mode: 100 kHz
- Fast mode: 400 kHz (recommended for DRV2605)
- Fast mode plus: 1 MHz (if supported)

**DRV2605 Communication**:
- I2C write: ~2-3 bytes (register + data)
- Time per write: ~10-30 μs at 400 kHz
- 8 simultaneous commands: ~80-240 μs total

**Conclusion**: I2C bandwidth should be sufficient for 8 simultaneous commands at 400 kHz.

### Address Configuration

**DRV2605 Address Pins**:
- ADDR0, ADDR1 pins (if available)
- Base address: 0x5A
- Possible addresses: 0x5A, 0x5B, 0x5C, 0x5D (4 addresses)

**Problem**: Need 8 addresses for 8 motors

**Solutions**:
1. **I2C Multiplexer**: TCA9548A provides 8 channels, each with full I2C bus
2. **Check datasheet**: Verify if DRV2605 supports more address options
3. **Alternative drivers**: Consider drivers with more address options

## Simultaneous vs Sequential Control

### Simultaneous Control (Current Design)

**Capability**: Drive all 8 motors simultaneously
**Requirement**: 8 DRV2605 drivers
**Cost**: Higher ($8-16)
**Complexity**: I2C address management

**Use Case**: Patterns requiring simultaneous activation (e.g., letter X, period)

### Sequential Control (Alternative)

**Capability**: Drive motors one at a time
**Requirement**: 1 DRV2605 + analog multiplexer
**Cost**: Lower ($3-7)
**Complexity**: Switching control logic

**Limitation**: Cannot create simultaneous patterns
**Trade-off**: Simpler patterns, lower cost

## Recommendations

### For Teletypathy System

**Recommended**: **8 DRV2605 drivers** (one per motor)

**Rationale**:
1. **Simultaneous control**: Required for spatial patterns
2. **Pattern flexibility**: Can create complex simultaneous patterns
3. **Performance**: No switching delays
4. **Simplicity**: Each motor independently controlled

**Implementation**:
- Use I2C multiplexer (TCA9548A) if address conflicts
- Or verify DRV2605 address configuration options
- Configure unique I2C address for each driver

### Cost Optimization (If Needed)

If cost is critical constraint:
1. **Reduce motor count**: 4-6 motors instead of 8
2. **Use ERM motors**: Direct PWM, no drivers needed
3. **Sequential control**: 1 DRV2605 + multiplexer (loses simultaneous capability)

## References

1. Texas Instruments. (2015). *DRV2605 Haptic Driver for ERM and LRA*. TI Datasheet SLOS773C. https://www.ti.com/lit/ds/symlink/drv2605.pdf
2. Texas Instruments. (2015). *DRV2605 Application Report: Haptic Driver ICs*. TI Application Report SLOA193. https://www.ti.com/lit/an/sloa193/sloa193.pdf
3. Texas Instruments. (2023). *TCA9548A Low-Voltage 8-Channel I2C Switch*. TI Datasheet. https://www.ti.com/lit/ds/symlink/tca9548a.pdf

## Related Documents

- [Actuator Technologies Research](actuator_technologies.md)
- [Hardware Architecture](../hardware/architecture.md)
- [Research Gaps and Issues](gaps_and_issues.md)
- [Driver Comparison: Multi-Channel vs Direct PWM](driver_comparison.md)

