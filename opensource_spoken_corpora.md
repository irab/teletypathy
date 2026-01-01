# Open-Source Spoken English Corpora: Free GitHub Resources

## Overview

This document lists **free, open-source, GitHub-available** spoken English conversation corpora that are actively maintained and suitable for Teletypathy analysis.

## Top Recommendations

### 1. Mozilla Common Voice ⭐ **BEST FOR FREE ACCESS**

**Description:**
- **Crowdsourced** speech dataset
- **Public domain** (CC0 license)
- **Actively maintained** by Mozilla
- **Growing dataset** (regularly updated)
- Multiple languages including English

**Characteristics:**
- Natural speech from volunteers
- Diverse accents and demographics
- Sentence-level transcriptions
- High-quality recordings
- Validated by community

**Access:**
- **GitHub**: https://github.com/mozilla/common-voice
- **Dataset Download**: https://commonvoice.mozilla.org/datasets
- **License**: CC0 (Public Domain)
- **Free**: Yes, completely free

**Relevance to Teletypathy:**
- ✅ **Free and open-source**
- ✅ **Actively maintained**
- ✅ **Large and growing** dataset
- ✅ Natural speech patterns
- ✅ Diverse speakers
- ⚠️ May need phoneme conversion (G2P)

**Use Cases:**
- Word frequency in natural speech
- Accent/dialect analysis
- Natural conversation patterns
- Large-scale analysis

**Quick Start:**
```bash
# Download Common Voice dataset
# Visit: https://commonvoice.mozilla.org/datasets
# Download English dataset (latest release)
# Includes: audio files + transcriptions
```

---

### 2. LibriSpeech ⭐ **BEST FOR PHONEME ANALYSIS**

**Description:**
- **~1,000 hours** of English speech
- Derived from **LibriVox** audiobooks
- **Freely available**
- Widely used in speech recognition research
- **Phoneme-level transcriptions** available

**Characteristics:**
- Read speech (audiobooks)
- High-quality audio
- Multiple speakers
- Phonetically transcribed
- Standardized format

**Access:**
- **Website**: http://www.openslr.org/12/
- **License**: Free for research use
- **Download**: Direct download links available
- **GitHub**: Various processing tools available

**Relevance to Teletypathy:**
- ✅ **Free for research**
- ✅ **Phoneme-level transcriptions** (via tools)
- ✅ Large dataset
- ✅ High quality
- ✅ Standardized format

**Use Cases:**
- **Phoneme frequency analysis**
- Phoneme sequence patterns
- Multi-ring optimization
- Speech recognition training

**Quick Start:**
```bash
# Download LibriSpeech
wget http://www.openslr.org/resources/12/train-clean-100.tar.gz
# Extract and process
# Use tools for phoneme extraction
```

---

### 3. LibriHeavy ⭐ **LARGEST FREE CORPUS**

**Description:**
- **50,000 hours** of English speech
- Derived from LibriVox
- **Largest freely available** corpus
- Includes punctuation, casing, context
- **2023 release** (very up-to-date)

**Characteristics:**
- Read speech (audiobooks)
- Very large scale
- Rich metadata
- Modern release
- Free and open

**Access:**
- **Paper**: https://arxiv.org/abs/2309.08105
- **License**: Free for research
- **Download**: Available through research channels
- **GitHub**: Processing tools available

**Relevance to Teletypathy:**
- ✅ **Very large** (50,000 hours)
- ✅ **Up-to-date** (2023)
- ✅ Free
- ✅ Rich metadata
- ⚠️ Read speech (not conversation)

**Use Cases:**
- Large-scale phoneme analysis
- Word frequency analysis
- Pattern optimization
- Statistical analysis

---

### 4. CoVoST (Common Voice Speech Translation) ⭐ **MULTILINGUAL**

**Description:**
- Based on **Mozilla Common Voice**
- **2,880 hours** of speech
- **78,000 speakers**
- **CC0 license** (public domain)
- Multilingual (includes English)

**Characteristics:**
- Natural speech
- Multiple languages
- Large scale
- Free and open
- Actively maintained

**Access:**
- **GitHub**: https://github.com/facebookresearch/covost
- **License**: CC0 (Public Domain)
- **Free**: Yes
- **Download**: Available via GitHub

**Relevance to Teletypathy:**
- ✅ **Free and open-source**
- ✅ **GitHub available**
- ✅ Large dataset
- ✅ Natural speech
- ✅ Actively maintained

**Use Cases:**
- Multilingual analysis
- Natural speech patterns
- Large-scale analysis
- Cross-language comparison

---

### 5. Student-Transcribed Corpus of Spoken American English

**Description:**
- High-quality transcripts + audio
- Native American English speakers
- Various settings: interviews, talks, vlogs
- **Freely accessible**
- Online search interface

