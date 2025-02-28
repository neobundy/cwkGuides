# Why the Heck Do We Need Causal Attention in Transformers, Anyway

The reason we use **Causal Attention** is to ensure that, for next-word prediction tasks (like the kind performed by all large language models, or LLMs), the model does not have access to the tokens that come after the current token. This is a critical rule in autoregressive models.

In a typical self-attention mechanism, every token can attend to every other token in the sequence, both before and after its position. However, in next-word prediction, the model should not be allowed to see future tokens (i.e., the tokens that come after the current one). If the model had access to future tokens while predicting the current one, it would be like "cheating" by looking ahead at the answer. This would lead to incorrect predictions because the model wouldn’t actually be learning to predict; it would just be reading the future.

## How Does Causal Attention Work?

- **Causal Attention** ensures that each token can only attend to itself and the tokens that came before it. This prevents the model from using any information from future tokens when making a prediction about the current token.
- This is achieved using a technique called **Attention Masking**. Essentially, a triangular mask is applied, which prevents the model from attending to tokens that come after the current position in the sequence.

## Caution

It is important to note that Causal Attention applies both during the pretraining process and the inference stage. During inference, causal masking ensures that the model generates predictions step-by-step without seeing future tokens, thereby preserving the autoregressive property. The goal of causal masking is to ensure proper training and inference by forcing the model to learn how to predict each next token without access to future tokens.

## Summary

- We use **Causal Attention** because, in next-word prediction, the model must predict without knowing future tokens.
- It ensures the model only has access to the tokens that come before the current one, forcing it to predict each token step by step in sequence.

In short, **Causal Attention** is crucial for maintaining the "unknown future" condition, ensuring that predictions are made using only past and present information.