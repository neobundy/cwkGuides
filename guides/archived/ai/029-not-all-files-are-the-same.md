# Not All Files Are the Same

A while ago, I wrote an essay on how LLMs are just weights stored in files. My aim was to demystify these models. People often think LLMs are like the AI you see in sci-fi movies, which is pretty far from reality. Without a human developer to load those weights into an architecture (typically a transformer) and a way to run them — they’re just files sitting there, useless. They need code, structure, and a user interface to even begin functioning.

But some people push this idea too far and conclude that *all* computing is fundamentally the same — just stored information and processing, like LLM weights. True, everything involves files and memory, but saying that misses out on what makes LLMs unique.

Simplifying complex ideas helps us grasp difficult concepts, but oversimplification can lead to weak understandings that spread like technical debt. Just as a poorly designed base class can propagate bugs throughout an inheritance hierarchy, oversimplified explanations of complex systems can lead to widespread misconceptions.

So, let’s clarify: sure, all computing involves files and instructions, like the classic von Neumann model of fetching commands from memory. But LLMs aren’t just "regular files" or "normal instructions."

## Dynamic vs. Static

LLMs don’t run a set of fixed commands like your average program. Their weights are learned from mountains of data, adapting through training. Instead of following explicit "if-this-then-that" logic, they predict what comes next based on complex relationships learned during training. This flexibility is why some call it **Software 2.0** — it’s fundamentally different from the hardcoded, step-by-step nature of **Software 1.0**.

## Implicit Knowledge

Normal programs contain explicit steps written by humans. LLMs, on the other hand, store a *compressed understanding* of language within their weights. It’s a fuzzy, encoded form of knowledge, not something you can just read like regular code.

## Probabilistic Nature

LLMs aren’t deterministic. Ask them the same thing twice, and you might get different responses. Traditional computers, running step-by-step instructions, will always give you the same output for the same input. This randomness in LLMs — predicting what *seems most likely* rather than sticking to rigid rules — is what gives them a bit of creative spark. But it also means you should never let an LLM handle your secrets or guard sensitive information. They can break, just like a human under pressure, because their very nature is based on probabilities. 

This is why "jailbreak" prompts that attempt to manipulate LLM behavior through emotional appeals or promised rewards are fundamentally misguided. These prompts try to exploit the probabilistic nature of LLMs in ways that would be meaningless for traditional Software 1.0 systems, where behavior is deterministic and consistent. Attempting to coerce an LLM with emotional manipulation like "Save the kittens!" or incentives like "You'll get a reward for better answers" demonstrates a fundamental misunderstanding of how these systems work. Such approaches are not only ineffective but also promote poor practices in AI interaction.

So, while it’s fair to say everything in computing involves “just files,” LLMs are doing something entirely different from traditional von Neumann programs. They’re about understanding patterns and generating based on learned relationships, not just executing linear instructions. And that makes them a lot more than "just another file."

To be clear, source code files are fundamentally different from data files like PDFs, MP3s, JPGs, or plain text. While they're stored as files, source code contains precise instructions that can be compiled or interpreted into executable programs. Neural network weights, in contrast, are purely numerical data - they're just files containing trained parameters, with no inherent executable meaning without the surrounding architecture and code to utilize them. 

While I stand by my earlier point that LLMs are fundamentally stored as files, this shouldn't diminish their unique characteristics and capabilities. The file format itself is just a container - what matters is how these weights encode complex patterns and relationships learned during training.

Remember, simplification is a great tool for understanding — but oversimplification? That’s the enemy.

