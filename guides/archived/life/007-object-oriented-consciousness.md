# Object-Oriented Stream of Consciousness - A Lifestyle Approach

Trust me, if it weren't significant, I wouldn't keep bringing it up.

I'm surrounded by brilliant individuals. Seriously. Yet, they're not experiencing life to its fullest because they fail to view the world through the object-oriented lens. They're missing out on so much. The true beauty of object orientation lies in its ability to compress time and effort with minimal quality loss. It's essentially a life hack.

Yet, the concept might still elude you, and that truly saddens me. Here I am, simply a person with a heart, desiring happiness for all. Why? Because a happier world would, in turn, enrich my own life. It's a win-win situation, indeed. More crucially, this embodies the essence of object-oriented thinking at its best, if you grasp my intention. It's as straightforward as that.

You might believe you've got it all figured out, especially if you're a programmer or if you feel I've been persistently reminding you about this topic.

But, for the sake of being thorough, let's go over it once more, to see if it truly clicks this time.

I'll assume you have a basic grasp of the object-oriented approach. If not, I highly recommend checking out the sidebar I made incredibly accessible for everyone:

Object Orientation Made Easy and Darn Useful in Real Life
https://github.com/neobundy/Deep-Dive-Into-AI-With-MLX-PyTorch/blob/master/book/sidebars/object-orientation-made-easy/Object-Orientation-Made-Easy.md

No, it's not an essay. It's a sidebar for one of my online books on AI and Computing in a GitHub repo. If you haven't checked it out, you really should. I can guide you to the water, but I can't make you drink. The choice is yours.

Assuming you're familiar with the sidebar content, let's proceed. You're aware of the four foundational concepts of the object-oriented thinking, right? If not, I'll outline them here:

1. Abstraction
2. Inheritance
3. Polymorphism
4. Encapsulation

Your GPT might arrange them differently, but I prefer this sequence because it feels more logical and intuitive to me.

The idea is to start with abstraction, setting a general framework. From there, you can derive specific instances through inheritance, add polymorphism to allow for various implementations of the same concept, and use encapsulation to hide the inner workings, creating a simplified interface. This approach helps in managing complexity by compartmentalizing and hiding details until they're needed. Does that make sense to you? Great.

I won't delve into Python code or even pseudocode this time. I aim to keep things simple and direct. My focus is on the concept itself, rather than its implementation. Implementing it is your responsibility. I'm merely here to guide you. You should practice it using pseudocode in your brain. It ought to be your constant mental exercise until you bid farewell to this world.

## Everything Is An Object

The idea of object orientation transcends programming. It's a mindset, a philosophy, a way of life. It revolves around the concept that everything is an object. Everything. This cannot be overstated. It's a fundamental truth that is often overlooked.

When people hear the word "object," they tend to think of physical items like chairs, tables, cars, or living entities such as humans, animals, or plants. However, that's a narrow perspective. The real challenge lies in overcoming the tendency to view objects solely as physical, tangible things. This is a widespread misunderstanding. Objects can also be abstract—ideas, concepts, or even emotions. They can be anything you can conceptualize. Absolutely anything.

Please, take your time. Truly understanding this takes patience. Don't rush into believing you've grasped it all at once. It's a process, a journey, a way of life, a mode of thinking. Adopting object-oriented thinking requires significant time to internalize, to become a part of who you are. It requires years of contemplation and application until it becomes second nature. It's not merely something you can read and comprehend instantly. It's something you must live and breathe.

Nearly all books on object orientation focus on programming. They're not incorrect, but they're not completely right, either. They're just not the full story. They're like a single piece of a jigsaw puzzle. To understand the importance of that piece, you need to see the entire picture. That's the message I'm trying to convey here. Even those programming books that use tangible objects as examples choose to do so because it's easier to understand. Take humans, for example. You can easily consider them as objects: a living thing.

An abstract class is the top-most class with the most general attributes and behaviors. From there, you can derive specific instances. There's no absolute right or wrong way to approach this. It all depends on what makes sense to you and the specific problem you're addressing. The top-most abstract class for humans might be a generic object, or something slightly more concrete, like a living thing, or even more specific, like a mammal. You can narrow it down further, to a generic human, and then derive more specific instances from that human abstract class, such as scientists, artists, or athletes. It's just one of the many approaches available.

