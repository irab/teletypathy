#!/usr/bin/env python3
"""
Protocol example for Teletypathy.

Demonstrates how to create and serialize protocol messages.
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.core.encoding import PatternEncoder
from src.core.protocol import (
    PatternMessage,
    PatternBatchMessage,
    ConfigMessage,
    StatusResponseMessage,
    ErrorMessage,
    Message,
    MessageType,
    ConfigType,
    ErrorCode
)


def main():
    """Main example function."""
    print("Teletypathy Protocol Example")
    print("=" * 40)
    
    encoder = PatternEncoder()
    
    # Example 1: Create and serialize pattern message
    print("\n1. Creating pattern message for 'E':")
    pattern = encoder.encode_character('E')
    if pattern:
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
        print(f"   Message type: {MessageType.PATTERN}")
        print(f"   Serialized size: {len(data)} bytes")
        print(f"   Data: {data.hex()}")
    
    # Example 2: Deserialize message
    print("\n2. Deserializing message:")
    deserialized = Message.deserialize(data)
    if deserialized:
        print(f"   Message type: {deserialized.msg_type}")
        print(f"   Payload length: {len(deserialized.payload)} bytes")
        if deserialized.msg_type == MessageType.PATTERN:
            char, events = PatternMessage.deserialize_pattern(deserialized.payload)
            print(f"   Character: '{char}'")
            print(f"   Events: {len(events)}")
    
    # Example 3: Batch message
    print("\n3. Creating batch message for 'HELLO':")
    text = "HELLO"
    patterns_list = []
    for char in text:
        pattern = encoder.encode_character(char)
        if pattern:
            events = [
                {
                    'actuator': event.actuator_id,
                    'time_offset': event.time_offset_ms,
                    'duration': event.duration_ms,
                    'intensity': event.intensity
                }
                for event in pattern.events
            ]
            patterns_list.append((char, events))
    
    batch_message = PatternBatchMessage(patterns_list)
    batch_data = batch_message.serialize()
    print(f"   Batch message size: {len(batch_data)} bytes")
    print(f"   Patterns in batch: {len(patterns_list)}")
    
    # Example 4: Configuration message
    print("\n4. Creating configuration message:")
    config_message = ConfigMessage(ConfigType.INTENSITY, 200)
    config_data = config_message.serialize()
    print(f"   Config type: {ConfigType.INTENSITY}")
    print(f"   Value: 200")
    print(f"   Serialized size: {len(config_data)} bytes")
    
    # Example 5: Status response message
    print("\n5. Creating status response message:")
    status_message = StatusResponseMessage(
        battery_level=80,
        connection_quality=-50,
        error_code=0,
        queue_length=5
    )
    status_data = status_message.serialize()
    print(f"   Battery: 80%")
    print(f"   Queue length: 5")
    print(f"   Serialized size: {len(status_data)} bytes")
    
    # Example 6: Error message
    print("\n6. Creating error message:")
    error_message = ErrorMessage(ErrorCode.QUEUE_FULL, "Queue is full")
    error_data = error_message.serialize()
    print(f"   Error code: {ErrorCode.QUEUE_FULL}")
    print(f"   Message: 'Queue is full'")
    print(f"   Serialized size: {len(error_data)} bytes")
    
    print("\n" + "=" * 40)
    print("Example complete!")


if __name__ == '__main__':
    main()


