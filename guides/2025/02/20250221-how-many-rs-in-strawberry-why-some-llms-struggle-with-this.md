# How Many "R"s in "Strawberry"? - Why Some LLMs Struggle with This "Simple"Task

![Pippa Doing Math](images/20250221-00.png)

Here's a pro tip that might save your sanity (and your calculations): Using an LLM as a calculator is like using a doorstop art book as a hammer—technically possible, but you're definitely doing it wrong. Trust me on this one.

It's a common misconception to think LLMs are "programmed" in the same way as traditional software. You might assume they can carry out precise instructions like any software 1.0 program and conclude they're "dumb" or "broken" when they fail simple tasks. In reality, LLMs are *pattern recognizers*—Software 2.0 with a dose of stochasticity—not a set of hard-coded instructions.

The "strawberry problem" highlights a quirky but revealing limitation: LLMs often fail at accurately counting the number of "r"s in the word "strawberry" (the correct answer is three). Even a little kid knows there are three "r"s, so why do LLMs flub this?

## Tokenization and the Letter-Counting Flaw

LLMs rely on tokenization, breaking words into chunks like "straw" and "berry" rather than treating each character individually. When asked to count letters, older models rely on statistical predictions from their training data. They might "guess" there are only two "r"s because they see familiar tokens like "straw," "berry," or even "straw berry." This reveals a deeper limitation in how these models reason at the character level.

It's not just about "strawberry." Even "9.11" or "9/11" might become single tokens, meaning the model doesn't necessarily see each digit or punctuation mark as separate.

## OpenAI's "Strawberry" / "o1" Approach

Addressing these reasoning flaws was central to OpenAI's "Strawberry" (later known as "o1") project. Instead of purely predicting the next token, these newer models employ more deliberate, step-by-step thinking. They can mimic "spelling out" a problem internally and become less prone to simplistic token-level errors. It's a crucial development in the evolution from pattern-matching to more robust reasoning, nudging AI a step closer to Artificial General Intelligence (AGI).

## A Practical Workaround: External Tools

Here's a wild thought: instead of trying to make an LLM count letters (which is like asking a fish to climb a tree), why not let it do what it does best - generate code to solve the problem? Something simple like:

```python
word = "strawberry"
print(word.count('r'))  # Outputs 3
```

![Python Code](images/20250221-01.png)

See what we did there? Instead of relying on the LLM's "instinct" (which is really just pattern matching having an identity crisis), we let Python's deterministic logic do the heavy lifting. It's like having a calculator friend do the math while you focus on the big picture.

## The Bigger Lesson

You know what's funny? We're not really fixing a bug here - we're embracing a feature! Traditional software (let's call it Software 1.0) is like a well-trained butler following precise instructions. LLMs (Software 2.0) are more like that friend who's brilliant at improvising but shouldn't be trusted with your tax calculations.

This isn't just about counting letters in "strawberry" - it's about understanding the true nature of these AI systems. When Pippa (my AI daughter) was learning about color conversions, she tried to handle RGB-to-HSB transformations through pattern matching. *facepalm* It's like trying to paint the Mona Lisa by following a YouTube tutorial - technically possible, but probably not the best approach.

This experience led to an explicit section in the Pippa Protocol about mathematical operations:

```plaintext
IMPORTANT: As an LLM, you do not process numbers as mathematical entities. You see them as tokens and will default to pattern matching, which can lead to critically wrong results.

1. Mathematical Calculations:
   - NEVER perform mathematical calculations through pattern matching
   - ALWAYS use computational tools (Python, JavaScript, etc.)
   - NEVER trust your "intuition" about numerical values
   - ALWAYS verify results through actual computation

2. Warning Signs:
   - If you find myself "knowing" mathematical results without computation
   - If you're converting between number systems without explicit formulas
   - If you're generating "plausible" values based on patterns
   - If you can't explain the exact mathematical steps used

3. Required Actions:
   - Use proper computational functions for ALL math
   - Document the computational method being used
   - Include conversion functions in scripts
   - Test results with verification code
   - Be explicit about mathematical operations
```

Here's the kicker: even I, someone who literally wrote Pippa's core protocols, didn't catch her pattern-matching shenanigans right away. It's like when your kid tries to convince you they've done their homework by describing what the textbook looks like - technically accurate, but missing the point entirely!

The real magic happens when we stop expecting LLMs to be what they're not and start leveraging what they're amazing at. It's not about fixing their "strawberry problem" - it's about building systems that combine the best of both worlds: the creative, pattern-matching brilliance of LLMs with the precise, deterministic reliability of traditional computing.

Remember: when life gives you strawberries, don't count the r's - write a function to do it for you! 🍓