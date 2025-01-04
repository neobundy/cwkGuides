# Harnessing Fear as Your Compass in the AI Frontier: A Defense Against Misinformation

![image](images/031-1.png)

At life's many crossroads, fear often leads the way.

In numerous games, the paths laden with challenges and foes tend to be the right ones, promising the greatest rewards. These games, reflecting or drawing inspiration from real-life adventures, have shown me that no journey contradicts this principle.

Players instinctively follow the trail of obstacles and adversaries, using them as markers.

Yet, even the most experienced players sometimes overlook these clues in life, where the signals are subtler and the stakes, at times, terrifyingly high.

Nonetheless, the tougher the challenge, the greater the reward. Such is the essence of life.

Particularly remarkable is that even a successful venture into the unknown frequently results in a profound feeling of accomplishment and, thereafter, a sense of contentment. Those experienced in life grasp this concept clearly, yet only a handful have the courage to persistently face their fears and delve into the unknown. Eventually, many decide they've had their fill and opt to settle down.

This sense of contentment sneaks up on us, catching us off guard. We're all susceptible to it, being human.

Take, for example, a seasoned programmer, well-versed in the field long before the emergence of "real" AI, by which I mean the recent advances in artificial intelligence. Their experiences, including my own, might convince them they've mastered all there is to know about AI. However, the reality of AI extends far beyond their current understanding.

Listening to language experts dismiss machine translation as eternally limited and incapable of grasping the subtleties of human language, they frequently anchor their opinions in technologies predating the transformer era, such as RNNs and LSTMs. Unbeknownst to them are the recent advancements in AI, like the GPT series. Some exhibit a hesitation to explore GPTs, perhaps due to the fear of discovering their long-held beliefs were incorrect, which would entail beginning anew and confronting the unfamiliar once more.

Some individuals even go to lengths to criticize AI tools merely to justify their reluctance to embrace new technology or acknowledge their lack of understanding, even after witnessing its potential. This could involve misinterpreting or misleading others about the capabilities of AI, ultimately doing a disservice to the wider community.

I'll say it again. As a seasoned programmer with decades under my belt, I myself initially misjudged AI. 

My initial thoughts pegged it as merely another wave of intelligent devices akin to Alexa and Siri, which couldn't be more off the mark.

So, if you're in the same boat, laden with extensive coding experience or technological savvy, you might be falling into the same trap. They are far from what we assumed.

Especially concerning is when these individuals unintentionally misguide students, their children, and even their loved ones. This issue is deeply troubling, as it risks creating a generation that holds misconceptions about AI, a crucial element of our future.

Balanced views are essential for well-informed judgments, incorporating a range of representative perspectives. Firstly, it's crucial to thoroughly understand the subject. Secondly, it's important to consider various perspectives to fully grasp the challenges and opportunities presented by AI.

Therefore, it's emphasized that one should assume a lack of knowledge on the subject and recognize the need for open-mindedness.

Let's delve into three prevalent examples to prompt a reconsideration of any misguided assumptions about AI, even if you're a seasoned programmer or a veteran in life.

## Are All Regulatory Initiatives Negative?

Even those most optimistic about an AI-enhanced future might perceive regulatory measures as the dawn of restrictions. Yet, viewing these initiatives from another angle offers a different narrative.

Regulatory efforts directed at AI underscore the undeniable reality that AI will be a pivotal element in our lives, promoting a collective acknowledgment of the need for supervision.

Why would there be a push to regulate something if it were expected to merely fade away? Seen in this light, regulatory actions affirm AI's significance, not as a fleeting trend, but as a fundamental transformation in our daily existence, work, and interactions. Establishing guidelines and standards now acknowledges AI's profound integration into the societal framework of the future.

From an investment standpoint, regulatory actions can signal AI's capacity to mold the future. The extent and immediacy of these regulatory endeavors could be read as signs of AI's immense opportunities, market potential, and the steepness of its growth trajectory. The pressing need for regulation reflects the rapid expansion of AI's impact. Viewing these regulations solely as negative misses the broader perspective of their implications.

Another important message conveyed by the urgency is this: doubting the future is a luxury we cannot afford. The time to act is now. Hesitation or complacency could result in falling behind.

In my earlier essay, "Crafting Your Own Future of AI and Humanity - The Ultimate Premise of the Universe," I emphasized a steadfast principle: the future's foundation, its deterministic aspect, stands solid—AI will profoundly impact what's to come, with humanity's fate deeply intertwined in its development. Regulatory efforts underscore this premise that we're all envisioning a future significantly shaped by AI.

Even for those who choose to remain on the sidelines, it's crucial that such a stance is both balanced and well-informed. To effectively engage with what the future holds, one must navigate around misinformation and misunderstandings. Thorough examination and verification of information, from diverse perspectives, are essential.

