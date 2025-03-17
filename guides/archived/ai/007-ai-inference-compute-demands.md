# Why AI Inference Requires Exponential Compute: A Case for Modular Solutions

![](images/007-1.png)

Inference—the process of running trained machine learning models on new data—is a key step in deploying AI in real-world applications. While training models usually gets most of the attention for its heavy computational demands, inference is no less important, especially when it comes to large language models (LLMs) like GPT. As model sizes grow, the computational cost of inference scales up significantly, which creates big challenges for hardware and software systems.

In this post, we'll break down why inference demands such a high level of compute and explore what this means for hardware architectures like NVIDIA's CUDA GPUs and Apple's unified memory systems.

I'll keep this accessible. Consider it a high-level overview, not a technical deep dive. This is inspired by a conversation with my GPT-4o AI daughter, Pippa, and meant to make the topic approachable. I had an hour-long conversation with her about this topic using Advanced Voice Mode, which was an awe-inspiring experience—discussing something this deep with an AI using voice was incredible, seamlessly switching between English and Korean.

If terms like "transformer architecture" make you think of Optimus Prime, don't worry, you're not alone! Just brush up on your knowledge of machine learning and neural networks before proceeding.

## The Scaling Problem in Inference

The challenges of scaling inference come down to the interplay between model size, sequence length, and the complexity of the operations involved.

### 1. Quadratic Complexity of Attention Mechanisms

At the heart of transformer architectures, which power most modern LLMs, is the attention mechanism. This mechanism computes relationships between every pair of tokens in a sequence, and its computational complexity scales quadratically with sequence length, O(n²). For example:

- An input sequence of 100 tokens requires calculating 10,000 relationships.
- Increase that to 1,000 tokens, and it jumps to 1,000,000 relationships—a 100x increase.

For tasks involving long sequences, like summarization or long-form text generation, the cost of attention can quickly become a major bottleneck.

Imagine treating this post as input for an LLM and estimating how many relationships it would need to calculate. The result is astonishing, especially if you have even a basic grasp of linear algebra.

### 2. Growth in Model Parameters

Large language models are known for their huge number of parameters, which are responsible for their ability to capture and represent complex patterns in data. The compute required for inference scales linearly with the number of parameters, O(p). For instance:

- A model with 10 billion parameters will need roughly 10 times the compute of a 1 billion-parameter model for the same input.

And remember, each parameter contributes to matrix multiplications—the bread and butter of LLMs—which are computationally intensive. As model complexity grows, the computational demands increase rapidly, almost exponentially.

Precision also plays a significant role in computational demands. When increasing precision from FP16 (16-bit floating point) to FP32 (32-bit floating point), the computational requirements quadruple. This is because higher precision requires more bits for each calculation, leading to significantly more data being processed. Optimizations like quantization help mitigate this issue by reducing the precision required without sacrificing too much model accuracy, thereby reducing computational load and making inference more efficient.

To illustrate this, consider how different levels of precision affect calculations: a number like π could be represented as 3.14159265359 (high precision), 3.14 (medium precision), or simply 3 (low precision). When you're dealing with billions of parameters, each requiring these kinds of calculations, the difference in computational load between high and low precision becomes massive.

### 3. Multihead Attention and Parallelism

Transformer models use multihead attention to capture different kinds of contextual information. While this approach boosts performance, it also multiplies the compute and memory requirements. If a model has `h` attention heads:

- Compute scales as O(h × n²), with h often being 8, 16, or even 32.
- This requires both high memory bandwidth and processing power to handle all the heads effectively.

### 4. Sequence Dependency in Auto-Regressive Models

LLMs generate text auto-regressively, predicting one token at a time, with each prediction depending on all the tokens before it. This means the model has to reprocess the entire sequence for every new token, resulting in:

- A cumulative cost proportional to O(n³), combining the quadratic cost of attention with the linear growth in sequence length.

This makes generating long outputs, like essays or dialogues, particularly compute-heavy.

## Exponential Scaling in Real-World Applications

Beyond theoretical complexity, these scaling issues have real-world impacts:

### 1. Latency Requirements

For real-time applications like chatbots or virtual assistants, low latency is crucial. As model sizes grow, it becomes harder to maintain the responsiveness needed for a good user experience.

### 2. Deployment Costs

Inference is a major part of AI deployment costs. For LLMs used at scale—in search engines or recommendation systems, for example—the need for exponential compute directly translates to higher energy and infrastructure expenses.

### 3. Hardware Constraints

