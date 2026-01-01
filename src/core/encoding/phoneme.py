"""
Phoneme-based encoding library for Teletypathy.

Converts text to phonemes and encodes phonemes into tactile patterns,
based on TAPS (TActile Phonemic Sleeve) research methodology.
"""

from typing import List, Optional, Dict
from .pattern import Pattern, ActuatorEvent


class PhonemeEncoder:
    """Encodes text into phonemes and converts phonemes to tactile patterns."""
    
    def __init__(self):
        """Initialize phoneme encoder with phoneme-to-pattern mappings."""
        self.phoneme_map = self._build_phoneme_map()
        self.g2p_map = self._build_g2p_map()  # Basic grapheme-to-phoneme rules
    
    def encode_text(self, text: str) -> List[Pattern]:
        """
        Encode text string into phoneme patterns.
        
        Args:
            text: Text string to encode
            
        Returns:
            List of Pattern objects representing phonemes
        """
        # Convert text to phonemes
        phonemes = self.text_to_phonemes(text)
        
        # Convert phonemes to patterns
        patterns = []
        for phoneme in phonemes:
            pattern = self.encode_phoneme(phoneme)
            if pattern:
                patterns.append(pattern)
        
        return patterns
    
    def text_to_phonemes(self, text: str) -> List[str]:
        """
        Convert text to phoneme sequence.
        
        Uses basic rule-based G2P conversion. For production, consider
        using a library like espeak-ng or phonemizer.
        
        Args:
            text: Text string
            
        Returns:
            List of phoneme symbols (IPA notation)
        """
        text = text.lower().strip()
        phonemes = []
        
        i = 0
        while i < len(text):
            char = text[i]
            
            # Skip spaces (handled as pauses)
            if char == ' ':
                phonemes.append(' ')
                i += 1
                continue
            
            # Try multi-character graphemes first (trigrams, then bigrams)
            matched = False
            for length in [3, 2]:
                if i + length <= len(text):
                    ngram = text[i:i+length]
                    if ngram in self.g2p_map:
                        result = self.g2p_map[ngram]
                        # Handle multi-phoneme results (e.g., 'x' -> ['k', 's'])
                        if isinstance(result, list):
                            # List of phonemes
                            phonemes.extend([ph for ph in result if ph in self.phoneme_map])
                        elif isinstance(result, str):
                            if len(result) > 1 and result not in self.phoneme_map:
                                # Split into individual phonemes
                                for ph in result:
                                    if ph in self.phoneme_map:
                                        phonemes.append(ph)
                            else:
                                phonemes.append(result)
                        i += length
                        matched = True
                        break
            
            if not matched:
                # Single character mapping
                if char in self.g2p_map:
                    result = self.g2p_map[char]
                    # Handle multi-phoneme results
                    if isinstance(result, list):
                        # List of phonemes
                        phonemes.extend([ph for ph in result if ph in self.phoneme_map])
                    elif isinstance(result, str):
                        if len(result) > 1 and result not in self.phoneme_map:
                            # Split into individual phonemes
                            for ph in result:
                                if ph in self.phoneme_map:
                                    phonemes.append(ph)
                        else:
                            phonemes.append(result)
                else:
                    # Fallback: skip unknown characters
                    # In production, use proper G2P library
                    pass
                
                i += 1
        
        return phonemes
    
    def encode_phoneme(self, phoneme: str) -> Optional[Pattern]:
        """
        Encode a single phoneme into a tactile pattern.
        
        Args:
            phoneme: Phoneme symbol (IPA notation)
            
        Returns:
            Pattern object or None if phoneme not supported
        """
        if phoneme == ' ':
            # Space: no pattern (pause handled separately)
            return Pattern([])
        
        pattern_def = self.phoneme_map.get(phoneme)
        if pattern_def is None:
            return None
        
        return self._create_pattern(pattern_def)
    
    def _create_pattern(self, pattern_def: dict) -> Pattern:
        """Create Pattern object from pattern definition."""
        events = []
        for event_def in pattern_def.get('events', []):
            event = ActuatorEvent(
                actuator_id=event_def['actuator'],
                time_offset_ms=event_def['time_offset'],
                duration_ms=event_def['duration'],
                intensity=event_def.get('intensity', 200)
            )
            events.append(event)
        return Pattern(events)
    
    def _build_phoneme_map(self) -> Dict[str, dict]:
        """Build phoneme to pattern mapping dictionary."""
        
        # High-frequency consonants: single actuator, short pulse (120ms)
        patterns = {
            # Most common consonants
            'n': {'events': [{'actuator': 0, 'time_offset': 0, 'duration': 120}]},  # /n/
            't': {'events': [{'actuator': 1, 'time_offset': 0, 'duration': 120}]},  # /t/
            's': {'events': [{'actuator': 2, 'time_offset': 0, 'duration': 120}]},  # /s/
            'r': {'events': [{'actuator': 3, 'time_offset': 0, 'duration': 120}]},  # /r/
            'l': {'events': [{'actuator': 4, 'time_offset': 0, 'duration': 120}]},  # /l/
            
            # High-frequency vowels: single actuator, medium pulse (150ms)
            'ə': {'events': [{'actuator': 5, 'time_offset': 0, 'duration': 150}]},  # schwa
            'ɪ': {'events': [{'actuator': 6, 'time_offset': 0, 'duration': 150}]},  # /ɪ/
            'ɛ': {'events': [{'actuator': 7, 'time_offset': 0, 'duration': 150}]},  # /ɛ/
            
            # Medium-frequency consonants: two actuators, sequential
            'd': {'events': [
                {'actuator': 0, 'time_offset': 0, 'duration': 100},
                {'actuator': 1, 'time_offset': 150, 'duration': 100}
            ]},  # /d/
            'k': {'events': [
                {'actuator': 1, 'time_offset': 0, 'duration': 100},
                {'actuator': 2, 'time_offset': 150, 'duration': 100}
            ]},  # /k/
            'm': {'events': [
                {'actuator': 2, 'time_offset': 0, 'duration': 100},
                {'actuator': 3, 'time_offset': 150, 'duration': 100}
            ]},  # /m/
            'p': {'events': [
                {'actuator': 3, 'time_offset': 0, 'duration': 100},
                {'actuator': 4, 'time_offset': 150, 'duration': 100}
            ]},  # /p/
            'b': {'events': [
                {'actuator': 4, 'time_offset': 0, 'duration': 100},
                {'actuator': 5, 'time_offset': 150, 'duration': 100}
            ]},  # /b/
            'g': {'events': [
                {'actuator': 5, 'time_offset': 0, 'duration': 100},
                {'actuator': 6, 'time_offset': 150, 'duration': 100}
            ]},  # /g/
            
            # Fricatives: continuous patterns (200ms)
            'f': {'events': [{'actuator': 0, 'time_offset': 0, 'duration': 200}]},  # /f/
            'v': {'events': [{'actuator': 1, 'time_offset': 0, 'duration': 200}]},  # /v/
            'z': {'events': [{'actuator': 2, 'time_offset': 0, 'duration': 200}]},  # /z/
            'θ': {'events': [{'actuator': 3, 'time_offset': 0, 'duration': 200}]},  # /θ/ (th as in "think")
            'ð': {'events': [{'actuator': 4, 'time_offset': 0, 'duration': 200}]},  # /ð/ (th as in "this")
            
            # Complex consonants: multi-actuator patterns
            'ʃ': {'events': [  # /ʃ/ (sh)
                {'actuator': 0, 'time_offset': 0, 'duration': 150},
                {'actuator': 2, 'time_offset': 0, 'duration': 150}
            ]},
            'ʒ': {'events': [  # /ʒ/ (zh as in "measure")
                {'actuator': 1, 'time_offset': 0, 'duration': 150},
                {'actuator': 3, 'time_offset': 0, 'duration': 150}
            ]},
            'tʃ': {'events': [  # /tʃ/ (ch)
                {'actuator': 0, 'time_offset': 0, 'duration': 80},
                {'actuator': 1, 'time_offset': 120, 'duration': 80},
                {'actuator': 2, 'time_offset': 240, 'duration': 80}
            ]},
            'dʒ': {'events': [  # /dʒ/ (j as in "judge")
                {'actuator': 2, 'time_offset': 0, 'duration': 80},
                {'actuator': 1, 'time_offset': 120, 'duration': 80},
                {'actuator': 0, 'time_offset': 240, 'duration': 80}
            ]},
            'ŋ': {'events': [  # /ŋ/ (ng)
                {'actuator': 5, 'time_offset': 0, 'duration': 150},
                {'actuator': 6, 'time_offset': 0, 'duration': 150},
                {'actuator': 7, 'time_offset': 0, 'duration': 150}
            ]},
            
            # Vowels: longer patterns (three actuators)
            'æ': {'events': [  # /æ/ (a as in "cat")
                {'actuator': 0, 'time_offset': 0, 'duration': 100},
                {'actuator': 1, 'time_offset': 150, 'duration': 100},
                {'actuator': 2, 'time_offset': 300, 'duration': 100}
            ]},
            'ʌ': {'events': [  # /ʌ/ (u as in "cup")
                {'actuator': 1, 'time_offset': 0, 'duration': 100},
                {'actuator': 2, 'time_offset': 150, 'duration': 100},
                {'actuator': 3, 'time_offset': 300, 'duration': 100}
            ]},
            'ɑ': {'events': [  # /ɑ/ (a as in "father")
                {'actuator': 2, 'time_offset': 0, 'duration': 100},
                {'actuator': 3, 'time_offset': 150, 'duration': 100},
                {'actuator': 4, 'time_offset': 300, 'duration': 100}
            ]},
            'ɔ': {'events': [  # /ɔ/ (o as in "dog")
                {'actuator': 3, 'time_offset': 0, 'duration': 100},
                {'actuator': 4, 'time_offset': 150, 'duration': 100},
                {'actuator': 5, 'time_offset': 300, 'duration': 100}
            ]},
            'ʊ': {'events': [  # /ʊ/ (u as in "put")
                {'actuator': 4, 'time_offset': 0, 'duration': 100},
                {'actuator': 5, 'time_offset': 150, 'duration': 100},
                {'actuator': 6, 'time_offset': 300, 'duration': 100}
            ]},
            'u': {'events': [  # /u/ (u as in "blue")
                {'actuator': 5, 'time_offset': 0, 'duration': 100},
                {'actuator': 6, 'time_offset': 150, 'duration': 100},
                {'actuator': 7, 'time_offset': 300, 'duration': 100}
            ]},
            'i': {'events': [  # /i/ (ee as in "see")
                {'actuator': 6, 'time_offset': 0, 'duration': 100},
                {'actuator': 7, 'time_offset': 150, 'duration': 100},
                {'actuator': 0, 'time_offset': 300, 'duration': 100}
            ]},
            'o': {'events': [  # /o/ (o as in "go")
                {'actuator': 7, 'time_offset': 0, 'duration': 100},
                {'actuator': 0, 'time_offset': 150, 'duration': 100},
                {'actuator': 1, 'time_offset': 300, 'duration': 100}
            ]},
            
            # Diphthongs: two-phase patterns
            'aɪ': {'events': [  # /aɪ/ (i as in "ice")
                {'actuator': 0, 'time_offset': 0, 'duration': 100},
                {'actuator': 4, 'time_offset': 150, 'duration': 150}
            ]},
            'aʊ': {'events': [  # /aʊ/ (ou as in "out")
                {'actuator': 0, 'time_offset': 0, 'duration': 100},
                {'actuator': 7, 'time_offset': 150, 'duration': 150}
            ]},
            'eɪ': {'events': [  # /eɪ/ (a as in "ate")
                {'actuator': 1, 'time_offset': 0, 'duration': 100},
                {'actuator': 4, 'time_offset': 150, 'duration': 150}
            ]},
            'oʊ': {'events': [  # /oʊ/ (o as in "go")
                {'actuator': 3, 'time_offset': 0, 'duration': 100},
                {'actuator': 7, 'time_offset': 150, 'duration': 150}
            ]},
            'ɔɪ': {'events': [  # /ɔɪ/ (oi as in "boy")
                {'actuator': 3, 'time_offset': 0, 'duration': 100},
                {'actuator': 4, 'time_offset': 150, 'duration': 150}
            ]},
            
            # Liquids and glides
            'w': {'events': [  # /w/
                {'actuator': 0, 'time_offset': 0, 'duration': 120},
                {'actuator': 7, 'time_offset': 0, 'duration': 120}
            ]},
            'j': {'events': [  # /j/ (y as in "yes")
                {'actuator': 1, 'time_offset': 0, 'duration': 120},
                {'actuator': 6, 'time_offset': 0, 'duration': 120}
            ]},
            'h': {'events': [{'actuator': 0, 'time_offset': 0, 'duration': 80}]},  # /h/ (short, sharp)
        }
        
        return patterns
    
    def _build_g2p_map(self) -> Dict[str, str]:
        """
        Build basic grapheme-to-phoneme mapping.
        
        This is a simplified rule-based system. For production, use
        a proper G2P library like espeak-ng or phonemizer.
        """
        # Common grapheme-to-phoneme mappings
        g2p = {
            # Single letters (common pronunciations)
            'a': 'æ',  # cat
            'e': 'ɛ',  # bed
            'i': 'ɪ',  # bit
            'o': 'ɔ',  # dog
            'u': 'ʌ',  # cup
            'b': 'b',
            'c': 'k',  # cat
            'd': 'd',
            'f': 'f',
            'g': 'g',
            'h': 'h',
            'j': 'dʒ',
            'k': 'k',
            'l': 'l',
            'm': 'm',
            'n': 'n',
            'p': 'p',
            'q': 'k',  # queue
            'r': 'r',
            's': 's',
            't': 't',
            'v': 'v',
            'w': 'w',
            # 'x' handled specially - maps to 'k' + 's' sequence
            'y': 'j',  # yes
            'z': 'z',
            
            # Common digraphs
            'th': 'θ',  # think (voiceless)
            'sh': 'ʃ',
            'ch': 'tʃ',
            'ng': 'ŋ',
            'ph': 'f',
            'ck': 'k',
            'qu': ['k', 'w'],  # queen (two phonemes)
            
            # Common vowel combinations
            'ee': 'i',  # see
            'oo': 'u',  # blue
            'ai': 'eɪ',  # rain
            'ay': 'eɪ',  # day
            'oi': 'ɔɪ',  # boy
            'oy': 'ɔɪ',  # toy
            'ou': 'aʊ',  # out
            'ow': 'aʊ',  # cow
            'ie': 'i',  # pie
            'ei': 'eɪ',  # vein
            'oa': 'oʊ',  # boat
            'ue': 'u',  # blue
            
            # Common consonant combinations
            'ck': 'k',
            'ph': 'f',
            'gh': '',  # silent in many cases
            'kn': 'n',  # knee
            'wr': 'r',  # write
            'mb': 'm',  # lamb
        }
        
        return g2p