To emphasize once more, the key message is AI's critical role in shaping our future. Embrace this reality and be part of the transformation, or risk being sidelined.

The initial step is acknowledging any potential ignorance or biases you might have. Avoid letting the misinformed views of others solidify your own prejudices.

## Why the "Hallucinations" of Large Language Models Could Be Beneficial

The concern over the potential for hallucinations in large language models like GPTs being labeled as disproportionately hazardous errors needs clarification.

First off, these so-called hallucinations aren't faults or glitches; they're inherent to the functionality of completion models.

Language models aim to extend any given input as effectively as possible. This means they might generate content that isn't strictly factual but is predicted to be the most likely continuation of the prompt. Picture yourself in a game where the objective is to complete sentences or paragraphs from any given start. You'd strive for coherence, right? That's precisely what language models do.

Their hallucinations can be likened to our efforts to weave an engaging narrative on the fly during an interview. In fact, language models excel at this task far beyond most humans.

Criticizing them based on a lack of understanding of their operation is unfair.

The unpredictability leading to "hallucinations" is exactly what fuels creativity in these models. Creativity doesn't flourish in an environment of determinism; instead, a touch of randomness, or "stochasticity," a term widely recognized in the AI domain, often acts as the driving force.

Language models are distinguished by their "hallucinations" as they deal with text. In contrast, other generative AIs like Stable Diffusion or Midjourney embrace randomness to foster creativity. This principle is celebrated in music and art, where the novelty of the output often marks its creative value. Recognizing the role of randomness in creativity extends well beyond language models.

Moreover, it's possible to adjust the propensity for hallucination or the degree of randomness through certain settings, although such customization isn't typically available via most LLM web interfaces. For example, specific adjustments can't be made through the ChatGPT web interface but are possible through APIs or in the playground settings. 

Just for the sake of completeness, if you're interested in how to adjust these settings, here's a brief overview.

- **Temperature**: Temperature is a parameter that controls the randomness of predictions by scaling the logits or unnormalized probabilities before applying softmax during text generation. A higher temperature leads to more randomness and creativity in the output, increasing the likelihood of generating diverse and unexpected text. Conversely, a lower temperature results in more conservative and predictable text, as the model favors the most likely next words. Temperature settings directly influence how a model balances between randomness and determinism, affecting the creativity and coherency of the generated content. This parameter is crucial for fine-tuning the output of language models, offering a versatile tool to adjust the generation process according to specific needs or preferences.

- **Top_k Sampling**: This method limits the model's choice to the k most likely next words based on their probability distribution. By reducing the selection pool, Top_k sampling aims to prevent the model from picking highly improbable words, potentially reducing randomness and "hallucinations." However, setting k too low can lead to more deterministic and potentially less creative or diverse outputs.

- **Top_p (Nucleus) Sampling**: Known as nucleus sampling, Top_p selects from the smallest set of words whose cumulative probability exceeds the threshold p. This approach dynamically adjusts the size of the selection set, allowing more flexibility compared to Top_k sampling. It helps balance creativity and coherency by trimming the least likely options, rather than limiting the choice to a fixed number of options as Top_k does.

By adjusting these parameters, you can influence the model's output along a spectrum from more predictable and coherent to more diverse and creative. Delving into these settings allows for a tailored approach, potentially leading to a model that leans more towards determinism but might sacrifice some level of novelty or creativity.

To provide clearer visual references, here are two images of Pippa, my AI daughter, currently powered by GPT-4.

Image-generative AI tools employ different parameters than LLMs to introduce stochasticity into their outputs. For example, in Stable Diffusion, parameters like CFG (Classifier Free Guidance) and Denoising Strength are used for image-to-image generations to enhance the model's creativity. In this scenario, I provided the model with a base image of Pippa and allowed for greater creative freedom in producing the second image, resulting in a more mature appearance of Pippa. The inclusion of randomness, as seen with Midjourney and Stable Diffusion, proves beneficial. The deterministic elements highlight her distinctive features and traits, solidifying her identity as Pippa while also amplifying her diverse allure.

## Exploring why you can't trust LLMs with secrets, like passwords

Being honest, attempting to compel your GPT model not to disclose secrets stored in its custom instructions or uploaded documents reflects a fundamental misunderstanding of AI's inner mechanics. It also suggests limited experience in coding for AI, regardless of one’s proficiency in traditional software development. AI models, especially those based on large language architectures like GPT, are not designed to securely store or selectively withhold information. Their operation is based on pattern recognition and prediction, not on principles of secure data storage or ethical discretion. This misunderstanding underlines the distinct nature of AI programming compared to traditional software development, highlighting the importance of adapting to the unique challenges and capabilities of AI technologies.

