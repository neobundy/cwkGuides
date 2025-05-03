# Parameter Counts and VRAM Requirements for LLMs - Comprehensive Guide

![Level of Sophistication](images/20250131-01.png)

Ever wondered if you can run that huge DeepSeek R1 model (with 671B parameters) on your laptop or across your new Apple Silicon cluster? This guide gathers the essential concepts—from the simplest to the most advanced—into one place. For a quick ballpark figure, check the **TL;DR**. If you want the deeper details, read on. Some sections provide breadcrumbs for further exploration, because no single guide can capture this rapidly evolving field entirely.

Despite the constant change, the fundamentals remain the same. Once you grasp these basics, you’ll be ready to adapt as new techniques emerge.

---

## Quick Reference (TL;DR)

A rough memory requirement for an LLM with **N** billion parameters:

- **FP32**: N × 4 GB  
- **FP16/BF16**: N × 2 GB  
- **INT8**: N × 1 GB  
- **INT4**: N × 0.5 GB  

> **Note**: These are the most common formats, but there are many other quantization methods (mixed-bit, sparse, vector/product quantization, etc.). Some cutting-edge approaches achieve under 2 bits per parameter for specific layers, but these require specialized tuning and are not yet widely used.

### Example
A **10B**-parameter model needs approximately:

- **40 GB** in FP32 (10B × 4 bytes)
- **20 GB** in FP16/BF16 (10B × 2 bytes)
- **10 GB** in INT8 (10B × 1 byte)
- **5 GB** in INT4 (10B × 0.5 bytes)

---

## Beyond Raw Memory Requirements

So you’ve done the math and found you have just enough VRAM to load that massive model. Great! But having enough memory to load a model is like having a garage big enough for a Formula 1 car—you can fit it, but can you drive it effectively on regular roads?

Real-world usability depends on **tokens per second (tok/s)**, which is basically the model's "reading speed." If your model produces text slower than you can read, it might technically "run," but it won't be practical.

**As a rule of thumb for generation speed:**
- **<10 tok/s**: Painfully slow for conversation.
- **10–20 tok/s**: Acceptable for email or documentation, but still sluggish for chat.
- **20+ tok/s**: Smooth enough for most interactive uses.

Generation speed varies widely based on:
- Model size and architecture (7B is naturally faster than 70B).
- Hardware capabilities (CPU speed, memory bandwidth, etc.).
- Usage details (batch size, context length, concurrency).
- End goal (chat vs. offline processing).

Bottom line: Don’t just ask, “Can I load it?” Also ask, “Can I run it at a usable speed for my needs?”

---

## Hardware Matters: Not All GPUs Are Created Equal

Here’s a key insight: two GPUs with the same VRAM can have very different performance. Think of it like comparing two cars with the same fuel tank capacity—identical fuel capacity doesn’t mean they’ll perform equally on the racetrack.

### What Makes a GPU “AI-Friendly”?

1. **Tensor Cores**
   - Specialized “AI calculators” built into some GPUs.
   - Optimized for matrix math, which LLMs rely on.
   - Example: An NVIDIA A100 can be 10–20× faster than a gaming GPU with similar VRAM.

2. **Memory Bandwidth**
   - It’s not just about storage; it’s about how quickly data can move.
   - Comparable to having an 8-lane highway vs. a single-lane road.
   - Real numbers: 
     - Gaming GPU: ~500 GB/s
     - AI-oriented GPU: 2–3 TB/s

3. **Memory Hierarchy**
   - Modern AI GPUs use advanced caching and data loading strategies.
   - Optimizations predict what data is needed next, boosting efficiency.

### Real-World Impact

Consider two 24GB GPUs:
- A gaming RTX 4090
- An NVIDIA A5000  

They have the same VRAM on paper, yet the A5000 typically handles large LLMs more efficiently. Apple Silicon’s Unified Memory Architecture (UMA) also changes the game by sharing memory between CPU and GPU, but dedicated NVIDIA GPUs with specialized tensor cores often outperform them in sheer LLM throughput.

### What to Look For

When evaluating hardware for AI:
- Does it have tensor cores (or an equivalent)?
- How high is its memory bandwidth?
- Is it designed for compute or for graphics?
- What do real-world benchmarks say about LLM performance?

Raw VRAM is just one piece of the puzzle. For real-world performance, consider specialized hardware features, bandwidth, and software optimizations—just like judging a race car by more than its gas tank size.

---

## Basic Concepts

### What is a Parameter?

In neural networks, “parameters” typically refer to **weights** (the large matrices that store the network’s learned information) plus **biases** (tiny offsets after matrix multiplications). Biases are usually a small fraction of the total.

#### Example
- A layer with dimensions 1024×1024:
  - Weights = 1024 × 1024 = 1,048,576 parameters
  - Biases = 1024 parameters (~0.1% of total)

### Terminology Nuances

- **Weights** often used colloquially to mean both weights and biases.
- **Bits per weight** means bits per parameter.
- Academic papers tend to be precise; engineering contexts might be more informal.

---

## Memory Estimation

### Rule of Thumb

- **FP32** (32-bit float): N × 4 GB  
- **FP16/BF16** (16-bit float): N × 2 GB  
- **INT8** (8-bit): N × 1 GB  
- **INT4** (4-bit): N × 0.5 GB  

> Real models often need extra memory for caching, overhead, and more.

### FP16 vs. BF16

- **FP16** (Float16): 1 sign bit, 5 exponent bits, 10 mantissa bits. Great near-zero precision but narrower range.  
- **BF16** (BFloat16): 1 sign bit, 8 exponent bits, 7 mantissa bits. Same range as FP32, less precision in mantissa, excellent training stability, widely supported.