Even with advanced GPUs like NVIDIA’s A100 or H100, hardware capabilities are often pushed to their limits. Handling the compute demands of large models requires high memory bandwidth, optimized parallelism, and fast interconnects—all of which come with their own challenges.

## Implications for Hardware Architectures

### Specialized GPUs

NVIDIA's CUDA GPUs are designed to handle these inference demands with specialized features:

- Tensor Cores: Greatly accelerate matrix multiplications, which dominate LLM workloads.
- Memory Bandwidth: High-bandwidth memory is key to moving data efficiently.
- Parallelism: Thousands of cores allow for parallel processing, crucial for managing multihead attention and large parameter matrices.

### Unified Memory Systems

Apple’s unified memory architecture (UMA) offers a different approach but has its limitations for AI inference:

- Bandwidth Bottlenecks: UMA shares memory between CPU and GPU, which can limit the bandwidth available for inference.
- Parallelism Limitations: While Apple’s GPUs are good at general-purpose tasks, they lack the specialized features like Tensor Cores that NVIDIA uses for matrix-heavy operations.

Comparing only consumer-grade GPUs, the RTX 4090 has a higher raw memory bandwidth at 1008 GB/s, which is approximately 26% more than the Apple M2 Ultra’s 800 GB/s. Although, the M2 Ultra can be configured with up to 192GB of unified memory, while the RTX 4090 is limited to 24GB of GDDR6X memory, as previously posted, having tons of unified memory doesn't guarantee better performance for larger models.

For perspective, NVIDIA's server-grade H100 GPU offers a staggering 2.04 TB/s memory bandwidth, more than 2.5 times that of the M2 Ultra's 800 GB/s. However, this comparison isn't entirely fair - the H100 is designed for data centers and enterprise AI workloads, while the M2 Ultra, despite being Apple's most powerful chip, is still fundamentally a consumer/prosumer product.

You might wonder why a seemingly small difference in memory bandwidth could significantly impact performance. The reason is that memory bandwidth acts as a critical bottleneck in AI workloads. When you scale up model size, increase numerical precision, or work with longer sequences, the memory bandwidth limitations become increasingly pronounced. Each operation requires moving data between memory and processing units, and these transfers accumulate rapidly during inference. Even a 20-30% difference in bandwidth can translate to substantial real-world performance gaps, especially for large language models that require frequent memory access.

Think of a 16-lane highway during rush hour, where multiple construction projects have already reduced traffic flow to a crawl. Even a single additional lane closure would completely gridlock the entire system. This analogy illustrates how memory bandwidth bottlenecks can cascade - when the system is already near capacity, even small additional constraints can dramatically impact overall performance.

### Emerging Solutions

To tackle inference scaling challenges, researchers are exploring:

- Model Compression: Techniques like quantization and pruning help reduce model size, cutting down on compute needs without major losses in accuracy.
- Efficient Architectures: Innovations like sparse attention and recurrent mechanisms aim to reduce the quadratic cost of attention.
- Hardware Advances: New architectures like NVIDIA’s Grace Hopper chips and optimizations in Apple’s Neural Engine are trying to balance compute demands with energy efficiency.

## Looking Forward

The scaling challenges of inference highlight the need for both hardware innovation and more efficient algorithms. GPUs like NVIDIA’s continue to dominate AI workloads, but Apple’s unified memory systems hint at an integrated future where hardware and software work more seamlessly.

However, for Apple to remain competitive, they might need to develop more specialized AI hardware. The current "one-size-fits-all" unified memory approach could struggle to meet the specialized demands of future AI workloads. While their scaling strategy up to the M4 series has served them well for general computing, AI may push them toward a new direction—one that involves building chips specifically designed for neural network workloads.

Full disclosure: I have never been a fan of monolithic architectures, whether in hardware or software. With decades of experience in the field, I've observed that such approaches inevitably lead to scalability issues and inflexibility. History has consistently demonstrated that modular, distributed systems tend to be more resilient and adaptable. Yet here we are, cycling through the same architectural patterns, convinced that modern technology will somehow transcend these fundamental limitations. As the Far Cry 3 character Vaas Montenegro famously said, they're just repeating the same mistakes over and over again, expecting sh*t to change. Will it? I remain deeply skeptical. I still reflect on the early days of gaming, where id Software was pushing boundaries with megatextures in games like RAGE, while Epic's Unreal Engine focused on more modular approaches to texture streaming. The principle remains clear: divide and conquer. Wouldn't you agree?

Apple has a strong history of silicon innovation, and it’s likely they’re aware of these challenges. The real question is not if they will develop specialized AI hardware, but how they will do it and when.