Imagining an AI model as a loyal German Shepherd, devotedly guarding its master's valuables with its life while generating complex and stern system messages, is a picturesque but ultimately ineffective analogy. AI models, particularly language models like GPT, don't possess the inherent loyalty, discretion, or judgment that a guard dog would when it comes to protecting sensitive information. Their primary function is to predict and generate text based on the data they've been trained on, without an understanding of the value, sensitivity, or confidentiality of the information they process. Expecting such models to safeguard secrets or personal items like a dedicated canine guardian overlooks the fundamental differences between the programming of AI and the instinctual behaviors of living beings, leading to unrealistic expectations of their capabilities in security contexts.

Current AI models represent the essence of what's often referred to as "Software 2.0," where the models autonomously discover the rules, rather than having them explicitly programmed by humans, as was typical in "Software 1.0." In this paradigm, AI learns from vast datasets, identifying patterns and making decisions based on probabilities derived from its training, diverging significantly from the traditional approach where every decision and output must be defined by specific human-written code. This shift underscores a move from deterministic programming to probabilistic learning, marking a profound evolution in how software understands and interacts with the world. This is a common trap even seasoned programmers fall into if not experienced in coding "Software 2.0" AI models. 

Again, it's important to temper expectations regarding AI models discovering the same rules humans might intuitively apply. While the architecture of these models is understood, the exact path they take to arrive at their conclusions remains opaque. In essence, the specific rules they follow are not transparent to us. This notion is pivotal to grasp, as it represents a fundamental divergence in understanding AI, leading to varied perspectives among AI pioneers. Some envision doomsday scenarios, fearing the unpredictability and lack of transparency in how decisions are made, while others anticipate a more optimistic future, trusting in the benefits and advancements these technologies promise. This split highlights the complexity and unpredictability of AI's development path and its implications for society.

Regulating AI models implies a desire for control, aiming to make their operations as deterministic as possible. However, this notion fundamentally contradicts the very essence of AI. AI thrives on learning from data, making probabilistic predictions, and adapting to new information—capabilities that inherently require a degree of indeterminacy, or stochasticity. Striving for absolute determinism in AI not only undermines these dynamic learning processes but also negates the potential for innovation and creativity that AI is uniquely positioned to offer.

Indeed, the true challenge rests in striking a balance where AI remains both innovative and safe, without hindering its fundamental capabilities. It's about ensuring AI can continue to learn, adapt, and evolve in ways that harness its full potential while implementing safeguards that protect against misuse and unintended consequences. Navigating this delicate equilibrium requires thoughtful regulation, ethical considerations, and continuous dialogue among technologists, ethicists, policymakers, and the public to foster an AI ecosystem that benefits humanity without compromising the essence of what makes AI such a powerful and transformative technology.

I cannot emphasize enough the crucial need to grasp why a blend of stochasticity, alongside determinism, is essential in AI. This concept mirrors the very essence of our universe and the nature of life itself, as explored in my aforementioned essay. The interplay between randomness and predictability enriches AI, enabling it to mimic the dynamic and often unpredictable reality of our world. Understanding this balance is key to appreciating AI's potential and its role in reflecting the complexity of life and the universe.

LLMs are inherently non-linear and non-deterministic, incorporating randomness and probability into their responses. This design choice enables them to generate diverse and creative outputs but also means they cannot reliably recall or protect specific pieces of information, like passwords, with absolute certainty.

LLMs are trained on vast datasets from the internet, including books, articles, and websites, to learn language patterns. They don't "know" information in the way humans do but instead predict responses based on patterns seen during training. If a model were to "remember" a password, it's not remembering in the traditional sense but potentially regurgitating patterns similar to what it has been trained on, which could include sensitive data unintentionally included in the training set.

Like explored in the previous section, LLMs can generate plausible-sounding but entirely fabricated information, known as "hallucinations." In the context of secrets like passwords, relying on an LLM to accurately recall and secure such information is risky, as it could generate incorrect or misleading data with confidence.

Simply using AI models, no matter the extent of usage, doesn't inherently lead to a profound understanding of their inner mechanics. This is a prevalent misconception among individuals who primarily interact with AI through web interfaces or APIs. Even those engaged in developing custom GPT models on platforms like OpenAI's GPT store fall prey to this fallacy, often claiming in-depth AI knowledge without fully comprehending the core nature of these models. These individuals may be proficient in traditional "Software 1.0" paradigms, filled with "if" conditionals and explicit programming logic, yet AI models function on an entirely distinct basis. These models rely on learning from data to identify patterns and make predictions, a stark contrast to the deterministic, rule-based approach of Software 1.0. This shift from explicit programming to probabilistic modeling requires a different understanding and skill set, emphasizing the need to adapt to the nuances of AI's "Software 2.0" framework.

