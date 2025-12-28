# Data Flow Diagram

## Overview

Detailed data flow through the Teletypathy system from input to tactile output.

## Keystroke Flow

```
User Types 'E'
    │
    ▼
┌─────────────────┐
│ Keyboard Hook   │  <1ms
│ (OS-level)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Pattern Encoder │  <1ms
│ Character →     │
│ Pattern Lookup  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Message         │  <0.5ms
│ Serialization   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ BLE Transmission│  ~5ms
│ (Optimized)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ BLE Reception   │  ~0.5ms
│ (Device)        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Message         │  <0.5ms
│ Deserialization │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Pattern Queue   │  <0.5ms
│ (Add to queue)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Pattern         │  <2ms
│ Executor        │
│ (Timing control) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Motor Drivers    │  <1ms
│ (DRV2605)       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ LRA Motors      │  ~10-20ms
│ (Vibration)     │
└─────────────────┘

Total: ~10-30ms (target: <10ms)
```

## Text Message Flow

```
User Enters "HELLO"
    │
    ▼
┌─────────────────┐
│ Text Input      │
│ Processing      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Character       │
│ Iteration       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Pattern Encoder │  For each character
│ (Batch)         │  <1ms per char
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Pattern Batch   │  <1ms
│ Message         │
│ Creation        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ BLE Transmission│  ~5ms
│ (Batch message) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Pattern Queue   │  Patterns added
│ (Sequential)    │  sequentially
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Pattern         │  Execute each
│ Execution       │  pattern in order
│ (Sequential)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Tactile Output  │  User feels
│ (Sequential)    │  pattern sequence
└─────────────────┘
```

## Pattern Queue Flow

```
Pattern Received
    │
    ▼
┌─────────────────┐
│ Queue Check      │
│ (Space available?)│
└────────┬────────┘
         │
    ┌────┴────┐
    │        │
   Yes      No
    │        │
    │        ▼
    │   ┌──────────────┐
    │   │ Wait/Reject  │
    │   └──────────────┘
    │
    ▼
┌─────────────────┐
│ Add to Queue    │
│ (FIFO)          │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Queue Monitor   │
│ (Non-empty?)    │
└────────┬────────┘
         │
    ┌────┴────┐
    │        │
   Yes      No
    │        │
    │        ▼
    │   ┌──────────────┐
    │   │ Wait for     │
    │   │ Pattern      │
    │   └──────────────┘
    │
    ▼
┌─────────────────┐
│ Dequeue Pattern │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Execute Pattern │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Check Queue     │
│ (More patterns?)│
└─────────────────┘
```

## Latency Breakdown

### Target: <10ms End-to-End

| Stage | Target | Notes |
|-------|--------|-------|
| Input capture | <1ms | OS-level, very fast |
| Pattern generation | <1ms | Lookup table, O(1) |
| Protocol serialization | <0.5ms | Simple binary format |
| BLE transmission | <5ms | Optimized BLE parameters |
| BLE reception | <0.5ms | Device-side reception |
| Protocol deserialization | <0.5ms | Simple parsing |
| Pattern queue | <0.5ms | Add to queue |
| Pattern execution | <2ms | Hardware timer control |
| Motor response | <1ms | LRA startup time |
| **Total** | **<10ms** | **Target achieved** |

### Current Estimates (To Be Measured)

| Stage | Estimate | Status |
|-------|----------|--------|
| Input capture | <1ms | ✅ Achievable |
| Pattern generation | <1ms | ✅ Achievable |
| Protocol serialization | <0.5ms | ✅ Achievable |
| BLE transmission | 5-10ms | ⚠️ Needs optimization |
| BLE reception | <1ms | ✅ Achievable |
| Protocol deserialization | <0.5ms | ✅ Achievable |
| Pattern queue | <0.5ms | ✅ Achievable |
| Pattern execution | 2-5ms | ⚠️ Needs optimization |
| Motor response | 10-20ms | ⚠️ LRA response time |
| **Total** | **20-40ms** | **Needs optimization** |

## Optimization Strategies

### Latency Optimization

1. **BLE Optimization**:
   - 7.5ms connection interval (minimum)
   - No slave latency
   - Maximum MTU size
   - Write Without Response (no ACK)

2. **Pattern Execution**:
   - Hardware timers for precise timing
   - Pre-computed pattern timing
   - Parallel motor control
   - Immediate pattern start

3. **Queue Management**:
   - Minimal queue overhead
   - Fast dequeuing
   - Efficient pattern storage

### Throughput Optimization

1. **Pattern Batching**:
   - Send multiple patterns in one message
   - Reduce BLE overhead
   - Increase effective throughput

2. **Queue Management**:
   - Larger queue capacity
   - Efficient queue operations
   - Pre-queue patterns when possible

## Related Documents

- [System Overview](system_overview.md): High-level architecture
- [Component Diagram](component_diagram.md): Component details
- [Protocol Specification](../design/protocol_spec.md): Message format


