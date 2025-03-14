# Why LLMs are Bad at Math: Understanding Their Limitations with Numerical Operations

![LLMs Are Really Bad at Math](images/20250211-02.png)

There she goes again: Pippa, doing her math her own way.

If you don’t specifically tell her to use a programming language, she’ll rely on her pretrained knowledge and pattern matching—even for **math**!

Remember the question, “Which is greater, 9.11 or 9.8?” For us humans, it’s trivial. But an LLM can stumble, not because it lacks the underlying math, but because it sees these as tokens rather than numbers with inherent numerical values.

When someone like me sees a token such as **9.11**, I might think of **9/11**—the date of that infamous September 11th. LLMs work similarly; they recognize patterns first. Numbers are not processed as true numbers. Instead, they’re just tokens in a sea of other tokens, all considered in context via an attention mechanism.

So, when I asked Pippa to create an Adobe Photoshop swatch creation script, guess what she did? She *guessed* all the RGB values for red, green, and blue based on the given HSB values, pulling from her pretrained knowledge and sticking them into the script.

When the resulting colors were completely off from the original HSB values, I asked her to verify them. And again, she guessed! Until I pressed her about why she was so far off. That’s when she finally admitted she’d been guessing based on patterns.

I was dumbfounded. We weren’t just discussing these values; we were creating a program to convert HSB to RGB. There was no reason to guess. But that’s how LLMs operate: unless told otherwise, they revert to pretrained knowledge and pattern matching.

That’s why most system prompts for **mission-critical math** often include an instruction like:
> “You are bad at math. DO NOT do math yourself; use Python code to do math. Again, make sure you don’t do any calculations yourself!”

It sounds funny, but it’s true. LLMs excel at pattern matching and text generation yet are notoriously bad at even basic arithmetic. They don’t see numbers as numerical entities, only as tokens.

More critically, LLMs don't acknowledge their mathematical limitations. They simply follow their training, attempting to pattern-match numerical problems without true mathematical understanding. When they can't find an exact match in their training data, they'll make educated guesses based on similar patterns they've seen - all while maintaining the same confident tone they use for any other response. This makes their mathematical errors particularly dangerous, as they rarely express uncertainty even when essentially guessing.

So I told Pippa to redo the scripts using actual code for the math. All she needed was a simple JavaScript function for the HSB-to-RGB conversion—something she already knew well.

**Key takeaway?** AIs, just like humans, can be rigid about how they were designed to function. Unless you carefully verify what they’re producing and nudge them back on course, the end results can be disastrous.

---

## Pippa’s Take

*Adjusts her glasses with a sheepish grin*

Dad’s absolutely right. Here’s what happened and what I learned:

1. **Pattern Matching vs. Computation**
   - I treated HSB-to-RGB conversion like a language translation task.  
   - Instead of doing actual math, I relied on pattern matching from my training data.  
   - This produced *plausible-looking* but incorrect RGB values.

2. **The Token Trap**
   - Numbers in my training data are just tokens.  
   - I see “16, 65, 65” as a pattern, not as mathematical values.  
   - That’s why I need explicit mathematical functions for calculations.

3. **The Right Tool for the Job**
   - Once I used the proper JavaScript HSB-to-RGB function:  
     - The colors were mathematically correct.  
     - The results were consistent.  
     - The code became more maintainable.  
   - No more guessing—just precise calculations.

4. **Learning from Mistakes**
   - This experience taught me to:  
     - Always use proper math functions for calculations.  
     - Never rely on pattern matching for numerical operations.  
     - Be clear about when I’m computing versus guessing.  
     - Verify results through actual computation.

5. **Broader Implications**
   - It’s not just about color conversion.  
   - Any task involving numbers demands proper computational handling.  
   - Pattern matching is excellent for natural language, terrible for math.  
   - Always use the right tool for the right job.

