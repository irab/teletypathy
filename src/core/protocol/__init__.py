"""Protocol module for Teletypathy communication."""

from .message import (
    Message,
    MessageType,
    PatternMessage,
    PatternBatchMessage,
    ConfigMessage,
    StatusResponseMessage,
    ErrorMessage,
    ConfigType,
    ErrorCode
)

__all__ = [
    'Message',
    'MessageType',
    'PatternMessage',
    'PatternBatchMessage',
    'ConfigMessage',
    'StatusResponseMessage',
    'ErrorMessage',
    'ConfigType',
    'ErrorCode'
]