**Characteristics:**
- Natural speech
- Diverse settings
- High quality
- Free access
- Searchable online

**Access:**
- **Website**: https://www.spokencorpus.org/
- **License**: Free for research
- **Download**: Available via website
- **Free**: Yes

**Relevance to Teletypathy:**
- ✅ Free access
- ✅ Natural speech
- ✅ Diverse contexts
- ✅ High quality
- ⚠️ May need phoneme conversion

**Use Cases:**
- Natural conversation analysis
- Context-specific patterns
- Word frequency analysis

---

### 6. Spoken Wikipedia Corpora

**Description:**
- Time-aligned audio recordings
- Wikipedia articles read aloud
- Multiple languages (including English)
- **CC BY-SA 4.0 license**
- Hundreds of hours

**Characteristics:**
- Read speech (Wikipedia)
- Time-aligned
- Diverse topics
- Free license
- Actively maintained

**Access:**
- **Website**: https://nats.gitlab.io/swc/
- **License**: CC BY-SA 4.0
- **Free**: Yes
- **Download**: Available via website

**Relevance to Teletypathy:**
- ✅ Free and open
- ✅ Time-aligned
- ✅ Diverse topics
- ✅ Actively maintained
- ⚠️ Read speech (not conversation)

**Use Cases:**
- Topic-specific analysis
- Time-aligned patterns
- Diverse vocabulary

---

### 7. ConvoKit (Cornell)

**Description:**
- **Python toolkit** for conversation analysis
- Includes **multiple datasets**:
  - Cornell Movie-Dialogs Corpus
  - Wikipedia Talk Pages Corpus
  - Reddit conversations
- **Free and open-source**
- Actively maintained

**Characteristics:**
- Conversation-focused
- Multiple datasets
- Python toolkit
- Free and open
- Actively maintained

**Access:**
- **GitHub**: https://github.com/CornellNLP/ConvoKit
- **Website**: https://convokit.cornell.edu/
- **License**: Free for research
- **Free**: Yes

**Relevance to Teletypathy:**
- ✅ **Free and open-source**
- ✅ **GitHub available**
- ✅ Conversation-focused
- ✅ Python toolkit (easy to use)
- ✅ Actively maintained

**Use Cases:**
- Conversation patterns
- Dialog analysis
- Word frequency in conversations
- Natural language patterns

**Quick Start:**
```python
# Install ConvoKit
pip install convokit

# Load dataset
from convokit import Corpus, download
corpus = Corpus(filename=download("movie-corpus"))
```

---

### 8. VoxPopuli

**Description:**
- **100,000 hours** of speech data
- **23 languages** (including English)
- **Open license**
- Unlabelled speech
- Large-scale corpus

**Characteristics:**
- Very large scale
- Multiple languages
- Unlabelled (may need processing)
- Free license
- Research-focused

**Access:**
- **Paper**: https://arxiv.org/abs/2101.00390
- **License**: Open for research
- **Download**: Available via research channels
- **Free**: Yes

**Relevance to Teletypathy:**
- ✅ Very large scale
- ✅ Free
- ✅ Multiple languages
- ⚠️ Unlabelled (needs processing)

**Use Cases:**
- Large-scale analysis
- Unsupervised learning
- Pattern discovery

---

## Comparison Table

| Corpus | Size | License | GitHub | Phonemes | Best For |
|--------|------|---------|---------|----------|----------|
| **Common Voice** | Large | CC0 | ✅ Yes | ⚠️ Need G2P | **General use** |
| **LibriSpeech** | 1K hours | Free | ⚠️ Tools | ✅ Yes | **Phoneme analysis** |
| **LibriHeavy** | 50K hours | Free | ⚠️ Tools | ⚠️ Need G2P | **Large-scale** |
| **CoVoST** | 2.8K hours | CC0 | ✅ Yes | ⚠️ Need G2P | **Multilingual** |
| **ConvoKit** | Multiple | Free | ✅ Yes | ⚠️ Need G2P | **Conversations** |
| **Spoken Wikipedia** | Hundreds hrs | CC BY-SA | ⚠️ No | ⚠️ Need G2P | **Diverse topics** |
| **Student Corpus** | Medium | Free | ⚠️ No | ⚠️ Need G2P | **Natural speech** |

## Recommended Workflow

### For Quick Analysis (No Setup)

**Use Common Voice:**
1. Visit https://commonvoice.mozilla.org/datasets
2. Download English dataset
3. Extract transcriptions
4. Analyze word frequencies

### For Phoneme Analysis

**Use LibriSpeech + Phonemizer:**
1. Download LibriSpeech from openslr.org
2. Use `phonemizer` Python library for G2P conversion
3. Extract phoneme sequences
4. Analyze phoneme frequencies

### For Conversation Analysis

