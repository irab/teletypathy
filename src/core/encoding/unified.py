"""
Unified encoding interface supporting both letter-based and phoneme-based encoding.

Allows switching between encoding modes for different use cases.
"""

from typing import List, Optional
from enum import Enum
from .pattern import Pattern
from .pattern import PatternEncoder as LetterEncoder
from .phoneme import PhonemeEncoder


class EncodingMode(Enum):
    """Encoding mode selection."""
    LETTER = "letter"  # Letter-based encoding (character-by-character)
    PHONEME = "phoneme"  # Phoneme-based encoding (speech sounds)


class UnifiedEncoder:
    """
    Unified encoder supporting both letter-based and phoneme-based encoding.
    
    Based on research:
    - Letter-based: Skin Reading (2016) - good for learning, spelling
    - Phoneme-based: TAPS (2020) - faster word recognition, 500 words learned
    """
    
    def __init__(self, mode: EncodingMode = EncodingMode.LETTER):
        """
        Initialize unified encoder.
        
        Args:
            mode: Encoding mode (LETTER or PHONEME)
        """
        self.mode = mode
        self.letter_encoder = LetterEncoder()
        self.phoneme_encoder = PhonemeEncoder()
    
    def set_mode(self, mode: EncodingMode):
        """Change encoding mode."""
        self.mode = mode
    
    def encode_text(self, text: str) -> List[Pattern]:
        """
        Encode text into tactile patterns based on current mode.
        
        Args:
            text: Text string to encode
            
        Returns:
            List of Pattern objects
        """
        if self.mode == EncodingMode.LETTER:
            return self.letter_encoder.encode_text(text)
        else:  # PHONEME
            return self.phoneme_encoder.encode_text(text)
    
    def encode_character(self, char: str) -> Optional[Pattern]:
        """
        Encode a single character (letter mode only).
        
        Args:
            char: Character to encode
            
        Returns:
            Pattern object or None
        """
        if self.mode == EncodingMode.LETTER:
            return self.letter_encoder.encode_character(char)
        else:
            # In phoneme mode, convert character to phoneme first
            phonemes = self.phoneme_encoder.text_to_phonemes(char)
            if phonemes:
                return self.phoneme_encoder.encode_phoneme(phonemes[0])
            return None
    
    def get_mode(self) -> EncodingMode:
        """Get current encoding mode."""
        return self.mode
    
    def get_mode_name(self) -> str:
        """Get current encoding mode as string."""
        return self.mode.value

