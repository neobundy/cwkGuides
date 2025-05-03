# Demystifying Multihead Attention in Transformers

![](images/013-1.png)

Multihead Attention is a core innovation in the Transformer architecture, enabling the model to attend to different parts of a sentence simultaneously and capture complex relationships within the data. While single-head attention allows for capturing relationships between tokens in a single context, multihead attention extends this by allowing the model to focus on different aspects of the data across multiple heads. Let's break down how multihead attention works, focusing on how it processes Q (Query), K (Key), and V (Value) matrices, why multiple heads are used, and how the model decides which head focuses on what.

By understanding multihead attention, we gain insight into why Transformers are so powerful and versatile in handling complex natural language tasks. Let's dive into the mechanics of this key component.

### 1. The Role of Multihead Attention

In a standard single-head attention mechanism, the model computes attention scores between tokens using Q, K, and V matrices. While this approach works well for capturing relationships within a sequence, it's limited to focusing on a single relationship or context at a time. This means the model may miss other important patterns, especially when different parts of a sentence relate to each other in complex ways.

Multihead attention solves this by introducing multiple attention "heads." Each head performs attention independently, allowing the model to capture different relationships between tokens. For example, one head may focus on short-range dependencies (like relationships between adjacent words), while another head might capture long-range dependencies or syntactic structures.

This enables the model to understand the input sequence from multiple perspectives simultaneously.

### 2. Q, K, and V in Multihead Attention

To understand how multihead attention processes Q (Query), K (Key), and V (Value), let's break down the steps involved. For simplicity, let's assume we are working with two heads in the multihead attention mechanism.

#### Step 1: Independent Q, K, and V for Each Head

In a typical Transformer implementation, each head has its own set of Q, K, and V weight matrices. For example, in a model with two heads:

- Head 1 has its own Q, K, and V matrices.
- Head 2 has different Q, K, and V matrices.

This means that even though both heads process the same input embeddings, they will calculate different Q, K, and V vectors because they are using different sets of weight matrices. This allows each head to focus on different aspects of the input sequence.

For each input word embedding, the Q, K, and V matrices are calculated as follows for Head 1 and Head 2:

- Head 1: Q₁, K₁, V₁
- Head 2: Q₂, K₂, V₂

#### Step 2: Independent Self-Attention for Each Head

Once the Q, K, and V vectors are computed for each head, each head performs its own self-attention computation. This means each head calculates attention scores based on its own Q and K vectors and uses these scores to compute a weighted sum of its V values.

The attention mechanism for each head follows the same steps as in single-head attention:

1. Compute the dot product between Q and K.
2. Scale and apply softmax to get attention weights.
3. Use the attention weights to calculate a weighted sum of V values.

Each head generates its own output based on this process, so we end up with separate attention outputs for each head:

- Output₁ for Head 1
- Output₂ for Head 2

#### Step 3: Concatenation of Head Outputs

Once the attention scores and V-weighted outputs are calculated for each head, the outputs are concatenated. This step combines the information from all the heads into a single vector. So if each head produces an output of size d, and we have n heads, the concatenated output will have a size of n × d.

For example, with two heads, the final output would be:

- [Output₁; Output₂]

#### Step 4: Final Linear Transformation

After concatenation, a final linear transformation is applied using a weight matrix Wₒ to transform the concatenated output back into the appropriate dimension for the next layer. This step ensures that the multihead attention output has the same dimension as the input to keep the model's architecture consistent.

### 3. Why Multiple Heads?

You might wonder, why use multiple heads at all? Why not stick with single-head attention?

The reason is that each head can focus on different aspects of the input sequence. For example:

- One head might focus on short-range dependencies (like nearby words).
- Another head might capture long-range dependencies (such as distant word relationships).
- Some heads may learn to focus on syntactic structures (e.g., subject-verb relationships), while others might capture semantic meanings.

The key is that each head learns to focus on different aspects of the data, which leads to richer representations and better performance on complex tasks. By having multiple heads, the model can look at the same input sequence in multiple ways simultaneously, making it more robust and effective.

### 4. Dynamic Role of Each Head

A common question is: How do heads decide what to focus on?

The answer lies in the learning process. During training, each head's Q, K, and V weight matrices are updated through backpropagation to minimize the model's loss function. This means that each head learns autonomously which aspects of the input sequence to focus on. There is no pre-determined role for any specific head—each head's role emerges as part of the training process.

For example:

- One head might learn to attend to verbs and their objects.
- Another head might focus on subject-predicate relationships.
- Yet another might capture the relationship between entities mentioned earlier and later in the sequence.

The model doesn't "know" ahead of time which head will do what. It's the training data and loss minimization that guide each head to specialize in different ways.

GPT-3, one of the most well-known Transformer models, uses 96 attention heads in its multihead attention mechanism. These multiple heads allow the model to capture a diverse set of relationships within the input sequence, enhancing its capability to understand and generate human-like text effectively. By distributing the workload across 96 different attention heads, GPT-3 is able to focus on a wide range of dependencies and features, contributing to its remarkable performance on complex language tasks.

The specific number of attention heads in GPT-4, however, has not been publicly disclosed by OpenAI. While GPT-3's architecture is well documented, GPT-4 is believed to be significantly more advanced, though the exact architectural details, including the number of attention heads, remain unknown. This lack of detailed information makes it difficult to provide a direct comparison, but it is generally assumed that GPT-4 incorporates improvements that further enhance its ability to understand and generate complex text.

LLaMA 3.1, which has several variants, includes a 405 billion parameter version that uses 128 attention heads. This configuration enables it to capture a wide range of relationships in the input sequence, similar to GPT-3, but with even greater capacity due to its larger number of parameters and additional attention heads. These multiple heads contribute to its enhanced ability to process complex natural language tasks more effectively and efficiently.

### 5. An Alternative Approach: Shared Weight Matrices with Splitting

In some implementations, instead of using separate weight matrices for each head, a single large Q, K, and V matrix is used, which is then split across multiple heads. This approach is more memory efficient and reduces the number of parameters, while still allowing multiple attention heads to function.

For example, a single large Q matrix can be split into smaller Q₁, Q₂, etc., for each head. The same applies to K and V. The attention mechanism remains the same, but the splitting allows for a more compact and efficient implementation.

### Conclusion

Multihead attention is a powerful extension of single-head attention, allowing Transformer models to capture complex patterns in data by looking at multiple aspects of a sequence simultaneously. Each head processes the input with its own Q, K, and V weight matrices, leading to different attention outputs that are then concatenated and transformed for the next layer.

By having multiple heads, the model gains the ability to capture short-range and long-range dependencies, syntactic structures, and semantic meanings—all at once. The heads' roles are not pre-determined but are learned dynamically during training, ensuring that the model adapts to the data it is trained on.

Understanding the mechanics of multihead attention gives us deeper insight into why Transformer models are so effective at processing complex language tasks, and how they capture the nuanced relationships within data.