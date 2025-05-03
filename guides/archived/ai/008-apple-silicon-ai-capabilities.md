# Apple Silicon's AI Workloads: A Reality Check

I wanted to follow up on my earlier post about clustering Macs. The technology is interesting and allows for some experimentation, but we should be realistic about the current capabilities of these machines. Hopefully, this provides a clearer picture of where things stand with running AI on Apple Silicon at the moment.

To clear up any confusion, just because a model fits comfortably into unified memory on Apple Silicon, it doesn't guarantee smooth performance.

For instance, the Qwen2.5 14B half precision (16-bit) model requires approximately 30GB of memory (14 billion parameters * 2 bytes per parameter = 28GB, plus overhead). Based on my testing, this represents the practical limit of usable performance on a maxed-out M2 Ultra with 192GB of unified memory. Larger models experience significant slowdown during inference, with token generation speeds dropping below usable thresholds. When scaling up to the 32B parameter model (16-bit), for example, performance degrades to the point of being impractical for real-world use.

Newcomers might assume that a 30GB model would only consume that much memory, but the reality is more complex. The actual memory footprint only becomes apparent during runtime due to additional factors like overhead and intermediate processing requirements.

Quantization isn't a silver bullet either. Take the 69GB Mistral Large 4-bit quantized model on the same M2 Ultra—it readily consumes nearly all available memory while still delivering sluggish inference performance. Simply put, these larger models aren't practically usable on this hardware.

You might come across impressive inference demos showing blazing speeds on Apple Silicon, but if you look closely, you'll find they're running smaller 1B, 3B, or 7B parameter models, usually quantized. Getting 100+ tokens per second with these smaller models isn't particularly meaningful in practical applications. What truly matters is throughput on larger models, and until Apple Silicon can deliver that, CUDA GPUs remain invaluable.

Think of it like sorting algorithms. CPU processing might feel like bubble sort—simple but inefficient. Non-CUDA GPUs might be comparable to shell sort—decent but not optimal. Meanwhile, CUDA GPUs are like quicksort or whatever the cutting-edge algorithm currently is—efficient and effective. This isn't a technical comparison, but rather an intuitive way to convey the performance gap.

So don't rush to purchase a Mac with abundant unified memory expecting it to handle large models efficiently—it simply won't. The architecture isn't optimized for AI workloads the way CUDA GPUs are.

Moreover, clusters of Macs are not a complete solution either. While clustering allows running models too large for a single Mac's unified memory, there are important tradeoffs to consider. If a model fits into a single Mac's memory, running it there will generally be faster than distributing it across nodes due to communication overhead. And for models so large they require clustering, the inference performance may still be suboptimal due to the distributed nature of processing. At the current state of technology, Mac clustering is more valuable as an experimental platform for exploring distributed AI architectures than as a production solution for large model inference. While it enables running models that wouldn't fit on a single machine, users should maintain realistic expectations about performance.

The key is to maintain a realistic perspective, looking past marketing claims and hype to understand the actual capabilities and limitations of the hardware.

This isn't meant to be a super technical breakdown—just some real-world observations from my hands-on testing of large language models on Apple Silicon. Apple Silicon has potential, but we need to stay realistic about what it can handle for AI work right now.

Go ahead and play with any tech - just keep your expectations in check about what it can actually do right now.

Note that the LLMs mentioned in this post were tested using MLX-based implementations, specifically through LM Studio with MLX backend and mlx-lm command line tool.