### 8-Bit Options

- **INT8**: Fixed-point, 256 discrete levels, typically used for inference.  
- **FP8**: Emerging format with variants (E4M3, E5M2). Still maturing but promising.

### 4-Bit Options

- **INT4**: 16 levels (-8 to +7). Often used in extreme compression scenarios for inference.  
- **Experimental FP4 (NF4)**: Research-stage format optimized for normal distributions.

#### Group-Size Quantization
Lower-bit formats often use group-wise scaling (e.g., 64 consecutive weights share a scaling factor). Larger group size reduces overhead but can lower accuracy.

### Example Memory Needs

For a **10B**-parameter model:
- FP32: ~40 GB
- FP16/BF16: ~20 GB
- INT8: ~10 GB
- INT4: ~5 GB

> You’ll need additional overhead for optimizer states, activation memory, KV cache, and so forth.

### Formula

Base Memory (GB) = N × (B/8) × (1 + O)

Where:
- N = number of parameters (in billions)  
- B = bits per parameter (e.g., 32 for FP32, 16 for FP16, 8 for INT8, 4 for INT4)  
- O = overhead factor (commonly 0.1–0.3, covering alignment/padding/framework overhead)  

---

## Additional Memory Requirements

### 1. Training Memory

- **Primary Training Format**  
  - Historically FP32, now often BF16 or mixed precision.  
  - FP8 is emerging but not yet mainstream.

- **Optimizer States**  
  - Adam: up to 8× model size (two moments + master weights).  
  - AdaFactor / Lion: can be ~2×.

- **Gradients**: ~1× model size.  
- **Activations**: depends heavily on batch size.  
- **Temporary Buffers**: ~1.2–1.5× model size.

### 2. Inference Memory

- **KV Cache**: Scales with context length and number of heads.  
- **Activation Memory**: Less than training but still non-trivial.  
- **Framework Overhead**: Typically 10–30% beyond raw weights.

---

## Precision Deep Dive

### FP32

- 1 sign bit, 8 exponent bits, 23 mantissa bits  
- Large dynamic range  
- Good numerical stability but high memory usage  

### Half Precision (FP16/BF16)

- Common in modern GPUs, TPUs, and Apple Silicon.  
- Significantly reduces memory usage and often speeds training/inference.  
- BF16 has better dynamic range, especially helpful in training.

### 8-bit Formats (INT8, FP8)

- Used primarily for inference to reduce memory requirements.  
- Often needs calibration or fine-tuning for accuracy.  
- FP8 is gaining traction for both training and inference.

### 4-bit and Lower (INT4, NF4)

- **INT4** and **NF4** are extreme compression approaches.  
- Often used in specialized scenarios or combined with higher-precision layers to maintain acceptable accuracy.

---

## Advanced Topics

### Quantization Techniques

1. **Vector Quantization (VQ)**  
   - Uses clustering (e.g., k-means) or product quantization.  
   - Potentially higher compression at the cost of complexity.

2. **Sparse Quantization**  
   - Combines weight pruning with quantization.  
   - Can greatly reduce size but often needs specialized hardware to see real speed gains.

3. **Hybrid Methods**  
   - Some layers at INT8, others at INT4, or a mix with pruning.

### Mixed Precision

1. **Training Workflow**  
   - Often keeps “master” weights in FP32 but does forward/backward passes in FP16/BF16.  

2. **Layer-Specific Precision**  
   - Critical layers (embeddings, attention) might remain higher precision.  
   - Other parts go lower to save memory.

### Memory Optimization Strategies

1. **Gradient Checkpointing / Activation Recomputation**  
   - Store fewer intermediate activations, recompute them when needed.  
   - Saves memory at the expense of extra computation.

2. **Attention Optimization**  
   - Methods like Flash Attention or multi-query attention reduce memory use.

3. **Multi-GPU Parallelism**  
   - **Pipeline Parallelism**: Split layers across devices.  
   - **Tensor Parallelism**: Split matrix ops within layers.  
   - **ZeRO**: Shard optimizer states/gradients to reduce duplication.

---

## KV Cache Deep Dive

During inference, the Key-Value (KV) cache can dominate memory usage at large context lengths. Approximate formula:

KV Cache (GB) = (context_length × num_layers × num_kv_heads × head_dim × 2 × 2 × num_users) / 10^9

Where:
- **context_length** = maximum tokens / sequence length  
- **num_layers** = total transformer layers  
- **num_kv_heads** = key-value attention heads  
- **head_dim** = dimension per head  
- First “2” = 2 bytes per FP16 value  
- Second “2” = storing both keys and values  
- **num_users** = concurrent inference requests  

### KV Cache Optimization

- **Page-Based Management**: Efficient memory page usage and possible disk offloading.  
- **Dynamic Scaling**: Adjust context length or evict low-priority data under pressure.  
- **Multi-query Attention**: Shares a single set of keys/values among heads to reduce duplication.

---

## Final Thoughts

- These guidelines apply to both dense and mixture-of-experts (MoE) models, though MoEs need additional considerations.  
- Large models often rely on sophisticated memory management and parallelization for efficiency.  
- The more you compress (quantize, prune, etc.), the more specialized the hardware and implementation.  
- Stay alert: new quantization and compression methods emerge almost monthly.

**Remember**: All numbers here are approximate. Actual requirements depend on model architecture, hardware, and software frameworks. Once you understand these fundamentals, you’ll be well-equipped to handle whatever emerges next.