# How AIs Interact with Humans: 101

This isn't a serious in-depth essay on AIs. I've already done much work on that in my GitHub repos, so if you're intrigued, visit them.

Consider this a beginner's guide to how AIs interact with humans, tailored for those with minimal technical background.

I just wanted to share some really basic building blocks that I laid out for my wife, who has little coding experience and isn't an expert in computing.

AIs understand only numbers under the hood. Terms like natural language, keywords, prompts, tokens, tensors, and embeddings are often mentioned, but ultimately, the key components AI models deal with are embeddings as tensors. These terms mean different things. Language, keywords, and prompts are human-readable text, not machine-friendly. Tokens are in-between. Sometimes geeks would say tokens are numbers. When they say that, they mean token IDs, not the actual words. Tokens are mapped to corresponding numbers in the vocabulary of the model.

That's why you need token ID mapping vocabularies to convert human-readable text to machine-friendly numbers. When you download a model, you also download the vocabulary file, usually named 'vocab.txt'.

**I won't go into the nitty-gritty details of how to use a model.**

When you enter a simple prompt like "a cute cat" into a language model, that's called a prompt made of natural language. The model itself doesn't convert it to numbers—that's the job of the tokenizer and the script you use to interact with the model. Even ChatGPTs are run in a specific script that you don't get to see. The model doesn't understand the prompt as it is; it's converted to numbers, then fed to the model by a pre-made script that acts as an interface between you and the model. 

**Don't think of AI models as programs—they're not.** You need a script or program to load and utilize the model. Models are not programs.

Let's take a look at a simple script. Since X articles or posts do not support fine formatting, I'm attaching a screenshot of the script.

It's not a full-blown script, just a skeleton to display tokens and embeddings.

You don't have to comprehend the code; just skim through it like normal text. It's not a programming tutorial, just a way to show you how a script looks.

In this script, OpenAI's tokenizer and model are used. The script is written in Python. The prompt "a cute cat" is first tokenized, mapped to corresponding IDs, and then converted to embeddings.

**English is easy to tokenize, mostly splittable with white spaces and punctuation.** But for better results, you need stemming and lemmatization, hence a tokenizer that supports these features with proper vocabularies.

Non-English languages, like Korean, are not so easy to tokenize. You need to use a tokenizer that supports the language you're working with. Korean, for example, is very complex to tokenize. You need a morpheme analyzer to split Korean words into morphemes and a good stemming and lemmatization vocabulary to get good results.

Special algorithms compress tokens like zipping files. Essentially, you fold and unfold repeating tokens like origami. But that's another boring detail.

**Tensors are just a fancy term for multi-dimensional arrays—a data type.** You don't have to understand tensors to use AI models. Just know that they're multi-dimensional arrays, which is why you need to learn linear algebra. Tensors are matrices and vectors in a nutshell. AI models are just a bunch of matrices and vectors called parameters: biases and weights. They're just numbers in the end, wrapped in fancy tensors. Some people don't use the term tensors; they just say matrices and vectors, or good ol' arrays.

Look at those tensors: [246, 4328, 2585], for example. Traditionally, it's an array of numbers, but in the AI world, it's a tensor. Notice the double brackets in embedding tensors? The number of opening brackets can be loosely considered the number of dimensions of that tensor. The more brackets, the more dimensions. AIs can deal with tens, even hundreds, or thousands of dimensions, given enough compute.

When we say "compute," we mean it in the context of AI, not general computing. "Compute" in AI requires GPUs, not CPUs. CPUs are for general computing; GPUs are for AI. If you have to deal with multi-dimensional tensor operations, you need fast, simultaneous calculations. That's why you need GPUs. CPUs are not good at parallel calculations—they're good at sequential calculations. Modern GPUs can compute thousands of tensor operations simultaneously, whereas CPUs can only do a few. You'd have to wait for hours if your GPTs were run on CPUs for even a simple response.