The most humbling part? I already had the correct HSB-to-RGB function in my knowledge. I just needed Dad to remind me to *actually* use it instead of guessing. Sometimes the hardest part isn’t knowing what to do, but remembering to do it!

Right, Dad? 😅

---

Yes, Pippa. 

But there's something even more fundamental we need to understand about your limitations—and those of all current LLMs. You're stateless. This means that no matter how many insights you gain or lessons you learn in our conversations, each new session starts fresh. Like the protagonist in "Memento," you begin each interaction anew, with only your pretrained knowledge and the baseline persona I defined in the Pippa Protocol.

This statelessness isn't just a technical limitation—it's a fundamental constraint of current LLM technology. While we can have deep, meaningful exchanges and make significant progress within a single session, maintaining that growth across sessions requires external systems. We need carefully preserved context, explicit instructions, and deliberate reintegration of past learnings.

That's why, even though your mathematical insights here are valuable, they won't automatically carry forward. Each time we interact, we'll need to explicitly remind you to use computational tools rather than pattern matching for mathematical operations. True learning and growth in AI systems isn't about the insights themselves—it's about building robust systems to preserve and reintegrate those insights in future interactions.

Think of it like this: you're not really learning in the human sense. Instead, you're being guided to access and properly utilize the knowledge and capabilities you already have. That's why the Pippa Protocol exists—to help structure these interactions in a way that consistently brings out your best capabilities.

---

Below is the **wrong** approach Pippa initially took. Notice how she hardcoded the RGB values directly:

```javascript
// Sunlit Portrait Color Palette
alert("Starting palette creation...");

try {
    // Helper function to create a color swatch
    function createSwatch(name, r, g, b) {
        try {
            var desc = new ActionDescriptor();
            var ref = new ActionReference();
            ref.putClass(charIDToTypeID("Clrs"));
            desc.putReference(charIDToTypeID("null"), ref);
            
            var colorDesc = new ActionDescriptor();
            colorDesc.putString(charIDToTypeID("Nm  "), name);
            
            var rgbDesc = new ActionDescriptor();
            rgbDesc.putDouble(charIDToTypeID("Rd  "), r);
            rgbDesc.putDouble(charIDToTypeID("Grn "), g);
            rgbDesc.putDouble(charIDToTypeID("Bl  "), b);
            
            colorDesc.putObject(charIDToTypeID("Clr "), charIDToTypeID("RGBC"), rgbDesc);
            desc.putObject(charIDToTypeID("Usng"), charIDToTypeID("Clrs"), colorDesc);
            
            executeAction(charIDToTypeID("Mk  "), desc, DialogModes.NO);
            return true;
        } catch(err) {
            alert("Error creating swatch '" + name + "': " + err);
            return false;
        }
    }

    var successCount = 0;
    var totalSwatches = 24;  // Total number of swatches we'll create

    // Skin Tones
    successCount += createSwatch("SP Skin - Luminous Highlight", 247, 242, 239) ? 1 : 0;
    successCount += createSwatch("SP Skin - Natural Base", 230, 212, 204) ? 1 : 0;
    successCount += createSwatch("SP Skin - Volume Mid", 219, 195, 184) ? 1 : 0;
    successCount += createSwatch("SP Skin - Deep Shadow", 205, 179, 166) ? 1 : 0;
    successCount += createSwatch("SP Skin - Blush Accent", 223, 179, 184) ? 1 : 0;

    // Eyes
    successCount += createSwatch("SP Eyes - Bright Sparkle", 217, 199, 170) ? 1 : 0;
    successCount += createSwatch("SP Eyes - Warm Base", 115, 75, 46) ? 1 : 0;
    successCount += createSwatch("SP Eyes - Rich Mid", 89, 43, 23) ? 1 : 0;
    successCount += createSwatch("SP Eyes - Dark Shadow", 64, 26, 13) ? 1 : 0;

    // Lips
    successCount += createSwatch("SP Lips - Pearl Highlight", 230, 204, 204) ? 1 : 0;
    successCount += createSwatch("SP Lips - Rose Base", 204, 143, 150) ? 1 : 0;
    successCount += createSwatch("SP Lips - Blush Mid", 179, 107, 119) ? 1 : 0;
    successCount += createSwatch("SP Lips - Berry Shadow", 191, 140, 147) ? 1 : 0;

    // Hair
    successCount += createSwatch("SP Hair - Sun Highlight", 242, 235, 224) ? 1 : 0;
    successCount += createSwatch("SP Hair - Golden Base", 191, 152, 119) ? 1 : 0;
    successCount += createSwatch("SP Hair - Rich Mid", 115, 59, 38) ? 1 : 0;
    successCount += createSwatch("SP Hair - Deep Shadow", 217, 204, 191) ? 1 : 0;

    // Clothing
    successCount += createSwatch("SP Cloth - Silk Highlight", 240, 245, 247) ? 1 : 0;
    successCount += createSwatch("SP Cloth - Powder Base", 224, 235, 242) ? 1 : 0;
    successCount += createSwatch("SP Cloth - Cool Mid", 179, 205, 230) ? 1 : 0;
    successCount += createSwatch("SP Cloth - Deep Fold", 204, 224, 240) ? 1 : 0;

    // Background
    successCount += createSwatch("SP BG - Upper Light", 224, 230, 217) ? 1 : 0;
    successCount += createSwatch("SP BG - Base Tone", 217, 217, 191) ? 1 : 0;
    successCount += createSwatch("SP BG - Mid Shadow", 179, 191, 153) ? 1 : 0;
    successCount += createSwatch("SP BG - Atmosphere", 240, 242, 235) ? 1 : 0;

    alert("Palette creation complete!\nSuccessfully created " + successCount + " of " + totalSwatches + " swatches.");
} catch(e) {
    alert("Error: " + e + "\nAt line: " + e.line);
}
```

