# Information Theory Research

## Overview

Analysis of entropy, compression, and efficient encoding strategies for tactile communication systems.

## Entropy Fundamentals

### Character-Level Entropy

#### English Text Entropy
- **Theoretical maximum**: ~4.7 bits per character (Shannon, 1951)
- **Practical encoding**: 5-8 bits per character typical
- **With context**: Can approach theoretical limit
- **Compressed**: ~2-3 bits per character achievable

#### Character Frequency Distribution
English letter frequencies (approximate):
```
E: 12.7%  T: 9.1%   A: 8.2%   O: 7.5%   I: 7.0%
N: 6.7%   S: 6.3%   H: 6.1%   R: 6.0%   D: 4.3%
L: 4.0%   C: 2.8%   U: 2.8%   M: 2.4%   W: 2.4%
F: 2.2%   G: 2.0%   Y: 2.0%   P: 1.9%   B: 1.5%
V: 1.0%   K: 0.8%   J: 0.15%  X: 0.15%  Q: 0.10%
Z: 0.07%
```

**Space**: ~18% of text  
**Punctuation**: Varies significantly by text type

#### Implications for Encoding
- **Fixed-length encoding**: 5 bits (32 combinations) insufficient
- **Variable-length encoding**: Optimal for frequency distribution
- **Huffman coding**: Can achieve ~4.5 bits/character average
- **Arithmetic coding**: Can approach entropy limit

### Word-Level Entropy

#### Word Frequency Distribution
- **Most common words**: "the", "be", "to", "of", "and" (~20% of text)
- **Zipf's law**: Frequency inversely proportional to rank
- **Vocabulary size**: ~170,000 words in English
- **Active vocabulary**: ~20,000 words typical

#### Implications
- **Word-level encoding**: Significant compression possible
- **Dictionary encoding**: Common words as single tokens
- **Context-aware**: Further compression with language models

## Encoding Strategies

### Fixed-Length Encoding

#### Characteristics
- **Pattern length**: Constant for all characters
- **Simplicity**: Easy to implement and decode
- **Efficiency**: Inefficient for frequency distribution
- **Latency**: Predictable, minimal processing

#### Example
- 6-bit encoding: 64 possible characters
- Sufficient for alphabet + numbers + basic punctuation
- Average pattern length: 6 units
- No optimization for frequency

### Variable-Length Encoding

#### Huffman Coding
- **Principle**: Shorter codes for frequent characters
- **Optimal**: For known frequency distribution
- **Construction**: Binary tree-based algorithm
- **Efficiency**: Approaches entropy limit

#### Example Encoding (hypothetical)
```
E: 00    (2 bits)
T: 010   (3 bits)
A: 011   (3 bits)
O: 100   (3 bits)
...
Z: 1111111111  (10 bits)
```

**Average length**: ~4.5 bits per character

#### Advantages
- **Efficiency**: Better than fixed-length
- **Optimal**: For stationary distributions
- **Flexibility**: Can adapt to different texts

#### Disadvantages
- **Synchronization**: Requires clear boundaries
- **Adaptation**: Fixed distribution may not match actual text
- **Complexity**: More complex encoding/decoding

### Dictionary-Based Encoding

#### LZ77/LZ78 Algorithms
- **Principle**: Replace repeated sequences with references
- **Compression**: Significant for repetitive text
- **Adaptive**: Learns patterns from data
- **Application**: Common in general compression

#### Word-Level Dictionary
- **Common words**: Encode as single tokens
- **Compression**: 2-3x improvement possible
- **Latency**: Dictionary lookup overhead
- **Memory**: Requires dictionary storage

### Context-Aware Encoding

#### N-gram Models
- **Principle**: Use previous characters for prediction
- **Markov chains**: Character transitions
- **Compression**: Further reduction possible
- **Complexity**: Requires model training

#### Language Models
- **Neural networks**: Advanced prediction
- **Compression**: Can exceed entropy estimates
- **Latency**: Significant processing overhead
- **Application**: May not suit real-time systems

## Compression vs. Latency Trade-offs

### Processing Overhead

#### No Compression
- **Latency**: Minimal (<1ms processing)
- **Bandwidth**: Higher (5-8 bits/character)
- **Complexity**: Low
- **Use case**: Ultra-low latency requirements

#### Simple Compression (Huffman)
- **Latency**: Low (~1-2ms processing)
- **Bandwidth**: Moderate (4-5 bits/character)
- **Complexity**: Moderate
- **Use case**: Balanced performance

#### Advanced Compression
- **Latency**: Higher (5-10ms+ processing)
- **Bandwidth**: Lower (2-3 bits/character)
- **Complexity**: High
- **Use case**: Bandwidth-constrained systems

### Bandwidth Considerations

#### Wireless Communication
- **BLE**: ~1 Mbps theoretical, ~270 kbps practical
- **WiFi**: Much higher bandwidth available
- **Latency**: Protocol overhead significant

#### Character Transmission
- **Uncompressed**: ~40-64 bits/character (with overhead)
- **Compressed**: ~20-40 bits/character
- **Impact**: Compression reduces transmission time

### Recommendation for Teletypathy

Given ultra-low latency requirement (<10ms):
1. **Start with minimal compression**: Direct character mapping
2. **Optimize transmission**: Efficient protocol design
3. **Consider simple Huffman**: If bandwidth becomes constraint
4. **Avoid advanced compression**: Latency overhead too high

## Pattern Encoding Efficiency