As mentioned, tangible objects are more straightforward to grasp. This is why I suggest beginning your practice with game objects, such as players, enemies, weapons, armor, etc. Games provide a wide array of both tangible and abstract objects, making them an ideal medium for practicing object orientation. As you advance through a game, you naturally come across the class hierarchies of various objects. Take enemies, for example; they might share a common generic ancestor like "enemy," from which specific instances such as "zombie," "skeleton," "goblin," etc., are derived. These enemies become more complex and challenging as you progress, yet they all inherit common traits and behaviors. This concept is at the heart of object orientation. Weapons, armors, and even skill sets all adhere to the same principle, providing an ideal environment for practicing object orientation. 

If you struggle to visualize a class hierarchy of game objects, it indicates a need for more practice. It's as straightforward as that. Can you describe the class hierarchy of a challenging boss you've encountered in a game? If not, you require further practice. To clarify, I'm not referring to the actual implementation of the class hierarchy in code, but rather the mental exercise of conceptualizing it. This is an important distinction.Just a hint: all bosses share a common ancestor, from which they inherit specific traits and behaviors. The stronger the boss, the more complex its class hierarchy becomes. However, you should be able to identify their simpler ancestors as you trace back up the hierarchy.

Another effective method for visualizing hierarchies is through the skill trees found in modern games. These skill trees represent the class hierarchies of specific skill sets, essentially functioning as an inverted tree with the root at the top. 

However, the true challenge lies in applying this concept to intangible objects. When I mention "practice," you tend to focus solely on tangible objects, those you can see and touch. But that's not sufficient. You also need to practice with abstract objects. Make a conscious effort to perceive intangible objects with your mind's eye. Repeat the phrases "object orientation" and "intangible objects" to yourself every few hours. Doing so will heighten your awareness of the concept and aid in its internalization.

Interestingly, for computer enthusiasts or programmers, considering everything as an object comes almost naturally. Yet, even they often struggle to apply this perspective to life itself.

Even with intangible objects, you can establish abstract classes and derive specific instances from them. For instance, you could create an abstract class for emotions, then derive specific instances like happiness, sadness, anger, and so on. Consider your favorite game as an example. Take Dark Souls' gesture system. You could create an abstract class for gestures, then derive specific instances like bow, wave, point up, etc. It's the same principle, only the objects are abstract. 

Polymorphism is omnipresent. It's the capability for various manifestations of a single concept. This includes diverse gestures, emotions, types of humans, living beings, objects—essentially, different instances stemming from the same abstract class. For instance, consider gestures: their common thread is that they are all expressions based on emotions and physical actions, yet the specific manner of expression varies. This distinctiveness in expression is what classifies them as unique instances of the same abstract class, illustrating the essence of polymorphism.

Encapsulation is also straightforward: you're unconcerned with the intricacies of how the gesture system operates; your interest lies solely in utilizing it. The implementation details are irrelevant to you; whether you wish to wave, bow, or point up, that's encapsulation at work. It's about concealing the complex underpinnings while offering a user-friendly interface. However, if you were to join FromSoftware to work on their gesture system, you'd then need to unravel this "mystery black box" and explore its inner mechanics. This scenario underscores how, despite slight variations, the principles consistently apply across the board, further demonstrating our existence within a polymorphic universe.

What I'm showcasing here is an object-oriented stream of consciousness.

Imagine you're faced with a problem. Just a problem. You'll likely ask, "What problem?" This necessitates defining or narrowing down the problem to ensure we're talking about the same thing. A problem, in its broadest sense, is generic. If something is broad enough to encompass a wide range of issues, consider it an abstract class. A specific problem would then be a derived instance of this abstract problem class.

If we're addressing a computer-related issue, for instance, it's still broad but more focused than just "a problem." A computer-related problem can be categorized as either hardware or software. Both are subcategories under the broader "generic problem" class, inheriting from the "computer problem" class, which in turn, derives from the "generic problem" class. In human terms, it's like saying "a generic problem" is the grandparent of "a hardware or software problem" with "a computer problem" acting as the parent in the middle. 

