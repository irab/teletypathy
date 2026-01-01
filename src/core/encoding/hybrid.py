"""
Hybrid encoding system combining character and phoneme modes.

Automatically selects the best encoding mode based on content type.
"""

from typing import List, Optional
from .pattern import Pattern
from .pattern import PatternEncoder as LetterEncoder
from .phoneme import PhonemeEncoder


class HybridEncoder:
    """
    Hybrid encoder that automatically switches between character and phoneme modes.
    
    Strategy:
    - Words: Use phoneme mode (faster, more efficient)
    - Non-words: Use character mode (code, URLs, numbers, punctuation)
    - Unknown words: Fallback to character mode if G2P fails
    """
    
    def __init__(self, strategy: str = 'adaptive'):
        """
        Initialize hybrid encoder.
        
        Args:
            strategy: Encoding strategy
                - 'adaptive': Automatic mode switching (recommended)
                - 'character': Always character mode
                - 'phoneme': Always phoneme mode
                - 'word_level': Phoneme for common words, character for rare
        """
        self.strategy = strategy
        self.letter_encoder = LetterEncoder()
        self.phoneme_encoder = PhonemeEncoder()
        
        # Common words for word-level strategy
        self.common_words = {
            'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'it',
            'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this',
            'but', 'his', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an',
            'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so',
            'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when',
            'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take',
            'people', 'into', 'year', 'your', 'good', 'some', 'could', 'them',
            'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its',
            'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our',
            'work', 'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any',
            'these', 'give', 'day', 'most', 'us'
        }
    
    def encode_text(self, text: str) -> List[Pattern]:
        """
        Encode text using hybrid strategy.
        
        Args:
            text: Text string to encode
            
        Returns:
            List of Pattern objects
        """
        if self.strategy == 'character':
            return self.letter_encoder.encode_text(text)
        elif self.strategy == 'phoneme':
            return self.phoneme_encoder.encode_text(text)
        elif self.strategy == 'adaptive':
            return self._encode_adaptive(text)
        elif self.strategy == 'word_level':
            return self._encode_word_level(text)
        else:
            # Default to adaptive
            return self._encode_adaptive(text)
    
    def _encode_adaptive(self, text: str) -> List[Pattern]:
        """
        Adaptive encoding: automatically switch modes based on content.
        
        Strategy:
        - Words: Try phoneme mode, fallback to character if G2P fails
        - Non-words: Always character mode
        """
        # Split into words and non-words
        import re
        tokens = re.split(r'(\s+)', text)  # Split but keep spaces
        
        patterns = []
        for token in tokens:
            if not token.strip():  # Empty or whitespace
                # Add space pattern
                space_pattern = self.letter_encoder.encode_character(' ')
                if space_pattern:
                    patterns.append(space_pattern)
                continue
            
            if self._is_word(token):
                # Try phoneme mode
                try:
                    phoneme_patterns = self.phoneme_encoder.encode_text(token)
                    # Check if we got valid patterns
                    if phoneme_patterns and len(phoneme_patterns) > 0:
                        patterns.extend(phoneme_patterns)
                    else:
                        # Fallback to character mode
                        char_patterns = self.letter_encoder.encode_text(token)
                        patterns.extend(char_patterns)
                except Exception:
                    # G2P failed - use character mode
                    char_patterns = self.letter_encoder.encode_text(token)
                    patterns.extend(char_patterns)
            else:
                # Non-word (code, URL, number, etc.) - use character mode
                char_patterns = self.letter_encoder.encode_text(token)
                patterns.extend(char_patterns)
        
        return patterns
    
    def _encode_word_level(self, text: str) -> List[Pattern]:
        """
        Word-level hybrid: phoneme for common words, character for rare.
        
        Strategy:
        - Common words: Use phoneme mode
        - Rare/unknown words: Use character mode
        """
        import re
        tokens = re.split(r'(\s+)', text)
        
        patterns = []
        for token in tokens:
            if not token.strip():
                space_pattern = self.letter_encoder.encode_character(' ')
                if space_pattern:
                    patterns.append(space_pattern)
                continue
            
            word_lower = token.lower().strip('.,!?;:')
            
            if word_lower in self.common_words:
                # Common word - use phoneme mode
                try:
                    phoneme_patterns = self.phoneme_encoder.encode_text(token)
                    if phoneme_patterns:
                        patterns.extend(phoneme_patterns)
                    else:
                        patterns.extend(self.letter_encoder.encode_text(token))
                except Exception:
                    patterns.extend(self.letter_encoder.encode_text(token))
            else:
                # Rare/unknown word - use character mode
                patterns.extend(self.letter_encoder.encode_text(token))
        
        return patterns
    
    def _is_word(self, text: str) -> bool:
        """
        Check if text is a real word (not code, URL, etc.).
        
        Args:
            text: Text to check
            
        Returns:
            True if text appears to be a word
        """
        # Remove punctuation
        cleaned = text.strip('.,!?;:')
        
        # Check if all alphabetic (allow apostrophes)
        if not cleaned.replace("'", "").replace("-", "").isalpha():
            return False
        
        # Check if it's a URL/code pattern
        if any(char in cleaned for char in ['/', ':', '@', '#', '$', '\\']):
            return False
        
        # Check if it's a number
        if cleaned.isdigit():
            return False
        
        # Check if it's mostly numbers (e.g., "3D", "2nd")
        if len(cleaned) > 1 and sum(c.isdigit() for c in cleaned) > len(cleaned) / 2:
            return False
        
        return True
    
    def set_strategy(self, strategy: str):
        """Change encoding strategy."""
        self.strategy = strategy
    
    def get_strategy(self) -> str:
        """Get current encoding strategy."""
        return self.strategy