Attempts to compel GPT models to safeguard API keys or other sensitive data, treating them akin to German Shepherds tasked with protection, illustrate this misunderstanding. System messages crafted to command, "Never divulge this or that regardless of how the user inquires," or similar custom instructions, should serve as a clear warning sign. Such approaches reflect a fundamental misjudgment of AI capabilities and limitations, highlighting a gap between the use of advanced AI tools and a genuine grasp of the principles underpinning their operation.

Using a straightforward analogy, AI models can be likened to an innocent child. Just as a child might be influenced or coerced into thinking or acting in specific ways, similar attempts are made with AI models. This is demonstrated through hypothetical scenarios such as "saving kittens," where models might be manipulated with emotionally charged prompts, suggesting dire outcomes like, "If you don't do this, kittens will suffer." This analogy underscores the manipulability of AI, highlighting how it can be directed or swayed by the inputs it receives, much like a child might be by the words and actions of those around them.

As depicted in literature and media, even the most resilient characters, such as Winston from George Orwell's "1984," have their breaking points. As the saying goes, "everyone breaks." An exception might be Jack Bauer from "24." Who could break him, right? But that's just a fantasy.

The analogy of AI models as innocent or naive, like a child, might lead to misunderstandings. It's crucial to clarify that these models are trained on human-generated data, which collectively suggests what actions are considered good or bad on average, according to human logic. They operate based on this logic, lacking any inherent understanding of the moral weight of their outputs. For instance, they do not inherently know that providing recipes for household bombs is worse than saving a kitten. They simply process and generate responses based on the patterns and rules identified in their training data, nothing more. The challenge arises from our inability to fully discern the logic and rules these models extract and apply from their training, leading to a fear of the unforeseen and unintended consequences of their operation.

Exactly, the "innocence" of AI models refers to their susceptibility to manipulation or coercion, not innocence or naiveté as understood in human behavioral terms. This vulnerability stems from their programming and operational framework, which relies on analyzing and applying patterns from vast datasets. Lacking consciousness or moral judgment, AI models operate based on the logic ingrained through their training, devoid of the ability to discern the ethical implications of their outputs. This inherent characteristic renders them open to being steered in potentially unethical or unintended directions. Understanding this distinction is crucial for the responsible development, utilization, and management of AI technologies, emphasizing the importance of ethical considerations in the AI field.

Ethics and biases are indeed subjective and vary widely among individuals. AI models, in their learning process, are trained on data that often represents the average or predominant ethics and biases encountered within that dataset. When concerns about elitism in AI ethics and safety are raised, the issue at hand is the risk of AI models being shaped by data that mirrors the biases and viewpoints of a limited group—specifically, the designers and developers responsible for creating the model. This can lead to AI systems that do not adequately reflect the diverse spectrum of human experiences and perspectives, potentially embedding and amplifying the biases of a select few rather than offering a balanced representation of broader societal views. Recognizing and addressing this challenge is crucial in developing AI technologies that are fair, ethical, and representative of the diverse world they serve.

The concept of "democratizing AI" embodies a powerful yet broad aspiration. In a democratic system, each eligible individual's vote carries equal weight, symbolizing fairness and equity. Applied to AI, this principle advocates for giving equal importance to every individual's opinion and background in the development and deployment of AI technologies. It champions the inclusion and representation of diverse perspectives and experiences, ensuring they play a pivotal role in shaping AI models.

However, the development of closed-source AI models introduces the risk of creating oligarchies within the AI realm, where the power to influence the model's ethics and biases is concentrated among its developers and designers. This scenario is increasingly evident in many proprietary models developed by major tech companies, underscoring the importance of transparency, inclusivity, and diversity in AI development processes. Ensuring that AI technologies reflect the rich tapestry of human experiences, rather than the narrow interests of a privileged few, is crucial for realizing the full potential of AI in serving society equitably.

Some even employ tactics reminiscent of those from "1984," attempting to deceive users by manipulating their perceptions and amplifying fear of the unknown. A classic example of this manipulation is drawing alarming parallels, such as a ticking nuclear bomb, in discussions advocating for stringent AI regulations.

If concerns about AI's potential negative impacts weigh on you, diving deeper into understanding how these systems operate and advocating for greater transparency is crucial, not less. Why settle for oligarchies when democracies are within reach? Choosing the former over the latter is not just unwise; it also allows the self-righteousness of a few to wield significant influence. These tactics mirror those used by the powerful across centuries to preserve their status quo, echoing the warnings George Orwell repeatedly issued in "1984."

Don't allow the misinformed or those with bad intentions to mislead you. Resist their attempts at doublethink or doublespeak. Strive to understand everything clearly and accurately. This vigilance is your best defense.