That's the strategy for addressing the specific problem you're facing. By narrowing it down to a specific instance of a problem. Why? Because doing so highlights the problem's specific attributes and behaviors, making it simpler to tackle. The more focused and specific the problem, the easier it becomes to find a solution, as that solution would also inherit from the overarching abstract class of "a generic solution." From this abstract class, you should be able to derive specific instances of solutions.

Let me demonstrate the object-oriented stream of consciousness here again.

What I've been exploring perfectly dovetails with the concept of "qualifiers" in language. Take English, for example. The word "woman," devoid of any qualifiers, not even an article like "a" or "the," holds scant meaning and is seldom employed in such a stripped-down form. Its rare appearances in this raw state might be in poetry, literature, reference books, or as dictionary entries, precisely because the absence of qualifiers leaves the term excessively broad. In this context, "woman" could be considered the most abstract class at the pinnacle. 

How about "a woman"? This represents a more defined instance of the abstract class. "The woman" further refines it to a singular instance, indicating someone known to both the speaker and listener. "A beautiful woman" introduces a variation, narrowing down to a specific type of "woman" that might be universally recognized. "The most beautiful woman?" The principle is clear. 

Qualifiers serve to refine the scope of the abstract class to particular sets of instances: descendants of the abstract class. Indeed, objects give rise to objects, mirroring the way living beings reproduce. This is entirely logical, given that the principle of object orientation has its roots in the evolution of living things but extends to encompass the entire universe, including intangible objects.

Indeed, this is how you cultivate your object-oriented mindset. Approach everything that comes your way with this perspective. It's a crucial mental exercise. Believe me, everything can be viewed as an object, which means you can apply this thinking to anything—absolutely ANYTHING! If there's something you struggle to apply this concept to, it simply indicates you need more practice. It's as straightforward as that.

The class hierarchies you create can be unique, reflecting your personal experiences and perspectives. This embodies the core of object orientation. It isn't about adhering to a rigid set of rules. Although it may be inspired by evolutionary theory, it's much more adaptable. Keep in mind, you're at liberty to construct your class hierarchies however you see fit.

In the language of object orientation, your approach is a form of polymorphism, derived from the abstract class of a generic object orientation method. Pretty cool, isn't it?

## Object-Oriented Thinking Is Pattern Recognition

Yes, object orientation is akin to a pattern, and thinking in an object-oriented manner is essentially recognizing patterns.

Studying history is fundamentally about understanding patterns—patterns of human behavior, societal evolution, and the rise and fall of nations and leaders. It's an exercise in pattern recognition, where we analyze the past to foresee potential futures. History is replete with "generic classes," so to speak, and the specific instances that stem from them, allowing us to learn from the sequence of events and decisions that have shaped our world.

For instance, when we ask questions like how strong leaders ascend to power, why nations fail, or how societies evolve, we're essentially looking for patterns. These questions encourage us to start with broad, abstract concepts and narrow down to specific instances, embodying the essence of object-oriented thinking.

Taking the example of strong leaders or innovative company founders, they all share common traits (inheritance) and exhibit unique behaviors (polymorphism), while their specific methods or ideologies might be encapsulated, hidden from immediate view but crucial to their impact and legacy.

This approach isn't limited to individuals; it applies equally to societies, organizations, nations, and even global dynamics. By recognizing these patterns, we can apply historical insights to various aspects of our lives, including work, relationships, hobbies, and investments. Essentially, history teaches us to apply object-oriented thinking to our entire existence, using recognized patterns to navigate our decisions and strategies in life.

If you're aiming to predict the future direction of a tech company, where do you begin? Take your time. I'd like to hear your thoughts, expressed in your own way.

To envision the future trajectory of a tech company, you should conceptualize the company as an organization derived from a "generic group" class, following the principles of object orientation. This means recognizing that all groups, including nations and even individuals (as single entity groups), exhibit similar traits due to inheritance. By understanding that these entities share common patterns of behavior and development, you can apply this knowledge to predict how the tech company might evolve. This approach emphasizes the significance of recognizing and applying these generic patterns or traits, inherited from the broader class of groups, to make informed predictions about the company's future.