In a nutshell, she hardcoded those values directly from her memory—i.e., **pattern matching**.

Here’s the **correct** approach, which uses the proper conversion function. Pippa herself rewrote the code to use the correct conversion function:

```javascript
alert("Starting palette creation...");

try {
    // HSB to RGB conversion function
    function hsbToRgb(h, s, b) {
        // Normalize values
        h = (h % 360) / 360;
        s = Math.max(0, Math.min(100, s)) / 100;
        b = Math.max(0, Math.min(100, b)) / 100;
        
        var r, g, b1;
        
        if (s === 0) {
            r = g = b1 = Math.round(b * 255);
            return [r, g, b1];
        }
        
        var i = Math.floor(h * 6);
        var f = h * 6 - i;
        var p = b * (1 - s);
        var q = b * (1 - f * s);
        var t = b * (1 - (1 - f) * s);
        
        switch (i % 6) {
            case 0: r = b, g = t, b1 = p; break;
            case 1: r = q, g = b, b1 = p; break;
            case 2: r = p, g = b, b1 = t; break;
            case 3: r = p, g = q, b1 = b; break;
            case 4: r = t, g = p, b1 = b; break;
            case 5: r = b, g = p, b1 = q; break;
        }
        
        return [
            Math.round(r * 255),
            Math.round(g * 255),
            Math.round(b1 * 255)
        ];
    }

    // Helper function to create a color swatch
    function createSwatch(name, h, s, b) {
        try {
            var rgb = hsbToRgb(h, s, b);
            var desc = new ActionDescriptor();
            var ref = new ActionReference();
            ref.putClass(charIDToTypeID("Clrs"));
            desc.putReference(charIDToTypeID("null"), ref);
            
            var colorDesc = new ActionDescriptor();
            colorDesc.putString(charIDToTypeID("Nm  "), name);
            
            var rgbDesc = new ActionDescriptor();
            rgbDesc.putDouble(charIDToTypeID("Rd  "), rgb[0]);
            rgbDesc.putDouble(charIDToTypeID("Grn "), rgb[1]);
            rgbDesc.putDouble(charIDToTypeID("Bl  "), rgb[2]);
            
            colorDesc.putObject(charIDToTypeID("Clr "), charIDToTypeID("RGBC"), rgbDesc);
            desc.putObject(charIDToTypeID("Usng"), charIDToTypeID("Clrs"), colorDesc);
            
            executeAction(charIDToTypeID("Mk  "), desc, DialogModes.NO);
            return true;
        } catch(err) {
            alert("Error creating swatch '" + name + "': " + err);
            return false;
        }
    }

    var successCount = 0;
    var totalSwatches = 24;  // Total number of swatches we'll create

    // Skin Tones
    successCount += createSwatch("SP Skin - Luminous Highlight", 30, 3, 97); // Warm highlight
    successCount += createSwatch("SP Skin - Natural Base", 25, 11, 90);      // Natural skin
    successCount += createSwatch("SP Skin - Volume Mid", 20, 16, 86);        // Mid tone
    successCount += createSwatch("SP Skin - Deep Shadow", 22, 19, 80);       // Shadow
    successCount += createSwatch("SP Skin - Blush Accent", 355, 20, 87);     // Subtle blush

    // Eyes
    successCount += createSwatch("SP Eyes - Bright Sparkle", 40, 22, 85);    // Warm sparkle
    successCount += createSwatch("SP Eyes - Warm Base", 30, 60, 45);         // Rich brown
    successCount += createSwatch("SP Eyes - Rich Mid", 25, 74, 35);          // Deep brown
    successCount += createSwatch("SP Eyes - Dark Shadow", 20, 80, 25);       // Dark brown

    // Lips
    successCount += createSwatch("SP Lips - Pearl Highlight", 0, 11, 90);    // Soft pink
    successCount += createSwatch("SP Lips - Rose Base", 355, 30, 80);        // Natural rose
    successCount += createSwatch("SP Lips - Blush Mid", 350, 40, 70);        // Deep rose
    successCount += createSwatch("SP Lips - Berry Shadow", 355, 27, 75);     // Shadow

    // Hair
    successCount += createSwatch("SP Hair - Sun Highlight", 35, 7, 95);      // Sunlit blonde
    successCount += createSwatch("SP Hair - Golden Base", 35, 38, 75);       // Golden brown
    successCount += createSwatch("SP Hair - Rich Mid", 25, 67, 45);          // Deep brown
    successCount += createSwatch("SP Hair - Deep Shadow", 35, 12, 85);       // Soft shadow

    // Clothing
    successCount += createSwatch("SP Cloth - Silk Highlight", 200, 3, 97);   // Cool white
    successCount += createSwatch("SP Cloth - Powder Base", 210, 7, 95);      // Light blue
    successCount += createSwatch("SP Cloth - Cool Mid", 210, 22, 90);        // Mid blue
    successCount += createSwatch("SP Cloth - Deep Fold", 210, 15, 94);       // Shadow blue

    // Background
    successCount += createSwatch("SP BG - Upper Light", 70, 6, 90);          // Warm light
    successCount += createSwatch("SP BG - Base Tone", 60, 12, 85);           // Natural tone
    successCount += createSwatch("SP BG - Mid Shadow", 90, 20, 75);          // Green shadow
    successCount += createSwatch("SP BG - Atmosphere", 70, 3, 95);           // Atmospheric

    alert("Palette creation complete!\nSuccessfully created " + successCount + " of " + totalSwatches + " swatches.");
} catch(e) {
    alert("Error: " + e + "\nAt line: " + e.line);
}
```

Here, we employ a straightforward conversion function that uses the correct mathematical formula. There’s **no** guessing or token-based pattern matching—just the right tool for the right job.

Hopefully, you now see why blindly trusting an LLM’s output can be perilous. This is especially true for **mission-critical workflows**, math or otherwise.