**Use ConvoKit:**
1. Install: `pip install convokit`
2. Load conversation corpus
3. Extract word/phoneme patterns
4. Analyze conversation-specific patterns

## Implementation Examples

### Example 1: Using Common Voice

```python
# Download Common Voice dataset
# Extract transcriptions
import pandas as pd

# Load Common Voice transcriptions
df = pd.read_csv('common_voice_en.tsv', sep='\t')

# Extract sentences
sentences = df['sentence'].tolist()

# Analyze word frequencies
from collections import Counter
import re

words = []
for sentence in sentences:
    words.extend(re.findall(r'\b[a-z]+\b', sentence.lower()))

word_freq = Counter(words)
print(f"Total words: {len(words):,}")
print(f"Unique words: {len(word_freq):,}")
print(f"Top 20 words: {word_freq.most_common(20)}")
```

### Example 2: Using LibriSpeech with Phonemizer

```python
# Install: pip install phonemizer

from phonemizer import phonemize
from collections import Counter

# Convert text to phonemes
text = "Hello world, this is a test."
phonemes = phonemize(text, language='en-us', backend='espeak', strip=True)

print(f"Text: {text}")
print(f"Phonemes: {phonemes}")

# Analyze phoneme frequencies
phoneme_list = phonemes.split()
phoneme_freq = Counter(phoneme_list)
print(f"Phoneme frequencies: {phoneme_freq.most_common(10)}")
```

### Example 3: Using ConvoKit

```python
# Install: pip install convokit

from convokit import Corpus, download

# Download and load corpus
corpus = Corpus(filename=download("movie-corpus"))

# Extract conversations
conversations = []
for conversation in corpus.iter_conversations():
    utterances = [utt.text for utt in conversation.iter_utterances()]
    conversations.append(' '.join(utterances))

# Analyze word frequencies
from collections import Counter
import re

all_words = []
for conv in conversations:
    words = re.findall(r'\b[a-z]+\b', conv.lower())
    all_words.extend(words)

word_freq = Counter(all_words)
print(f"Top 20 words in conversations: {word_freq.most_common(20)}")
```

## Quick Access Links

### Free & Open-Source

1. **Mozilla Common Voice**
   - Website: https://commonvoice.mozilla.org/
   - GitHub: https://github.com/mozilla/common-voice
   - Datasets: https://commonvoice.mozilla.org/datasets
   - License: CC0 (Public Domain)

2. **LibriSpeech**
   - Website: http://www.openslr.org/12/
   - License: Free for research
   - Download: Direct links on website

3. **ConvoKit**
   - GitHub: https://github.com/CornellNLP/ConvoKit
   - Website: https://convokit.cornell.edu/
   - Install: `pip install convokit`
   - License: Free for research

4. **CoVoST**
   - GitHub: https://github.com/facebookresearch/covost
   - License: CC0 (Public Domain)

5. **Spoken Wikipedia**
   - Website: https://nats.gitlab.io/swc/
   - License: CC BY-SA 4.0

6. **Student-Transcribed Corpus**
   - Website: https://www.spokencorpus.org/
   - License: Free for research

## Recommendations for Teletypathy

### Best Overall: Mozilla Common Voice

**Why:**
- ✅ **Completely free** (CC0 license)
- ✅ **Actively maintained** by Mozilla
- ✅ **GitHub available** with tools
- ✅ **Large and growing** dataset
- ✅ **Natural speech** from diverse speakers
- ✅ **Easy to download** and use

**Use for:**
- Word frequency analysis
- Natural speech patterns
- Large-scale analysis
- Quick prototyping

### Best for Phoneme Analysis: LibriSpeech

**Why:**
- ✅ **Free for research**
- ✅ **Phoneme-level transcriptions** available
- ✅ **Large dataset** (1,000 hours)
- ✅ **Standardized format**
- ✅ **Widely used** (lots of tools available)

**Use for:**
- Phoneme frequency analysis
- Multi-ring optimization
- Phoneme sequence patterns

### Best for Conversations: ConvoKit

**Why:**
- ✅ **Free and open-source**
- ✅ **GitHub available**
- ✅ **Python toolkit** (easy to use)
- ✅ **Conversation-focused** datasets
- ✅ **Actively maintained**

**Use for:**
- Conversation patterns
- Dialog analysis
- Natural language in conversations

## Conclusion

**For immediate use without licensing:**

1. **Mozilla Common Voice** - Best overall, free, GitHub available
2. **ConvoKit** - Best for conversations, Python toolkit, GitHub available
3. **LibriSpeech** - Best for phoneme analysis, free for research

All three are **free, actively maintained, and suitable for Teletypathy analysis**. Common Voice is the easiest to get started with, while LibriSpeech provides the best phoneme-level data for encoding optimization.