### Tactile Pattern Representation

#### Pattern Components
- **Actuator ID**: Which motor (log₂(N) bits for N actuators)
- **Intensity**: Vibration strength (2-4 bits)
- **Duration**: Pulse length (3-5 bits)
- **Timing**: Delay/rhythm (3-5 bits)

#### Pattern Size
- **Simple pattern**: ~8-12 bits
- **Complex pattern**: ~16-24 bits
- **Multi-actuator**: Additional bits per actuator

### Encoding Efficiency Metrics

#### Bits per Character
- **Direct mapping**: 1 pattern = 1 character
- **Pattern size**: 8-24 bits typical
- **Efficiency**: Compare to theoretical entropy (4.7 bits)

#### Information Density
- **Spatial**: Multiple actuators = parallel encoding
- **Temporal**: Sequential patterns = serial encoding
- **Hybrid**: Combine spatial + temporal

### Optimization Strategies

#### Frequency-Based Pattern Assignment
- **Short patterns**: Common characters (E, T, A)
- **Long patterns**: Rare characters (Z, Q, X)
- **Efficiency**: Reduces average pattern length

#### Pattern Reuse
- **Similar characters**: Similar patterns (e.g., E vs. F)
- **Learning**: Easier recognition
- **Trade-off**: May reduce discrimination

#### Multi-Dimensional Encoding
- **Parallel actuators**: Encode multiple bits simultaneously
- **Sequential patterns**: Encode over time
- **Efficiency**: Higher information density

## Recommendations

### Initial Implementation
1. **Direct character mapping**: Simple, low latency
2. **Fixed pattern structure**: Predictable, learnable
3. **Frequency optimization**: Shorter patterns for common characters
4. **Minimal compression**: Focus on transmission efficiency

### Future Optimizations
1. **Variable-length patterns**: Huffman-like encoding
2. **Word-level patterns**: Dictionary encoding for common words
3. **Context-aware**: Adapt patterns based on context
4. **User customization**: Allow personal optimization

### Performance Targets
- **Pattern generation**: <1ms latency
- **Transmission**: <5ms latency (wireless)
- **Execution**: <4ms latency (hardware)
- **Total**: <10ms end-to-end

## References

### Information Theory Foundations
1. Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379-423. https://doi.org/10.1002/j.1538-7305.1948.tb01338.x
2. Shannon, C. E. (1951). Prediction and entropy of printed English. *Bell System Technical Journal*, 30(1), 50-64. https://doi.org/10.1002/j.1538-7305.1951.tb01366.x
3. Cover, T. M., & Thomas, J. A. (2006). *Elements of Information Theory* (2nd ed.). Wiley-Interscience.
4. MacKay, D. J. (2003). *Information Theory, Inference, and Learning Algorithms*. Cambridge University Press.

### Entropy and Character Frequency
5. Mayzner, M. S., & Tresselt, M. E. (1965). Tables of single-letter and digram frequency counts for various word-length and letter-position combinations. *Psychonomic Monograph Supplements*, 1(2), 13-32.
6. Wimmer, H., & Goswami, U. (1994). The influence of orthographic consistency on reading development: Word recognition in English and German children. *Cognition*, 51(1), 91-103.
7. Zipf, G. K. (1935). *The Psycho-Biology of Language: An Introduction to Dynamic Philology*. Houghton Mifflin.

### Compression Algorithms
8. Huffman, D. A. (1952). A method for the construction of minimum-redundancy codes. *Proceedings of the IRE*, 40(9), 1098-1101. https://doi.org/10.1109/JRPROC.1952.273898
9. Ziv, J., & Lempel, A. (1977). A universal algorithm for sequential data compression. *IEEE Transactions on Information Theory*, 23(3), 337-343. https://doi.org/10.1109/TIT.1977.1055714
10. Ziv, J., & Lempel, A. (1978). Compression of individual sequences via variable-rate coding. *IEEE Transactions on Information Theory*, 24(5), 530-536. https://doi.org/10.1109/TIT.1978.1055934
11. Welch, T. A. (1984). A technique for high-performance data compression. *Computer*, 17(6), 8-19. https://doi.org/10.1109/MC.1984.1659158

### Dictionary-Based Compression
12. Storer, J. A., & Szymanski, T. G. (1982). Data compression via textual substitution. *Journal of the ACM*, 29(4), 928-951. https://doi.org/10.1145/322344.322346
13. Bell, T. C., Cleary, J. G., & Witten, I. H. (1990). *Text Compression*. Prentice Hall.

### Context-Aware Encoding
14. Cleary, J. G., & Witten, I. H. (1984). Data compression using adaptive coding and partial string matching. *IEEE Transactions on Communications*, 32(4), 396-402. https://doi.org/10.1109/TCOM.1984.1096090
15. Moffat, A. (1990). Implementing the PPM data compression scheme. *IEEE Transactions on Communications*, 38(11), 1917-1921. https://doi.org/10.1109/26.61469

### Information Theory Applications
16. Gallager, R. G. (1968). *Information Theory and Reliable Communication*. Wiley.
17. Blahut, R. E. (1987). *Principles and Practice of Information Theory*. Addison-Wesley.
18. Sayood, K. (2017). *Introduction to Data Compression* (5th ed.). Morgan Kaufmann.

## Related Documents

- [Linguistics Research](linguistics.md)
- [Encoding System Design](../design/encoding_system.md)
- [Protocol Specification](../design/protocol_spec.md)