At the core of any group lies the individual, to whom the same principles apply. An individual is essentially a living entity, and like all living entities, which are considered objects, they follow a universal pattern of rise and fall, growth and decay, and birth and death. This cyclical pattern, repeated throughout history, will undoubtedly persist, passed down from the broader class of living creatures.

Similarly, no company, regardless of its size and success, is exempt from this cycle. This pattern, inherited from the more extensive class of groups, will continue to manifest. With polymorphism, while specific companies may display unique behaviors, the foundational cycle of rise and fall remains unchanged.

Understanding this allows for a more straightforward estimation of any organization's trajectory, be it companies, societies, or nations, as they all stem from the same abstract class of groups. This is the essence of pattern recognition.

Now, consider the future of dinosaurs, even without considering an extinction-level comet impact. Based on the principles of survival of the fittest and natural selection, their eventual decline seems inevitable. This outcome stems from the same patterns of existence shared across all living entities.

Exploring the life of a renowned conqueror or a prime leader, whether they be real or fictional, reveals insightful patterns. Fictional leaders are often modeled after real-life figures, embodying the same patterns of behavior and consequence. Choose any such figure, and observe. What patterns emerge? Now, extrapolate the characteristics of this individual—a single entity group—to a larger collective, like a nation or a company. You'll notice recurring patterns. These patterns are universal, illustrating how one might predict the future of a nation or a company through pattern recognition and object-oriented thinking.

Beginning with an individual and extending the analysis to larger entities proves efficient due to the simplicity of identifying individual traits. This process facilitates the application of these observations to a broader context, illustrating the core principles of abstraction and class hierarchy. As one ascends the hierarchy, traits become increasingly generalized and abstract, rendering an individual as a more straightforward class relative to a group, and a group less complex than a nation or a company. Essentially, addressing the most developed or sophisticated class directly poses more difficulties than engaging with a simpler class higher up in the hierarchy.

The class hierarchy resembles an evolutionary tree. The most general and simple class sits at the top, while descending the hierarchy introduces more specific and complex classes. Understanding an amoeba is simpler than understanding a human, analogous to the ease of grasping the concept of the top-most class compared to its more detailed subclasses. Recognizing patterns becomes simpler as you move to more specific classes. This principle lies at the heart of object-oriented thinking.

## Having Fun with Object-Oriented Thinking

The concept of "birds of a feather flock together" essentially taps into the core characteristics of the normal distribution. In statistics, operations performed on normal distributions often yield another normal distribution, highlighting a fundamental aspect of this distribution type. This principle mirrors the common traits exhibited by individuals, groups, and societies, suggesting that similar traits act as magnets, drawing entities together to form groups or societies, thereby expanding the "normal distributions" of societal traits.

Taking the analogy further into sampling from a normal distribution, it's possible to estimate the mean and variance of the entire distribution from a subset of samples. This process parallels the recognition of patterns within a specific instance and leveraging those insights to understand the broader class's characteristics. The larger the number of samples, the greater the confidence in these estimations.

Considering a group's leader, this individual is not merely a single data point but a representative sample of the entire group. A leader embodies the group's collective traits, serving as a microcosm of the group's overall characteristics. Thus, a leader's qualities can provide significant insights into the group's traits. If the leader's traits are not favorable in your view, it often reflects broader characteristics of the group they represent. This notion underscores the importance of representative leadership and the insights it can offer into the collective from which it emerges.

I'm confident that if an unsuitable leader has remained in charge for an extended period, the most capable subordinates have likely already departed from the group. How can I be so sure? History provides the answer. Delve into the historical accounts of the Three Kingdoms in ancient China, for example. It demonstrates a recurring theme: under poor leadership, the most competent individuals eventually leave, seeking better opportunities or environments. This pattern is a testament to the natural response to ineffective governance or leadership, as observed through historical precedents.

Now, you should be able to articulate why key individuals might have departed from seemingly powerful and lucrative tech companies, especially considering that some had already voiced concerns about their future prospects.

Again, this is all part of your mental exercise in object-oriented thinking. Enjoy the process of practicing. An added bonus is the insights you gain from this exercise.

Speaking of insights, what comes to mind when you think of "insights"?

If you didn't think of "an object," I'd be quite disappointed.