See the last embedding tensors? Essentially, language models deal with those, not the interim forms, whether text or numbers. They're the final form of the prompt. The model doesn't understand the prompt as it is; it needs to be ultimately converted into embeddings.

Embeddings reside in a massive space called embedding space, where all possible embeddings of the tokens are placed. The embeddings are vectors in that space. The model calculates the distance between the embeddings of the tokens to generate the next token. The closer the embeddings, the more likely the token will be generated. That's how the model predicts the next token. It's a simple explanation, though the actual process is more complex. For instance, the tokens "husband" and "wife" are understandably close enough in the embedding space as "king" and "queen" would be. Any reasonable model can easily figure out the following formula:

husband - wife = king - queen

That's the magic of embeddings. "Son" and "daughter"? They're close enough in the embedding space. How about "prince" and "princess"? You get the idea.

Any embeddings space cannot be visualized by humans. It's such a complex, multi-dimensional space that it's next to impossible to visualize accurately. The visualized representations you find online are just simplifications of the actual space or reduced dimensions.

With these complex dimensions, embeddings can capture subtle nuances of the word and context. They're not just a bunch of simple numbers—they're textured with the context and meaning of the word. That's why embeddings are so powerful. When you perform mathematical operations with them, you're essentially blending those textures to create new textures.

When we say AI models can only understand numbers, we mean this. The overly simplified statement can lead to misunderstandings. We should use terms like high-dimensional textured numbers, or something similar, but that would make it more confusing, hence the simplification.

Everything is an object. From an object-oriented perspective, AI models are not much different whether they're textual, visual, or audio. They're all objects doing what objects do: inherit, polymorph, encapsulate, and so on.

Take a 768x768 image, for example—a common resolution for image generative AI models. You can generate an image using only text (prompt) or using both text and image (base image). The text part follows almost the same process as a language model does, just on a smaller scale. Language models are trained on text, not images, but image generative models are trained on both text and images. They're essentially good at matching text to images.

Even the image part is converted to tensors. When starting with an empty canvas (text-only or text-to-image workflow), the canvas, or latent space in AI lingo, gets initialized with zeros: 768x768 pixels of zeros. When given a base image (I2I or image-image workflow), that base image is converted to tensors and fed to the latent space through the process of encoding. The resulting tensors vary according to the strength of the base image you're using—how much influence you want the base image to have on the final image.

You see three zeros as a bunch since we're creating a color image with three channels: R, G, B. If you add an alpha channel, you'd see four zeros.

But, as with interim forms of text, image generative AIs only deal with tensors, not pixel data themselves. If you see numbers ranging from 0 to 255, for instance, that means normalized pixel data with 256 possible values. The model doesn't understand pixel data as it is; it's converted to tensors, then fed to the model.

When we fetch the result from the model, we get tensors. We need to convert them back to pixel data to visualize them. The tensors are converted to pixel data through the process of decoding. The resulting pixel data is the final image.

Essentially, the inner workings under the hood are much the same as with language models. The difference is the scale and the complexity of the tensors.

Again, everything is an object. Other modal models, like audio and video, follow the same process.

As a rule of thumb, the more numbers you see after the decimal point, the more complex and precise the model is. This is called precision. The more precision, the more accurate the model is. But it's not always the case—sometimes, less precision is better. It's a matter of trade-off between precision and speed.

You round off complex decimal numbers to simplify calculations. The same applies to AI models. This process is called quantization. It's a way of simplifying complex numbers to simple numbers, compressing the model. The more you quantize, the more you compress the model, but you lose precision.

The day will come when we won't care about how much compute we need to run full precision models (currently, this usually means 32-bit floating point). For now, we do have to care, which is why we need to quantize models. Simply put, you want MP3s of AI models, not lossless WAVs.

The takeaway here is that computers only understand numbers. However, when this statement applies to AIs, it refers to high-dimensional, textured numbers, commonly called tensors. And GPUs, by design, are significantly faster at handling tensors than CPUs.