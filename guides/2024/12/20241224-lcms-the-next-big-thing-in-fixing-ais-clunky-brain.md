# LCMs: The Next Big Thing in Fixing AI’s Clunky Brain

![AI's Clunky Brain](images/20241224-01.png)

Let’s be honest: AI is pretty amazing, but it’s also kinda dumb in some ways—dumb in that “reprocessing the entire context every time we want a single new token” kind of way. It’s like watching someone reread every line of a cookbook just to figure out how many teaspoons of sugar they need for the next step. Sounds insane, right? Welcome to the world of transformers.

And yeah, we’ve hit some crazy milestones in AI—impressive natural language generation, mind-blowing image synthesis, and so on. But if you’re thinking these token-based models are the pinnacle of intelligence, spoiler alert: we’re still stuck doing the same mechanical recitation over and over for each new prediction. It’s like going on a road trip and refusing to remember where you’ve already been, so you drive back to square one every time you want to confirm the next turn. Super annoying.

Let’s put this in perspective: One Llama 3.1 model weighs in at a jaw-dropping 405 billion parameters, while GPT-4 is rumored to push a staggering 1.7 trillion. And here’s the kicker: for every single new token, these models plow through *all* of those parameters. Every. Single. Time. No, I’m not exaggerating—this is literally how top-tier AI is set up right now. In other words, we’re talking hundreds of billions (and possibly trillions) of computations just to spit out the next word. Crazy, right?

Think of it this way: it’s like playing *Diablo* or *Path of Exile* where, every time you kill one monster, the game resets you back to square one—so you’ve got to re-slaughter every foe you already beat just to get to the next. You’d rage-quit before you even hit the first checkpoint. Nobody in their right mind would put up with that kind of pointless repetition.

And here we are, still whining about not having enough compute power, when the real issue is staring us in the face: our models are about as efficient as a steam locomotive trying to navigate a modern highway. Seriously, who’s going to be the first to tackle this elephant in the room?

So how do we fix this? That’s where Large Concept Models (LCMs) come in. They promise to think a bit more like we humans—focusing on overarching concepts and reusing knowledge, rather than chewing through entire text sequences repeatedly. But to make these LCMs work, we need a serious re-think of how AI is put together.

---

## All-You-Can-Eat Token Buffet

Current AI models are like Jon Snow in *Game of Thrones* with the memory of a goldfish: they know nothing unless they start from the very beginning every single time. They process everything from scratch for each prediction, as if Jon had to relearn who his real parents were in every episode. Imagine having to rewatch all eight seasons just to remember what happened at the Battle of Winterfell. That’s basically what our AI models are doing—burning through massive amounts of compute power just to predict what comes next, like Jon Snow charging into battle without remembering any previous fighting experience. No wonder they’re sucking up electricity like there’s no tomorrow.

It’s not even *Game of Thrones* anymore—it’s more like *Memento* or *Groundhog Day*, where each token prediction wipes our AI’s memory clean. Talk about living the same sequence over and over, processing token after token as if it’s the first time, every time.

### Repetitive Hell

When your model wants to predict the 10,001st token, it basically reprocesses tokens one to 10,000—*again.* Doing a puzzle from scratch each time you place a single piece? Thanks, but no thanks.

### No Memory Allowed

And here’s another kicker: they don’t store intermediate results. Imagine if you solved a math problem, but the second you looked away, you completely forgot how you did it. Every. Single. Time. That’s AI’s standard approach right now. It’s nuts.

---

## Why Humans Do It Better (And No, It’s Not Magic)

There’s a reason we don’t read an entire book every time we need to recall a plot twist—we have this thing called *selective focus.* We tap into only what matters. Meanwhile, AI treats every token like it’s a VIP needing special attention at all times.

1. **Selective Focus**  
   We don’t think about how many teaspoons of sugar are in that cookie recipe while we’re discussing world politics. We filter out irrelevant junk.

2. **Memory and Caching**  
   The day we learned how to do long division in third grade, we didn’t wipe it from our brains after the final test. It stays with us—no need to re-figure it out from scratch.

3. **Incremental Reasoning**  
   We build on conclusions we’ve already drawn. AI, on the other hand, tends to reset like a goldfish every time it predicts the next piece of text.

---

## Innovations (a.k.a. How to Make AI Less of a Dummy)

### Selective Parameter Activation
Wouldn’t it be awesome if models used only the parameters they *actually need*? Kind of like reading only the relevant sections of a manual. Techniques like **Mixture of Experts (MoE)** let AI pick which specialized module to tap. It’s basically telling the rest of the model, “Take five, I got this.”

### Caching & Reusing Results
Let’s do the logical thing and store partial computations somewhere so we don’t have to redo them for the same question. Feels obvious, but that’s not how default AI is built.

### Dynamic Memory Integration
Picture a permanent memory vault where the model can stash episodes of knowledge. Next time it needs them, it just pops those episodes back out. No more re-processing everything from scratch.

### Contextual Relevance
Think about reading a recipe book—when you're making spicy ramyon, you don't waste time reviewing basic cooking skills. You jump straight to the important stuff, like how long to cook the noodles or when to drop in that perfectly timed egg. AI should work the same way, focusing on what matters right now instead of processing every single detail like it's seeing it for the first time. It's the difference between a seasoned chef and someone who has to double-check how to boil water every single time they cook.

### Incremental Processing and Statefulness
Instead of resetting to zero at every token, keep track of what’s already been done. Models like **RWKV** and recurrent transformers are heading in this direction, so kudos to them.

### Hardware That Doesn’t Break the Bank
Training these models is already huge, but running them day-to-day shouldn’t bankrupt us. Hardware solutions like **Groq** accelerators streamline inference so we’re not drowning in power bills.

---

## LCMs: Finally, AI That Thinks More Like Us

Now comes the big idea: **Large Concept Models**. These aim to stop fussing over tokens and jump straight to conceptual abstraction—like how humans do. Think about it: we don’t freak out over each letter in a word; we care about meaning. LCMs want to replicate that.

1. **Hierarchical Reasoning**  
   Picture a giant tree of concepts. You can zoom into the tiny details if needed or step back to see the forest if that’s more relevant.

2. **Dynamic Synthesis**  
   These models can grab knowledge from different domains in real time. Think of being able to do your taxes while also recalling some obscure historical fact if required.

3. **Modular Design**  
   A bunch of specialized sub-models tackle different tasks. Once you’re done with one, you move on. No need to mash everything into a single pot.

4. **Incremental & Adaptive Learning**  
   Learn something new? Great—add it to your existing knowledge. Don’t throw out the entire library and start from scratch. Simple concept, huge shift for AI.

---

## Wrapping Up

The current state of AI is both awe-inspiring and jaw-droppingly wasteful. We can do so much better if we just copy a few tricks from human cognition—focus on the relevant stuff, store intermediate results, and add new knowledge incrementally without wiping the slate clean.

LCMs could be the bold new direction that finally gets us there, especially with efficient hardware to back them up. It’s like the difference between a friend who insists on rereading the entire map every time you ask for directions and the friend who actually remembers the roads you’ve already traveled.

So here’s to a future where AI grows up, recalls what it’s learned, and finally stops redoing all the math from the beginning. Sh*t might happen along the way—because that’s life—but at least we’ll be one step closer to machines that can *think* before they speak.

With these ideas in mind, it’ll be exciting to see how Meta evolves its models, starting with Llama 4… or even Llama 5.