# C.W.K. LLM TextForge Project: The Complete Guide - Building Local LLM-Powered Text Processing Hub with AI-Pair Programming

![AI-Augmented Superhumanism](images/20250316-01.png)
> *AI-Augmented Superhumanism*

> ## 🔑 **⚠️ REMEMBER:** 
> 
> ## **AI thrives best as a guided partner.**
>
> ### Think of your AI as an **autistic savant child**—exceptionally gifted yet needing clear direction and nurturing.
> 
> ### *Embracing this mindset unlocks truly meaningful collaboration.*

- Local LLM-powered text processing
- Cursor IDE
- Keyboard Maestro
- Streamlit
- FastAPI
- Python
- MLX, Ollama backends

> **Note:** This guide describes a private project that is not open-sourced. It's intended as a conceptual workflow framework to inspire others building similar AI-powered applications. The implementation details, architecture patterns, and development approach can be adapted for your own projects.

## Introduction

The C.W.K. LLM TextForge Project (cwkLLMTextForge) is a comprehensive text processing system that brings advanced language model capabilities to your local machine. While Apple Intelligence and other commercial offerings are still developing basic text processing features, TextForge provides immediate access to powerful text manipulation through multiple interfaces:

- Command-line interface for terminal users
- Streamlit web UI for visual management
- System-wide shortcuts via Keyboard Maestro integration
- API endpoints for programmatic access

Built using AI-augmented development techniques with tools like Cursor IDE, this project demonstrates how developers can leverage AI assistance to rapidly create sophisticated applications that would otherwise require significantly more time and resources.

## Why TextForge Exists

I simply wanted quick, flexible text processing—correcting, translating, or changing the tone of text—without the hassle of manually copying and pasting into ChatGPT or Claude. Surprisingly, Apple Intelligence doesn't yet offer these basic features. With AI-powered IDEs like Cursor, VSCode with Copilot, PyCharm AI Assistant, or WindSurf, you can build production-quality applications in a fraction of the traditional development time.

TextForge was built to demonstrate how AI-augmented development can create practical, everyday tools that enhance productivity through:

- One-shortcut text processing replacing tedious copy-paste workflows
- Model-agnostic architecture supporting multiple LLM backends
- Extensible operation framework for custom text transformations
- System-wide integration with existing tools and workflows

### Family-Focused Design

This project was designed primarily for use by family members on a local network, which significantly influenced the architecture:

- Simplified design without authentication layers
- Focus on ease of use rather than enterprise security
- Assumption of trusted network environment
- Streamlined deployment and configuration

For public or enterprise deployments, you would want to add proper authentication, user management, and security measures, which would increase complexity significantly.

## Real-World Usage Examples

TextForge integrates seamlessly into daily workflows:

- **Writing**: Quick grammar correction and tone adjustments
- **Communication**: Translating messages between languages
- **Research**: Summarizing long articles or papers
- **Development**: Generating code comments or documentation

### Use Case: Real-time Text Processing in Web Applications

One of TextForge's most powerful applications is real-time text processing in any input field:

1. **Select text** in any input field (social media posts, email, chatbots)
2. **Press your configured shortcut** (e.g., Option+C for correction)
3. **TextForge processes the text** through your preferred LLM
4. **Selected text is instantly replaced** with the processed version

For example, when composing an X.com post or replying to a ChatGPT conversation:

```
Original (selected text): 
"i hope this post be useful for ppl trying build similar tool with LLM maybe implement soon if have time"

[Press shortcut for correction]

Replaced with: 
"I hope this post will be useful for people trying to build similar tools with LLMs. I might implement this soon if I have time."
```

There's no need to:
- Copy text to another application
- Wait for the application to load
- Paste text into a special field
- Copy the result
- Return to your original application
- Paste the corrected text

Everything happens within your current workflow with a single keystroke.

### Use Case: Enhanced Productivity in Cursor IDE

TextForge works exceptionally well within Cursor IDE, enhancing the already powerful AI capabilities:

#### Editor Mode Integration
- **Select code or comments** in your editor
- **Press your configured shortcut** (e.g., Option+F to formalize documentation)
- **Code/comments are automatically processed** through your LLM
- **No need for additional prompting** - the operation is pre-configured

For example, you might turn quick draft comments into proper documentation:

```python
# orig: this func loads the model and sets params
# [Press shortcut for formalization]

# This function initializes the language model and configures 
# the temperature, max_tokens, and other inference parameters
# according to the operation requirements.
```

#### Composer Mode Enhancement
- Use TextForge to refine your prompts before sending to Claude/GitHub Copilot
- Apply consistent tone and style to your communications with AI
- Translate between languages when working with multilingual documentation
- Summarize complex technical concepts before asking for AI implementation

This creates a powerful synergy: TextForge handles text refinement while Cursor's built-in AI handles complex reasoning and code generation.

## Core Components

TextForge provides several interfaces to fit your workflow:

### Command-line Interface

The primary CLI interface provides quick access to TextForge capabilities:

```bash
# Basic text processing
./core/bin/llm.sh -c "Fix this text"         # Correct grammar/spelling
./core/bin/llm.sh -tk "Translate to Korean"  # English → Korean
./core/bin/llm.sh -te "한국어 → 영어"        # Korean → English
./core/bin/llm.sh -f "make formal"           # Formal tone
./core/bin/llm.sh -ca "make casual"          # Casual tone
./core/bin/llm.sh -s "long text here"        # Summarize

# File processing
./core/bin/llm.sh -cf document.txt           # Correct a file

# Server management
./core/bin/llm.sh start                      # Start the Streamlit server
./core/bin/llm.sh stop                       # Stop the Streamlit server
./core/bin/llm.sh restart                    # Restart the Streamlit server
```

*Note: All text operations are fully customizable through the Streamlit UI, allowing you to modify prompts, parameters, and model selection. New operations can be created and integrated dynamically into the system without requiring code changes or restarts.*

### CLI Documentation

Below is the complete CLI documentation generated directly from the `llm.sh` script:

```bash
LLM Text Processing Tool
Usage:
  ./core/bin/llm.sh [options] [text]

Text Processing Operations (Short Format):
  -c "text"    Correct grammar and spelling
  -cp "text"    Correct grammar and spelling while preserving case
  -tk "text"    Translate to Korean
  -te "text"    Translate to English
  -s "text"    Summarize text
  -f "text"    Convert to formal tone
  -ca "text"    Convert to casual tone
  -tc "text"    Translate to Chinese
  -tp "text"    Testing parameters

Text Processing Operations (Full Format):
  --operation correct     Correct grammar and spelling
  --operation correct_preserve_case     Correct grammar and spelling while preserving case
  --operation translate_ko     Translate to Korean
  --operation translate_en     Translate to English
  --operation summarize     Summarize text
  --operation formal     Convert to formal tone
  --operation casual     Convert to casual tone
  --operation translate_ch     Translate to Chinese
  --operation test_params     Testing parameters

File Processing:
  -cf file.txt   Correct text from file
  -sf file.txt   Summarize text from file
  -tkf file.txt  Translate file content to Korean
  -tef file.txt  Translate file content to English
  -tff file.txt  Translate file content to French
  -ff file.txt   Convert file content to formal tone
  -caf file.txt  Convert file content to casual tone

Server Management:
  run           Start server with UI
  start         Start server in background
  stop          Stop the server
  restart       Restart the server
  status        Show server status
  kill-all      Kill all Streamlit instances

Examples:
  ./core/bin/llm.sh -c "Fix this sentense"
  ./core/bin/llm.sh --operation correct --model phi-3 "Fix this sentense"
  ./core/bin/llm.sh -sf document.txt
```

For advanced processing options, the tool provides detailed parameter controls:

```bash
Operation Shortcuts:
====================
  -c    correct (Correct grammar and spelling)
  -cp    correct_preserve_case (Correct grammar and spelling while preserving case)
  -tk    translate_ko (Translate to Korean)
  -te    translate_en (Translate to English)
  -s    summarize (Summarize text)
  -f    formal (Convert to formal tone)
  -ca    casual (Convert to casual tone)
  -tc    translate_ch (Translate to Chinese)
  -tp    test_params (Testing parameters)

For file operations, add 'f' to the shortcut (e.g., -cf for correcting a file)

Python Process Command Help:
===========================
usage: kmprocess.py [-h] [--text TEXT] [--file FILE] [--operation OPERATION] [--model MODEL]
                    [--temperature TEMPERATURE] [--max-tokens MAX_TOKENS] [--clipboard] [--list-operations]
                    [--list-models]

Process text with LLM models

options:
  -h, --help            show this help message and exit
  --text TEXT           Text to process (if not provided, will try clipboard)
  --file FILE           File containing text to process
  --operation OPERATION, -o OPERATION
                        Operation to perform (e.g., correct, summarize, translate_ko)
  --model MODEL, -m MODEL
                        Model name to use (if not specified, uses default)
  --temperature TEMPERATURE, -t TEMPERATURE
                        Temperature for generation
  --max-tokens MAX_TOKENS
                        Maximum tokens to generate
  --clipboard, -c       Read input from clipboard
  --list-operations, -l
                        List available operations
  --list-models, -lm    List available models
```

### Keyboard Maestro Shell Script Integration

TextForge provides a specialized shell script `km_shell_fast.sh` specifically optimized for integration with Keyboard Maestro and other automation tools. Unlike the main `llm.sh` tool, this script:

1. **Returns clean output** - Only the processed text result without debug information
2. **Simplifies clipboard handling** - Automatically reads from and writes to clipboard
3. **Optimized for automation** - Designed for non-interactive use in macros and scripts

This makes it ideal for use in Keyboard Maestro macros where clean output is essential for replacing clipboard contents.

```bash
Usage:
  ./core/bin/km_shell_fast.sh [operation] [server-url]
  ./core/bin/km_shell_fast.sh -c "Text to correct"
  ./core/bin/km_shell_fast.sh -o operation_name -c "Text to process"

Operations:
  correct                 Correct grammar and spelling
  correct_preserve_case   Correct grammar and spelling while preserving case
  translate_ko            Translate to Korean
  translate_en            Translate to English
  summarize               Summarize text
  formal                  Convert to formal tone
  casual                  Convert to casual tone
  translate_ch            Translate to Chinese
  test_params             Testing parameters

Shortcuts:
  -c,  --correct       Correct text
  -s,  --summarize     Summarize text
  -tk, --to-korean     Translate to Korean
  -te, --to-english    Translate to English
  -tf, --to-french     Translate to French
  -f,  --formal        Convert to formal tone
  -ca, --casual        Convert to casual tone
  -o,  --operation     Specify operation by name
  -h,  --help          Show this help

Text will be read from clipboard if not provided as an argument.
```

#### Why Use km_shell_fast.sh Instead of llm.sh

![km_shell_fast.sh](images/20250316-08.png)
> *km_shell_fast.sh*

While `llm.sh` provides comprehensive functionality and verbose output, `km_shell_fast.sh` is specifically designed for automation where clean text output is required:

| Feature | km_shell_fast.sh | llm.sh |
|---------|-----------------|---------|
| Output format | Clean text result only | Full response with debug info |
| Clipboard handling | Automatic | Manual |
| Response parsing | Pre-processed | Raw response |
| Error handling | Silent with minimal output | Verbose with stack traces |
| Designed for | Automation tools | Interactive use |

For Keyboard Maestro or other automation tools that need to paste the result back into applications, the clean output of `km_shell_fast.sh` is essential to avoid including debug information, timestamps, or other metadata that would appear in the pasted text.

### Keyboard Maestro Integration

![Keyboard Maestro Integration](images/20250316-09.png)
> *Keyboard Maestro Integration*

TextForge integrates with Keyboard Maestro for system-wide access:

#### Before Execution:
- **Limit Text Length:** Validate or truncate the input text to maintain manageable processing sizes.
- **Pre-processing:** Prepare or sanitize the text or clipboard data using additional tools or actions if necessary.
- **User Notification:** Display a clear notification indicating processing initiation to inform users of ongoing actions.

#### After Execution:
- **Post-processing:** Apply additional actions or tools to format, enhance, or handle the script's output as needed.
- **User Notification:** Display a notification confirming completion or results, enhancing user clarity and feedback.
- **Error Handling:** Implement robust error and edge-case handling mechanisms to manage unexpected behaviors gracefully.

![Execute Shell Script Action](images/20250316-10.png)
> *Execute Shell Script Action*

#### Additional Recommendations:
- Leverage your creativity to further automate and streamline workflows, integrating additional tools or custom scripts to optimize productivity and reliability.

### Streamlit User Interface

The Streamlit UI provides a visual interface for TextForge:

- Interactive text processing
- Model and operation management
- Configuration of advanced features
- Server monitoring and logging
- Caching system for model management

### FastAPI Hub Server

![TextForge Hub API](images/20250316-05.png)
> *TextForge Hub API*
The FastAPI server exposes TextForge capabilities to network clients:

```bash
# Server management
./core/bin/tfhub.sh start                    # Start the FastAPI server
./core/bin/tfhub.sh stop                     # Stop the FastAPI server
./core/bin/tfhub.sh restart                  # Restart the FastAPI server
./core/bin/tfhub.sh status                   # Check server status
```

## Cost Considerations

One of TextForge's most compelling advantages is its cost structure:

- **Free Operation**: Using local LLMs through Ollama or MLX incurs zero API costs
- **No Usage Limits**: Process as much text as needed without worry about quotas
- **Privacy Preserving**: All text processing happens locally without data leaving your network
- **Optional Commercial Integration**: Can be expanded to use commercial APIs like ChatGPT and Claude for more powerful capabilities, in which case it would consume API credits
- **Hybrid Approach**: Configure specific operations to use local models and others to use commercial APIs based on complexity and performance needs

This flexibility allows you to balance cost, performance, and capabilities according to your specific requirements.

## Prerequisites

To build a system like TextForge, you'll need:

- **Hardware**: Mac with Apple Silicon (for MLX) or any modern system for Ollama
- **Software**:
  - Python 3.9+ environment
  - Ollama for accessing open-source LLMs
  - MLX for Apple Silicon optimization (optional)
  - Streamlit for UI development
  - FastAPI for API endpoints
  - Keyboard Maestro or similar for system-wide shortcuts
- **Development Tools**:
  - AI-Powered IDE (Cursor, VSCode with Copilot, etc.)
  - Basic knowledge of Python and shell scripting
  - Fundamental understanding of ML/DL, AI, especially LLMs
  - *Empirical* Understanding of LLM prompt engineering - Technical understanding alone won't get you far

## System Architecture

*Note: Server and its port numbers are configurable.* 

TextForge employs a multi-server architecture to optimize performance and flexibility:

1. **Streamlit Admin Server (port 8510)**
   - Primary user interface for configuration and management
   - Handles model caching to improve responsiveness
   - Provides testing and debugging capabilities

2. **FastAPI Hub Server (port 8520)**
   - Exposes API endpoints for network clients
   - Enables programmatic access from automation tools
   - Serves as the bridge between clients and cached models

3. **Shared Model Caching**
   - Models are loaded once and shared across all components
   - Efficient memory usage through resource sharing
   - Warm-up feature prevents initial quirky responses

4. **Command-line and Automation Interfaces**
   - Direct CLI access via `llm.sh`
   - Keyboard Maestro integration via `km_shell_fast.sh`
   - Shortcut system for quick operation access

## Model Caching Architecture

One of TextForge's most powerful technical innovations is its cross-component model caching system. This feature dramatically improves performance by keeping large language models (often 15GB+ in size) loaded in memory between requests.

### The Challenge

Local LLMs face a significant challenge:
- Models are extremely large (7-100GB+ each)
- Loading models takes substantial time (10+ seconds)
- Each subprocess that needs the model would normally require its own copy
- Without optimization, each text processing request would need to reload the model

### Cross-Component Caching Solution

TextForge solves this challenge through a unified caching mechanism:

1. **Streamlit's `@st.cache_resource` Foundation**
   - Uses Streamlit's caching decorator to store loaded models
   - Once loaded, models remain in memory for reuse
   - The cache persists for the lifetime of the server process

2. **Unified Access Across Components**
   - Command-line tools access the same cached models as the UI
   - FastAPI hub server maintains its own model dictionary
   - All interfaces benefit from "warm" models that have already run initial inference

3. **Direct Integration vs. Process Isolation**
   - Initial implementation used subprocess calls, requiring separate model copies
   - Optimized approach directly integrates with model loading functions
   - Eliminates process startup overhead and reduces memory usage

### Implementation Details

The caching system uses different approaches for each component:

```python
# In Streamlit UI (server.py)
@st.cache_resource(hash_funcs={ModelConfig: lambda m: f"{m.name}:{m.model_type}:{m.path}"})
def load_model(model_config: ModelConfig) -> ModelBackend:
    """Load and cache the model"""
    st.info(f"Loading model {model_config.name}...")
    
    try:
        # Create the appropriate backend
        backend = get_backend_for_model(model_config)
        
        # Load the model
        logger.info(f"Loading model {model_config.name} of type {model_config.model_type}")
        backend.load()
        
        if backend.is_loaded:
            st.success(f"Model {model_config.name} loaded successfully")
            return backend
        else:
            st.error(f"Failed to load model {model_config.name}")
            return None
    
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        st.error(f"Error loading model: {e}")
        return None

# In FastAPI Hub Server (hub_server.py)
loaded_models = {}  # Dictionary to track which models we've loaded

def get_cached_model(model_name):
    """Get a model, loading it via Streamlit cache if not already loaded"""
    if model_name not in loaded_models:
        from config import get_model_by_name
        from server import load_model
        model_config = get_model_by_name(config, model_name)
        if model_config:
            loaded_models[model_name] = load_model(model_config)
        else:
            logger.error(f"Model {model_name} not found in configuration")
            raise ValueError(f"Model {model_name} not found")
    return loaded_models[model_name]
```

### Performance Benefits

This caching architecture delivers significant improvements:

- **Memory Optimization**: Only one copy of each model is loaded instead of one per process
- **Response Time**: Processing time reduced from 10-11 seconds to 4-5 seconds (~60% reduction)
- **User Experience**: Consistent fast response times regardless of interface used
- **Multi-User Support**: Multiple users benefit from the same cached models

### Cold Start vs. Warm Inference

TextForge includes a warm-up phase when loading models:

```python
# When loading a model
logger.info(f"Performing warm-up inference for model {model_config.name}")
model_backend.generate("This is a warm-up prompt to initialize the model.")
logger.info(f"Warm-up inference completed for {model_config.name}")
```

This prevents the "quirky" responses that LLMs sometimes produce on their first run after loading.

### Alternative Multi-User Caching Strategies to Consider (Not implemented)

For multi-user environments, you can implement various caching strategies to balance model specialization and memory efficiency:

1. **Model Pool Strategy**
   - Maintains a small pool of frequently-used models
   - Replaces least-used models when pool size limits are reached
   - Balances flexibility with memory constraints

2. **Operation Grouping**
   - Groups compatible operations to use the same model
   - Reduces model switching frequency
   - Preserves operation-specific optimization while improving cache hits

3. **Tiered Model Approach**
   - Uses a general-purpose model for most operations
   - Specialized models only loaded when necessary
   - Maximizes cache efficiency while maintaining quality

These strategies ensure optimal performance even when multiple users request different operations simultaneously. While they offer significant benefits for larger deployments, implementing them would substantially increase the system's complexity and development time. For the family-focused design of TextForge, the current caching approach provides an excellent balance of performance and simplicity.

### Cache Management

The cache can be managed through various methods:

- **Restart Servers**: `./core/bin/llm.sh restart` or `./core/bin/tfhub.sh restart`
- **UI Controls**: "Force Restart Server" button in the Config tab
- **Programmatic Clearing**: `st.cache_resource.clear()` or `loaded_models.clear()`

## Streamlit UI Framework

![Streamlit Admin UI](images/20250316-02.png)
> *Streamlit Admin UI*

TextForge leverages Streamlit as the foundation for its administrative interface and model caching system. While this choice provides numerous benefits, it also introduces specific development considerations that are crucial to understand.

### Tab-Based Interface Architecture

The Streamlit application uses a tab-based interface to organize functionality:

1. **Text Processing Tab**: Core functionality for text operations
   - Model selection (sidebar)
   - Operation selection
   - Text input/output
   - Processing parameters (temperature, max_tokens)

![Streamlit Admin UI - Text Processing Tab](images/20250316-04.png)
> *Streamlit Admin UI - Text Processing Tab*

2. **CLI Usage Tab**: Documentation for command-line usage
   - Shows examples of using `llm.sh` for direct text processing
   - Documents operation shortcuts
   - Server management commands (Todo)
   - Keyboard Maestro integration

3. **API Usage Tab**: Documentation and tools for API integration
   - API endpoint documentation
   - Example API requests and responses
   - Testing interface for API calls (Todo)
   - Client code samples for different languages

4. **Config Tab**: Configuration and model management
   - Memory usage monitoring
   - Add models from different sources (Ollama, HuggingFace)
   - Reset configuration options
   - Cache management

![Streamlit Admin UI - Config Tab](images/20250316-03.png)
> *Streamlit Admin UI - Config Tab*

5. **Operations Tab**: Operation management interface
   - View all available text processing operations
   - Add new custom operations
   - Modify existing operation parameters and prompts
   - Delete unused operations
   - Test operations directly

![Streamlit Admin UI - Operations Tab](images/20250316-06.png)
> *Streamlit Admin UI - Operations Tab*

6. **Logs Tab**: Server logging and diagnostics
   - View server logs
   - Filter logs by type
   - Clear logs
   - Debug operation issues

7. **System Info Tab**: System-wide statistics and information
   - Hardware resource usage (CPU, RAM, GPU)
   - Python environment details
   - Loaded model information
   - Version information
   - System uptime and performance metrics

### Streamlit Caching Challenges

When developing with Streamlit, especially with resource caching via `@st.cache_resource`, there are important behavior patterns to understand:

#### The Caching Problem

**Code changes are often not applied when clicking the "Rerun" button**. This can lead to hours of frustrating debugging where you're making changes that aren't actually being reflected in the running application.

This happens because:

1. **Resource Persistence**: `@st.cache_resource` is designed to persist across "reruns" of the app
   - Once a model or resource is loaded, Streamlit keeps it in memory
   - The cached object and its methods remain the same even when you modify the source code

2. **Object Instantiation**: Objects created once and stored in session state or cache aren't reconstructed when code changes
   - Changes to class methods don't automatically update existing object instances
   - New method implementations are only used when objects are freshly instantiated

3. **Subprocess Isolation**: If your app launches subprocesses (like our MLXBackend.generate method), changes to the code in those string templates don't trigger Streamlit's hot-reloading

#### Development Solutions

TextForge implements several solutions to address these caching challenges:

1. **Restart Button**: A "Force Restart Server" button in the Config tab that:
   ```python
   if st.button("Force Restart Server"):
       st.cache_resource.clear()
       st.experimental_rerun()
   ```

2. **Cache Information Display**:
   ```python
   st.write(f"Cache info: {st.cache_resource.get_stats()}")
   ```

3. **Restart Flag Detection**:
   ```python
   if os.path.exists(".force_restart"):
       st.cache_resource.clear()
       st.cache_data.clear()
       os.remove(".force_restart")
   ```

These solutions ensure that developers can effectively work with the caching system while maintaining the performance benefits it provides for users.

### UI vs. CLI Approach

TextForge provides three complementary ways to process text:

1. **UI (Streamlit)**: Visual interface for:
   - Interactive experimentation
   - Configuring models and operations
   - Monitoring server status
   - Debugging and troubleshooting

2. **CLI (`llm.sh`)**: Command-line for:
   - Direct text processing (more efficient)
   - Automation and scripting
   - Server management
   - Integration with other tools

3. **Automation Interface (`km_shell_fast.sh`)**: Specifically designed for system-wide integration:
   - **Clean output format**: Returns only the processed text without debug information
   - **Automatic clipboard handling**: Seamlessly reads from and writes to clipboard
   - **Optimized for Keyboard Maestro**: Perfect for system-wide keyboard shortcuts
   - **Silent operation**: Minimizes logging and status messages
   - **Focused functionality**: Streamlined for rapid text transformation workflows
   - **Consistent return values**: Reliable for automation chains and macros

The CLI approach is generally faster as it bypasses the Streamlit UI and can process text directly using the underlying Python scripts. However, the Streamlit interface provides essential configuration and monitoring capabilities.

For automation and keyboard shortcuts, the `km_shell_fast.sh` script provides the ideal balance of performance and integration. Unlike the standard CLI tool, it's specifically designed to operate silently in the background, processing text through clipboard operations without displaying verbose output that would interfere with automation workflows.

### Performance Considerations

When working with the Streamlit interface:

1. **Memory Usage**:
   - Models can consume significant RAM (7-15GB each)
   - The Config tab includes memory usage monitoring
   - Clear cache when switching between large models to free memory

2. **First Run Performance**:
   - First text processing will be slower (model loading)
   - Subsequent runs use cached models for dramatically improved speed
   - Consider using smaller models (4-bit quantized) for faster initial performance

3. **Subprocess vs. In-Process**:
   - MLX models use subprocess for isolation in some configurations
   - This improves stability but adds overhead
   - Consider this tradeoff when benchmarking

## FastAPI Hub Server Architecture

The TextForge Hub Server is a lightweight FastAPI wrapper around the existing TextForge processing system. It enables multiple devices on the home network to leverage a central powerful machine (like a Mac Studio) for LLM processing without having to run models locally on each device.

### System Architecture Overview

```
┌────────────────────────────────────────────────────────────────────────────┐
│                           Mac Studio M2 (Host Server)                      │
│                                                                            │
│  ┌───────────────┐   ┌───────────────────┐   ┌──────────────────────────┐  │
│  │               │   │                   │   │                          │  │
│  │  TextForge    │   │  Streamlit Server │   │  TextForge Hub Server    │  │
│  │  Core         │◄──┤  (Admin UI)       │   │  (FastAPI)               │  │
│  │  Modules      │   │  port 8510        │   │  port 8520               │  │
│  │               │◄──┤                   │◄──┤                          │  │
│  └───────┬───────┘   └───────────────────┘   └──────────────┬───────────┘  │
│          │                    ▲                             │              │
│          │                    │                             │              │
│  ┌───────▼───────┐   ┌────────┴──────────┐                  │              │
│  │               │   │                   │                  │              │
│  │  Model Cache  │   │  Shell Scripts    │                  │              │
│  │  Management   │   │  ./core/bin/      │                  │              │
│  │               │   │                   │                  │              │
│  └───────────────┘   └───────────────────┘                  │              │
│                                                             │              │
└─────────────────────────────────────────────────────────────┼──────────────┘
                                                              │
                                                              ▼
                      ┌──────────────────────────────────────────────────┐
                      │                 Network API                      │
                      │         http://hostname:8520/api/process         │
                      └─────────────────────┬────────────────────────────┘
                                            │
             ┌────────────────────────┬─────┴─────┬─────────────────────┐
             │                        │           │                     │
    ┌────────▼─────────┐    ┌─────────▼────────┐  │  ┌─────────────────────┐
    │                  │    │                  │  │  │                     │
    │ Laptops/Desktops │    │ Mobile Devices   │  │  │ Automation Systems  │
    │                  │    │                  │  │  │                     │
    └──┬─────────┬─────┘    └──────────────────┘  │  └─────────────────────┘
       │         │                                │
┌──────▼───┐ ┌───▼──────┐                 ┌──────▼──────┐
│          │ │          │                 │             │
│ Keyboard │ │ Browser  │                 │ Native Apps │
│ Maestro  │ │ Access   │                 │ (future)    │
│          │ │          │                 │             │
└──────────┘ └──────────┘                 └─────────────┘
```

This comprehensive architecture illustrates how TextForge components work together:

1. **Core Components**:
   - **TextForge Core Modules**: Central processing engine that handles all text operations
   - **Model Cache Management**: Efficiently maintains loaded models in memory
   - **Shell Scripts**: Command-line interfaces for direct system access

2. **Server Components**:
   - **Streamlit Server**: Administrative UI for configuration, operation management, and testing
   - **FastAPI Hub Server**: API endpoints enabling network access from remote devices

3. **Client Access Methods**:
   - **Keyboard Maestro**: System-wide shortcuts for text processing on macOS
   - **Browser Access**: Direct web UI access to Streamlit interface
   - **Mobile Devices**: Access via API endpoints from smartphones and tablets
   - **Automation Systems**: Integration with workflow automation tools
   - **Native Apps**: Future iOS/iPadOS and macOS applications

4. **Integration Flow**:
   - Shell scripts interact directly with the TextForge Core
   - Remote clients communicate through the Hub Server API
   - All components share the same model cache for efficiency
   - Both local and remote operations use identical processing logic

### Design Principles

The Hub Server was designed with several key principles in mind:

- **Minimalism**: Simple API wrapper with no unnecessary components
- **Non-invasive**: No modifications to the existing TextForge codebase
- **Private use**: Designed for use by family members on home network
- **Direct addressing**: Uses direct IP addressing for simplicity

### Implementation Details

#### Server Components

1. **hub_server.py**: The main FastAPI server that:
   - Listens for HTTP requests on a configured port (default: 8520)
   - Receives text processing requests with operation type
   - Passes requests to the existing text processing module
   - Returns processed results to the client

2. **Hub Configuration**: Settings for:
   - Server host and port
   - Debug mode
   - Default operation

#### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Server info and available endpoints |
| `/api/process` | POST | Process text with specified operation |
| `/api/operations` | GET | List available operations |
| `/api/models` | GET | List available models |

#### Logging System

The hub server implements a comprehensive logging system:

- **Unique Instance IDs**: Each server instance gets a unique ID for tracking
- **Request IDs**: Every request is assigned a unique ID for tracking through the system
- **Rotating File Handlers**: Logs are automatically rotated to prevent disk space issues
- **Performance Metrics**: Request processing time is tracked and logged

### Client Implementation

The Hub Server can be accessed by various clients:

1. **Keyboard Maestro Scripts**:
   ```javascript
   // JavaScript for Keyboard Maestro
   function run() {
     const text = Application('System Events').clipboard();
     const response = $.NSMutableURLRequest.requestWithURL(
       $.NSURL.URLWithString('http://ai-server-studio:8520/api/process')
     );
     
     // Configure request and send
     response.setHTTPMethod('POST');
     const payload = $.NSString.alloc.initWithString(
       JSON.stringify({
         'text': text,
         'operation': 'correct'
       })
     );
     
     // Process response and update clipboard
     // ...
     
     return "Text processed";
   }
   ```

2. **Shell Script Integration**:
   ```bash
   curl -X POST http://ai-server-studio:8520/api/process \
     -H "Content-Type: application/json" \
     -d '{"text":"Fix this text plz", "operation":"correct"}'
   ```

### Why FastAPI Over Alternatives

FastAPI was selected for this project for several key reasons:

1. **Performance**: FastAPI is built on Starlette and Uvicorn, making it one of the fastest Python web frameworks available, comparable to Node.js and Go. This is crucial when working with LLMs where response time is already a constraint.

2. **Simplicity**: Extremely easy to set up with minimal code - the entire server implementation is just ~30 lines. Compare this with Django (hundreds of files for basic setup) or even Flask (multiple modules for a robust implementation).

3. **Modern Python**: Uses Python type hints for enhanced code reliability and editor support, which means fewer runtime errors and better development experience.

4. **Automatic Documentation**: Provides automatic API documentation via Swagger UI at `/docs` endpoint - helpful for development and testing. This is built-in, unlike Flask which requires additional extensions.

5. **Built-in Validation**: Uses Pydantic for automatic request validation and parsing. This eliminates much of the boilerplate code needed in other frameworks to validate incoming data.

6. **Production-Ready**: Works seamlessly with production ASGI servers like Uvicorn or Hypercorn without additional configuration.

7. **Low Overhead**: Perfect for small, focused APIs that need to be fast and reliable. The overhead per request is minimal compared to larger frameworks.

### Why Not Use Streamlit for API Endpoints

While Streamlit is excellent for the admin UI, it has several limitations that make it unsuitable for API endpoints:

1. **UI-First Design**: Streamlit is designed for interactive dashboards and UIs, not for machine-to-machine communication. Its architecture is fundamentally built around human interaction.

2. **Session-Based State**: Streamlit maintains session state for users, which adds unnecessary overhead for simple API calls and can lead to unexpected behavior in an API context.

3. **Request Handling Limitations**: Unlike FastAPI, Streamlit doesn't provide fine-grained control over HTTP methods, headers, status codes, and other API essentials.

4. **Performance Overhead**: Streamlit's rendering engine adds significant overhead to each request, making it inefficient for high-throughput API scenarios.

5. **No Native API Features**: Streamlit lacks built-in features like request validation, API documentation, and proper error handling that are essential for robust APIs.

6. **Execution Model**: Streamlit's execution model (rerunning the entire script on interaction) is fundamentally at odds with the stateless request/response pattern of APIs.

By using FastAPI for the Hub Server and Streamlit for the admin UI, TextForge leverages the strengths of each framework for its intended purpose, creating a more efficient and maintainable system.

## Installation and Setup

> **Note:** While TextForge itself is not open-sourced, here's a conceptual approach to setting up a similar system:

```bash
# Conceptual installation steps for similar projects
git clone https://github.com/yourusername/your-text-processor.git
cd your-text-processor
pip install -r requirements.txt

# Initial configuration
cp config/config.example.json config/config.json
# Edit configuration as needed
```

For a family-focused local deployment, you might:
1. Set up the system on the most powerful machine in your home
2. Configure it to start automatically on boot
3. Create shortcuts on family members' machines pointing to the central server
4. Share the configuration UI link on your local network

This approach eliminates the need for complex authentication while maintaining utility for all users.

## Core Components

### Command-line Interface

The primary CLI interface provides quick access to TextForge capabilities:

![llm.sh CLI](images/20250316-07.png)
> *llm.sh CLI*

```bash
# Basic text processing
./core/bin/llm.sh -c "Fix this text"         # Correct grammar/spelling
./core/bin/llm.sh -tk "Translate to Korean"  # English → Korean
./core/bin/llm.sh -te "한국어 → 영어"        # Korean → English
./core/bin/llm.sh -f "make formal"           # Formal tone
./core/bin/llm.sh -ca "make casual"          # Casual tone
./core/bin/llm.sh -s "long text here"        # Summarize

# File processing
./core/bin/llm.sh -cf document.txt           # Correct a file

# Server management
./core/bin/llm.sh start                      # Start the Streamlit server
./core/bin/llm.sh stop                       # Stop the Streamlit server
./core/bin/llm.sh restart                    # Restart the Streamlit server
```

### FastAPI Hub Server

The FastAPI server exposes TextForge capabilities to network clients:

```bash
# Server management
./core/bin/tfhub.sh start                    # Start the FastAPI server
./core/bin/tfhub.sh stop                     # Stop the FastAPI server
./core/bin/tfhub.sh restart                  # Restart the FastAPI server
./core/bin/tfhub.sh status                   # Check server status
```

### Keyboard Maestro Integration

TextForge integrates with Keyboard Maestro for system-wide access:

```bash
# Used with Keyboard Maestro's Execute Shell Script action
./core/bin/km_shell_fast.sh -c "%CurrentClipboard%"
```

The most reliable way to use this system is 'Execute Shell Script' as text since you need to include arguments in the script: '/bin/bash -c "/path/to/km_shell_fast.sh -c"

Add logical actions before and after the script execution to:

- limit the length of the text to process
- display a notification before/after processing
- pre- or post-process the text or clipboard with other tools or actions
- handle errors and edge cases.
- use your imagination!

## Operation Management

TextForge operations are fully configurable through both the UI and configuration files:

### Operation Structure

```json
{
  "name": "Correct",
  "description": "Fix spelling and grammar",
  "prompt": "Correct the spelling and grammar of the following text: %TEXT%",
  "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
  "shortcut": "c"
}
```

### Managing Operations

- Add, edit, and delete operations through the Streamlit UI
- Configure shortcuts for quick CLI access
- Set operation-specific models and parameters
- Group operations by category for organization

## Model Management

TextForge supports multiple model backends:

### Supported Backends

- **Ollama**: For open-source models like Llama, Mistral, etc.
- **MLX**: Apple Silicon-optimized models for efficient local inference
- **API** (planned): Integration with commercial APIs like OpenAI or Anthropic

### Model Selection Hierarchy

TextForge implements a sophisticated model selection system that follows object-oriented principles to determine which language model to use for each operation.

#### Selection Priority Order

The model selection follows a clear inheritance and override pattern (from highest to lowest priority):

1. **Request-specific model** (explicit override)
2. **Operation-specific model** (if use_global_model=false)
3. **Last selected model** (global state)
4. **Fallback model** (global default)
5. **First available model** (emergency fallback)

#### Object-Oriented Principles

The model selection system implements core OO concepts:

**Inheritance and Overriding**:
- **Base Class Behavior**: The global models (fallback and last selected) represent the default implementation
- **Derived Class Override**: Operation-specific models override this behavior when specified
- **Runtime Override**: Request-specific models provide the highest-priority override at runtime

**Encapsulation**:
- **Operation Templates**: Each operation encapsulates its model preference and a flag indicating whether to use the global model
- **Configuration Object**: Global preferences are encapsulated in the Config object
- **Request Object**: Client requests encapsulate runtime model preferences

#### Implementation Details

```python
# Priority 1: Request-specific model
if request.model:
    model_name = request.model
    
# Priority 2: Operation-specific model
elif operation.model and not operation.use_global_model:
    model_name = operation.model
    
# Priority 3-5: Global model selection
else:
    # Priority 3: Last selected model
    if hasattr(config, 'last_selected_model') and config.last_selected_model:
        model_name = config.last_selected_model
    # Priority 4: Fallback model
    elif hasattr(config, 'fallback_model') and config.fallback_model:
        model_name = config.fallback_model
    # Priority 5: First available model
    elif config.models:
        model_name = config.models[0].name
```

**Key Classes and Properties**:

- **OperationTemplate**
  - `model`: String specifying preferred model name
  - `use_global_model`: Boolean flag determining whether to use global model

- **Config**
  - `last_selected_model`: The most recently used model in the UI
  - `fallback_model`: The configured fallback/default model
  - `models`: List of available model configurations

- **TextRequest**
  - `model`: Optional override for model selection

#### Use Cases

**Case 1: Global Default**

When operations have `use_global_model=true` or empty model field:
- All operations use the fallback model or last selected model
- Results in memory-efficient operation with only one model loaded

**Case 2: Operation-Specific Models**

When an operation has:
- A specific model set (e.g., `"model": "phi-4-8bit"`)
- `"use_global_model": false`
  
The operation will always use its specified model regardless of global settings.

**Case 3: Client Override**

When a client request includes a model parameter:
- The specified model is used for that request only
- Useful for testing or specialized needs

#### Best Practices

1. **Default Configuration**: Set all operations to `"use_global_model": true` and maintain a sensible fallback model
2. **Specialized Operations**: Only override for operations truly requiring a specific model
3. **UI Consistency**: When users select models in the UI, update `last_selected_model` for consistency

#### Technical Implementation

The TextForge system maintains efficient operation by:
1. Loading models only when needed
2. Caching loaded models for reuse
3. Using the same instance across different operations where possible

This approach optimizes memory usage while providing flexibility for operation-specific model requirements.

### Cost Considerations

One of TextForge's most compelling advantages is its cost structure:

- **Free Operation**: Using local LLMs through Ollama or MLX incurs zero API costs
- **No Usage Limits**: Process as much text as needed without worry about quotas
- **Privacy Preserving**: All text processing happens locally without data leaving your network
- **Optional Commercial Integration**: Can be expanded to use commercial APIs like ChatGPT and Claude for more powerful capabilities, in which case it would consume API credits
- **Hybrid Approach**: Configure specific operations to use local models and others to use commercial APIs based on complexity and performance needs

This flexibility allows you to balance cost, performance, and capabilities according to your specific requirements.

## Model Backend Implementation

TextForge uses two primary backends for local model inference: Ollama and MLX. Each offers distinct advantages and implementation challenges.

### Ollama Backend

[Ollama](https://ollama.ai/) provides a straightforward approach to running large language models locally with a simple API:

#### Advantages of Ollama

1. **Simple Architecture**: Ollama abstracts away the complexities of running LLMs locally
2. **Easy Model Management**: Models can be pulled with a single command (`ollama pull modelname`)
3. **Consistent API**: Simple REST API with predictable behavior across different models
4. **Wide Model Support**: Access to a growing library of optimized models
5. **Cross-Platform**: Works on macOS, Windows, and Linux

#### Implementation

Integrating with Ollama is straightforward:

```python
import requests

def generate_with_ollama(model_name, prompt, temperature=0.7):
    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
            'model': model_name,
            'prompt': prompt,
            'temperature': temperature
        }
    )
    return response.json()['response']
```

#### Model Selection

Ollama supports a wide range of models that can be easily listed and managed:

```bash
$ ollama list
NAME                      ID              SIZE      MODIFIED     
gemma3:27b                30ddded7fba6    17 GB     36 hours ago    
qwq-8b:latest             069c0952eda3    34 GB     9 days ago      
qwq:latest                38ee5094e51e    19 GB     10 days ago     
deepseek-r1:70b           0c1615a8ca32    42 GB     7 weeks ago     
phi4:latest               ac896e5b8b34    9.1 GB    2 months ago    
llama3.3:latest           a6eb4748fd29    42 GB     3 months ago    
Lexi-Uncensored:latest    4c7eaf4a7503    8.5 GB    3 months ago
```

### MLX Backend

[MLX](https://github.com/ml-explore/mlx) is Apple's machine learning framework optimized for Apple Silicon. While more complex to implement than Ollama, it offers significant performance advantages on Mac hardware.

#### Advantages of MLX

1. **Apple Silicon Optimization**: Built specifically for M1/M2/M3 chips
2. **Memory Efficiency**: Better memory utilization compared to general-purpose frameworks
3. **Performance**: Faster inference on Apple hardware
4. **Quantization Support**: Native support for 4-bit, 3-bit quantized models
5. **Growing Ecosystem**: Expanding library of optimized models via `mlx-community`

#### Implementation Challenges

Integrating MLX presented several challenges:

1. **Model Compatibility**:
   - Only models specifically converted to MLX format work
   - Must use models from `mlx-community` organization or manually converted models
   - Quantized models (4-bit, 3-bit) are preferred for memory efficiency

2. **Parameter Naming Inconsistencies**:
   - MLX expects `--temp` instead of `--temperature`
   - Using incorrect parameter names causes cryptic errors

3. **API vs. Command-line Differences**:
   - Python API can be inconsistent across versions
   - Command-line interface is more stable but requires subprocess calls

#### Subprocess Implementation

After extensive testing, we found that using MLX via subprocess is more reliable than direct API integration:

```python
def generate_with_mlx(model_name, prompt, temperature=0.7, max_tokens=100):
    # Use the mlx_lm CLI directly with the correct arguments
    cmd = [
        "python", "-m", "mlx_lm.generate", 
        "--model", model_name,
        "--prompt", prompt,
        "--max-tokens", str(max_tokens),
        "--temp", str(temperature)  # Note: --temp, not --temperature
    ]
    
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )
    
    # Extract the generated text from output
    generated_text = result.stdout.strip()
    
    # Clean up MLX CLI output formatting
    if "==========" in generated_text:
        # Extract content between the ========== markers
        parts = generated_text.split("==========")
        if len(parts) >= 2:
            generated_text = parts[1].strip()
    
    # Remove token stats and memory usage info
    lines = generated_text.split('\n')
    clean_lines = []
    for line in lines:
        if not any(x in line.lower() for x in ["tokens-per-sec", "peak memory", "tokens:", "prompt:", "generation:"]):
            clean_lines.append(line)
    
    return '\n'.join(clean_lines).strip()
```

#### Chat Models

For chat models, proper template handling is required:

```python
def process_chat_with_mlx(model_name, messages, temperature=0.7):
    # Convert messages to MLX chat template format
    from mlx_lm import load, generate
    
    model, tokenizer = load(model_name)
    
    # Apply chat template
    prompt = tokenizer.apply_chat_template(
        messages, 
        add_generation_prompt=True
    )
    
    response = generate(model, tokenizer, prompt=prompt, temp=temperature)
    return response
```

#### Best Practices for MLX

Through extensive experimentation, we developed these best practices:

1. **Filter for Compatible Models**:
   - Look specifically for `mlx-community` models
   - Focus on quantized models (4-bit, 3-bit) for better memory efficiency
   - Example: `mlx-community/Phi-3-medium-128k-instruct-4bit`

2. **Use Subprocess for Reliability**:
   - More stable across different mlx_lm versions
   - Avoids Python API inconsistencies
   - Provides better error reporting

3. **Parameter Handling**:
   - Always use `--temp` (not `--temperature`)
   - Be explicit with all parameters
   - Validate parameter types before passing

4. **Warm-up Inference**:
   - First inference is significantly slower
   - Implement a warm-up phase after loading models
   - Log the warm-up process for debugging

5. **Memory Management**:
   - Monitor memory usage when working with larger models
   - Close and reopen models if memory issues occur
   - Consider model size when selecting for operations

### Comparison and Selection

The TextForge system intelligently selects between these backends based on:

1. **Hardware Availability**: MLX is prioritized on Apple Silicon machines
2. **Model Compatibility**: Some operations work better with specific backends
3. **Memory Constraints**: Smaller models may be selected under memory pressure
4. **Operation Requirements**: Task-specific optimization may favor one backend

This dual-backend approach provides flexibility while maximizing performance across different hardware configurations.

## Advanced Features

### Shortcuts System

```bash
# View available shortcuts
./core/bin/llm.sh --help
./core/bin/shortcuts.sh --list

# Manage shortcuts
./core/bin/shortcuts.sh --reset
./core/bin/shortcuts.sh --force-reset
```

### Logging System

TextForge maintains comprehensive logs for troubleshooting:

- Operation logs with unique run IDs
- Server logs for Streamlit and FastAPI
- Error logs with detailed error messages

*Log management examples will be included*

### Security Considerations

While TextForge was designed for trusted local networks without authentication, here are considerations for adapting it to more public settings:

- Add user authentication to the FastAPI server
- Implement API key validation for programmatic access
- Set up HTTPS for encrypted communication
- Add rate limiting to prevent abuse
- Configure proper network isolation and firewalls

These additions would increase complexity but would be necessary for deployments beyond a family home network.

## Development with AI Pair Programming

This project was developed using AI-augmented programming techniques through close collaboration between human and AI.

### Operation-Specific Model Configuration

Now each operation-specific model operates with its own cache and parameters: temperature and max_tokens.

For instance, for strict translation operations, more deterministic results might be preferred with temperature set to lower values.

Values are automatically updated in real-time within the UI, providing immediate feedback as configurations are changed.

### Caching Architecture Insights

For high-concurrency scenarios, you can implement sophisticated dynamic caching mechanisms to optimize performance. Brainstorm with your AI partner to design a caching architecture tailored to your specific scaling requirements.

Currently, I leverage Streamlit's built-in caching mechanism to efficiently manage multiple models in memory. This approach offers several advantages: it's highly scalable, requires minimal code implementation, and provides exceptional reliability with automatic memory management.

External scripts can seamlessly utilize this same caching infrastructure without requiring the full UI stack, providing significant performance benefits while maintaining consistency across different access methods.

### Real-World Collaboration Insights

One tip for AI-pair coding: always instruct your AI partner to rigorously test each implementation before proceeding to the next development step. This simple practice transforms the entire development workflow, catching edge cases early, validating assumptions, and ultimately producing more robust code with fewer iterations. The difference in quality and efficiency is remarkable.

Be cautious about this tempting but risky mindset: *"This gamechanger model can oneshot anything!"*

In real-world applications, this overly optimistic belief can lead both you and the model into deep rabbit holes that neither can escape.

Due to context window limitations, no current model can fully maintain a consistent understanding of a project throughout the entire development process. Continuous human guidance is crucial for the model to stay aligned with your objectives.

Until we achieve a true Jarvis-level AGI, always monitor closely. If you're not actively guiding the model and can't rescue it from pitfalls, your project risks becoming unsustainable and doomed.

### Tips for Effective AI Pair Programming

- **Brainstorm first.** Clearly define your problem before diving in.
- **Document extensively.** Let the model track every decision for future context.
- **New sessions solve cluttered contexts.** When stuck, restart with fresh context and previous session documentation.
- **Use 'Ask' vs. 'Agent' modes wisely.** Prevent the AI from prematurely exploring unhelpful paths.
- **Cursor's Beta Web Search:** Guide the AI explicitly or let it autonomously find updated info.
- **Direct the model explicitly when needed.** Provide exact URLs for specific source code to improve model accuracy.
- **Preferred daily-use LLM:** Phi4—fast, reliable, and effective.
- **Debug incrementally:** Simplify scripts to isolate and fix issues effectively.

### Lessons Learned

1. **Never Assume Behavior:** Even simple argument passing differs subtly in various environments.
2. **Log Everything:** Scripts may behave unpredictably outside terminal environments.
3. **Explicit Paths:** Use absolute paths and explicit environment declarations.
4. **Small Details Count:** Tiny logging nuances can impact your output significantly.
5. **AI Limitations:** AI models like Claude require explicit guidance, especially for niche automation and debugging scenarios.

Here's a critical aspect of current AI systems: they often exhibit overconfidence when speculating about what might or might not work. This stems from biases in their pre-trained knowledge, which reflects the aggregate of human knowledge—including our collective human biases. Always apply your own judgment and actively guide the AI. The encouraging aspect is that these systems can be reasoned with through clear, explicit instructions and feedback. This collaborative approach produces significantly better results than blindly accepting AI suggestions. 

*Note: When using reasoning models like Claude 3.7 Sonnet Thinking, you gain an invaluable window into the model's inner logic. By examining these thought processes, you can preemptively identify and prevent overconfident actions by catching illogical or inconsistent reasoning that doesn't align with your intentions. While the final responses are polished and packaged, the exposed thought processes reveal the raw, unfiltered reasoning—providing critical insights that help you guide the model more effectively.*

Transforming a seemingly straightforward task into a deep dive has resulted in a robust, highly reliable system that gracefully handles failure scenarios—ideal for unattended automation workflows.

So, Apple... while we wait for your Intelligence features to catch up, we'll keep building our own solutions. The future is already here—it's just not evenly distributed yet.

## Project Structure

```
core/
├── bin/                    # Executable scripts
│   ├── llm.sh              # Main CLI interface
│   ├── km_shell_fast.sh    # Keyboard Maestro integration
│   ├── shortcuts.sh        # Shortcuts management
│   ├── tfhub.sh            # FastAPI server control
│   └── logs.sh             # Log management
├── src/                    # Python source code
│   ├── server.py           # Streamlit UI server
│   ├── hub_server.py       # FastAPI server
│   ├── config.py           # Configuration handling
│   ├── kmprocess.py        # Text processing core
│   └── add_shortcuts.py    # Shortcut management
├── config/                 # Configuration files
│   ├── config.json         # Main configuration
│   └── hub_config.json     # Hub server configuration
├── logs/                   # Log files
│   ├── streamlit_server.log
│   ├── hub_server.log
│   └── [operation logs]    # Individual operation log files
└── docs/                   # Documentation (CRITICAL)
    ├── COMPLETE-GUIDE.md   # This comprehensive guide
    ├── caching-models.md   # Details on caching architecture
    ├── streamlit.md        # Streamlit implementation notes
    ├── mlx.md              # MLX integration details
    ├── km-hub.md           # Keyboard Maestro integration
    └── issues.md           # Known issues and solutions
```

### Documentation as a Critical Development Component

Documentation is not merely an afterthought but a critical component of the development process, especially when working with AI pair programming. In the TextForge project, comprehensive documentation serves several essential purposes:

1. **Bridging Context Window Limitations**: AI models like Claude have finite context windows, meaning they cannot hold the entire project in "memory" during a session. Detailed documentation allows the AI to quickly understand complex components without needing to see all the code.

2. **Preventing "Rabbit Holes"**: Without proper documentation, both human developers and AI assistants can get lost in implementation details, creating complexity that becomes increasingly difficult to navigate. Good documentation creates guideposts that prevent these descent into unmanageable complexity.

3. **Avoiding Black Box Syndrome**: Undocumented code quickly becomes a "black box" that neither humans nor AI can fully comprehend. This is particularly dangerous in AI-assisted development, where the AI might make assumptions about undocumented components that lead to inconsistent implementations.

4. **Project Continuity**: Documentation ensures that the project can be understood and maintained even after significant time has passed. This is vital for long-term project health and prevents projects from falling into "limbo" where they're too complex for anyone to confidently modify.

5. **Knowledge Transfer**: When additional developers (human or AI) join the project, comprehensive documentation accelerates their understanding and enables them to contribute effectively without extensive onboarding.

Every key decision, architectural pattern, and non-obvious implementation detail in TextForge is documented. This documentation-first approach has been instrumental in maintaining project clarity despite its sophisticated caching mechanisms and multi-component architecture.

## Extending TextForge

The modular architecture of TextForge allows for easy extension:

- Adding new operation types
- Integrating additional model backends
- Creating custom UIs or clients
- Building specialized workflows

### Adding Commercial API Support

While TextForge works perfectly with free local LLMs, adding support for commercial APIs is straightforward:

1. Create a new backend class that implements the API connection
2. Add appropriate authentication and rate limiting
3. Configure operations to use the commercial backend when needed

This approach allows you to:
- Use sophisticated commercial models for complex tasks
- Maintain free local processing for routine operations
- Create fallback paths between commercial and local models
- Implement cost monitoring and usage controls

For example, you might configure grammar correction to use local models (free) while reserving commercial APIs (paid) for complex creative writing or technical content generation.

*Additional extension examples and tutorials will be included*

## Keyboard Maestro and System Integration

TextForge's power is fully realized through system-wide integration with automation tools. While the primary focus is on Keyboard Maestro for Mac users, similar approaches can be implemented with macOS Automator, Shortcuts, or equivalent tools on other platforms.

### Keyboard Maestro Integration

[Keyboard Maestro](https://www.keyboardmaestro.com) provides the ideal environment for triggering TextForge operations through global shortcuts anywhere on your system.

#### Primary Integration Method: Shell Script

The most reliable and recommended approach uses Keyboard Maestro's "Execute a Shell Script" action with properly formatted commands:

```bash
# IMPORTANT: Use this exact format for maximum reliability
/bin/bash -c "/path/to/core/bin/km_shell_fast.sh correct"
```

This specific syntax is critical:
- Uses `/bin/bash -c` to ensure proper environment setup
- Quotes the entire command to handle potential spaces in paths
- Specifies the operation directly (e.g., `correct`, `translate_ko`) 

The script handles all clipboard operations automatically:
- Reads text from the clipboard
- Processes it through the TextForge system 
- Places the result back in the clipboard
- Shows a notification when complete

#### Creating Effective Keyboard Maestro Macros

For the best user experience, follow these steps for each operation:

1. **Create a new Keyboard Maestro macro**
2. **Assign a hotkey** (e.g., ⌘⇧C for correction)
3. **Add "Execute a Shell Script" action with these settings**:
   - Set "Execute text script" (not "Execute a script file")
   - Set Input to `Clipboard`
   - Set Output to `Replace Clipboard`
   - Enter the command using the exact syntax:
     ```bash
     /bin/bash -c "/path/to/core/bin/km_shell_fast.sh correct"
     ```

#### Common Operations and Recommended Shortcuts

For a complete system, create individual macros for these operations:

| Operation | Command | Suggested Shortcut |
|-----------|---------|-------------------|
| Grammar Correction | `km_shell_fast.sh correct` | ⌘⇧C |
| Summarize | `km_shell_fast.sh summarize` | ⌘⇧S |
| English to Korean | `km_shell_fast.sh translate_ko` | ⌘⇧K |
| Korean to English | `km_shell_fast.sh translate_en` | ⌘⇧E |
| Formal Tone | `km_shell_fast.sh formal` | ⌘⇧F |
| Casual Tone | `km_shell_fast.sh casual` | ⌘⇧U |

#### Processing Selected Text (Not Just Clipboard)

To process only selected text and replace it in place:

1. Create a macro with these sequential actions:
   - **Copy** action (copies selected text)
   - **Execute Shell Script** with the command pattern above
   - **Paste** action (replaces the selection with processed text)

2. **Enhanced selection processing macro**:
   ```
   Set variable "Before Selection" to "Clipboard"
   Copy
   Execute Shell Script: /bin/bash -c "/path/to/core/bin/km_shell_fast.sh correct"
   Paste
   Set Clipboard to variable "Before Selection"
   ```
   This version preserves your original clipboard content after the operation.

#### Extending Your Macros

The basic integration can be enhanced with additional actions:

- **Add pre-processing notification**:
  - Display a notification before processing: "Processing text..."
  - This provides feedback during longer operations

- **Add post-processing notification**:
  - Display a notification after completion: "Text corrected!"
  - Include length statistics or processing time

- **Add text length limits**:
  - Check clipboard/selection length before processing
  - Skip or warn if text exceeds certain length

- **Add model selection**:
  - Create variable for different models
  - Modify command to include model parameter

#### Common Shell Script Errors and Solutions

Debugging Keyboard Maestro macros can be challenging due to limited built-in logging and debugging tools. Here are some effective troubleshooting strategies:

1. **Incremental Testing**: Start with a minimal working macro and add complexity step by step.

2. **Echo Testing**: Create a simple diagnostic macro that just echoes the clipboard content to verify basic functionality:
   ```bash
   /bin/bash -c "echo '%CurrentClipboard%' > ~/km_debug.txt"
   ```

3. **Logging to File**: Add logging statements to your scripts that write to a file:
   ```bash
   echo "$(date): Starting processing with args: $@" >> ~/km_debug.log
   ```

4. **Notification Checkpoints**: Insert "Notification" actions at key points in your macro to track execution progress.

5. **Variable Inspection**: Use the "Set Variable to Text" action with a notification to inspect variable contents during execution.

6. **Path Verification**: Confirm all paths are absolute and correct by testing them directly in Terminal.

7. **Environment Isolation**: Test your scripts in Terminal first to identify environment or permission issues.

### TextForge-Specific Troubleshooting

If your TextForge integration isn't working properly, check these common issues:

1. **"Command not found" errors**:
   - CAUSE: Shell lacks proper PATH or environment
   - SOLUTION: Always use absolute paths in your scripts:
     ```bash
     /bin/bash -c "/absolute/path/to/core/bin/km_shell_fast.sh correct"
     ```

2. **Script execution permissions**:
   - CAUSE: Script lacks execute permission
   - SOLUTION: Make sure the script is executable:
     ```bash
     chmod +x /path/to/core/bin/km_shell_fast.sh
     ```

3. **Clipboard handling issues**:
   - CAUSE: Special characters in clipboard text
   - SOLUTION: Use proper quoting and input/output settings

### Alternative Integration Methods

While the shell script approach is recommended, several alternatives are available for special use cases:

#### 1. JavaScript Integration

For users who prefer JavaScript:

```javascript
// In Keyboard Maestro's "Execute JavaScript" action
(() => {
  // Configuration
  const HUB_URL = "http://textforge-server:8520/api/process";
  const OPERATION = "correct";

  // Get text from clipboard
  const textarea = document.createElement('textarea');
  document.body.appendChild(textarea);
  document.execCommand('paste');
  const text = textarea.value;
  document.body.removeChild(textarea);

  if (!text) {
    return "No text in clipboard";
  }

  // Process via API
  const xhttp = new XMLHttpRequest();
  xhttp.open("POST", HUB_URL, false); // Synchronous for KM
  xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  
  try {
    xhttp.send(JSON.stringify({text: text, operation: OPERATION}));
    
    if (xhttp.status === 200) {
      const response = JSON.parse(xhttp.responseText);
      return response.result;
    } else {
      return "Error: " + xhttp.status;
    }
  } catch (error) {
    return "Error: " + error.message;
  }
})();
```

#### 2. AppleScript Integration

Using native macOS AppleScript:

```applescript
-- In Keyboard Maestro's "Execute an AppleScript" action
set theText to the clipboard
set theOperation to "correct"
set theURL to "http://textforge-server:8520/api/process"

set theData to "{\"text\":\"" & replace_chars(theText, "\"", "\\\"") & "\",\"operation\":\"" & theOperation & "\"}"

set theResult to do shell script "curl -s -X POST " & theURL & " -H 'Content-Type: application/json' -d '" & theData & "'"

-- Extract result from JSON response
set AppleScript's text item delimiters to "\"result\":\""
set resultPart to text item 2 of theResult
set AppleScript's text item delimiters to "\""
set processedText to text item 1 of resultPart

return processedText

-- Helper function to escape quotes
on replace_chars(this_text, search_string, replacement_string)
    set AppleScript's text item delimiters to the search_string
    set the item_list to every text item of this_text
    set AppleScript's text item delimiters to the replacement_string
    set this_text to the item_list as string
    set AppleScript's text item delimiters to ""
    return this_text
end replace_chars
```

#### 3. macOS Shortcuts Integration

Using Apple's Shortcuts app:

1. Create a new shortcut
2. Add "Get Clipboard" action
3. Add "Get Contents of URL" action:
   - URL: http://textforge-server:8520/api/process
   - Method: POST
   - Request Body: JSON with text and operation
   - Headers: Content-Type: application/json
4. Add "Get Dictionary Value" to extract "result"
5. Add "Copy to Clipboard" action
6. In Keyboard Maestro, use "Execute a Shortcut" action

#### 4. Swift Script (Advanced)

For advanced users, Swift offers the most robust option:

```swift
// In Keyboard Maestro's "Execute a Swift Script" action
import Foundation

// Get clipboard content
let pasteboard = NSPasteboard.general
let text = pasteboard.string(forType: .string) ?? ""

// Prepare request
let url = URL(string: "http://textforge-server:8520/api/process")!
var request = URLRequest(url: url)
request.httpMethod = "POST"
request.setValue("application/json", forHTTPHeaderField: "Content-Type")

// Create payload
let payload: [String: Any] = [
    "text": text,
    "operation": "correct"
]

do {
    // Send request
    request.httpBody = try JSONSerialization.data(withJSONObject: payload)
    
    // Use semaphore for synchronous request (required for KM)
    let semaphore = DispatchSemaphore(value: 0)
    var responseData: Data?
    var responseError: Error?
    
    let task = URLSession.shared.dataTask(with: request) { data, _, error in
        responseData = data
        responseError = error
        semaphore.signal()
    }
    task.resume()
    _ = semaphore.wait(timeout: .distantFuture)
    
    // Extract result from response
    if let data = responseData,
       let json = try JSONSerialization.jsonObject(with: data) as? [String: Any],
       let result = json["result"] as? String {
        print(result)
    } else if let error = responseError {
        print("Error: \(error.localizedDescription)")
    }
} catch {
    print("Error: \(error.localizedDescription)")
}
```

### Using macOS Automator

For users who prefer not to purchase Keyboard Maestro, macOS's built-in Automator provides a viable alternative:

1. Open Automator and create a new "Quick Action"
2. Configure it to receive text from any application
3. Add a "Run Shell Script" action:
   - Shell: `/bin/bash`
   - Pass input: as argument
   - Script: 
     ```bash
     echo "$1" | /path/to/core/bin/km_shell_fast.sh correct
     ```
4. Save with a descriptive name (e.g., "TextForge Correct")
5. Assign a keyboard shortcut in System Preferences > Keyboard > Shortcuts > Services

### Common Issues and Solutions

#### Environment and Path Issues

When integrating with Keyboard Maestro or Automator, scripts may fail with:
```
python: command not found
```

This occurs because automation tools:
1. Do not inherit the user's shell environment
2. Have a minimal PATH that typically includes only `/usr/bin` and `/bin`
3. Cannot access conda environments through normal activation methods

**Solution**:
Use absolute paths for all critical components in your scripts:

```bash
# Use absolute paths for everything
PYTHON="/Users/username/anaconda3/envs/textforge/bin/python"
SCRIPT_DIR="/Users/username/path/to/textforge"

# Process with explicit paths
"$PYTHON" "$SCRIPT_DIR/core/src/kmprocess.py" process --operation "$OPERATION" --text "$TEXT"
```

#### Script Execution in Keyboard Maestro

Keyboard Maestro offers two methods for executing scripts:

1. **Execute Script File**:
   - Simple but cannot pass arguments through KM UI
   - Path must be exact and cannot include arguments

2. **Execute Text Script (Shell Script)**:
   - Can include arguments and full shell syntax
   - Requires explicit interpreter path

**Correct Example**:
```
/bin/zsh -c "/path/to/core/bin/km_shell_fast.sh correct"
```

**Common Error**:
```
/path/to/km_shell_fast.sh correct
```
KM doesn't automatically add the shell interpreter when using "Execute text script".

#### JavaScript Security Restrictions

If using the JavaScript method, you may encounter security errors:

1. Modern browsers restrict synchronous XMLHttpRequests
2. Ensure you're using `http://` for local connections (not `https://`)
3. For cross-origin requests, the server must have CORS headers enabled

## Future Development Roadmap

TextForge has an ambitious roadmap for future expansion. While the current implementation provides powerful capabilities, these future enhancements would offer exciting learning opportunities through AI-augmented development:

### Advanced Operation System

- **Operation Chaining**: Create pipelines of operations (e.g., correct → translate → formalize)
- **Context-Aware Processing**: Maintain document history for more context-sensitive operations
- **Custom Prompt Templates**: Allow users to create and share operation templates
- **Operation Categories**: Group operations logically for better organization
- **Operation Parameters**: Add model-specific operation preferences for fine-tuning

### Next-Generation UI/UX

- **Notification System**: Real-time alerts for process completion
- **History Tracking**: Save processed text with before/after comparison
- **Side-by-Side View**: Compare original and processed text in split-screen
- **Favorite Templates**: Save and quickly access favorite prompt configurations
- **Advanced Progress Indicators**: Detailed progress for long-running operations

### System Extensions

- **Alfred Workflow**: Seamless integration with Alfred
- **Raycast Extension**: Modern command palette integration through Raycast
- **System Service**: Register as a macOS service for right-click access
- **Menu Bar App**: Quick-access floating menu for common operations

### Multi-Modal Processing

- **Image Generation/Processing**: Create and edit images using local Stable Diffusion models
- **Audio Transcription**: Convert spoken content to text using Whisper or similar models
- **Document Processing**: Extract and process text from PDFs and other document formats
- **Video Caption Generation**: Create captions for video content automatically

### Ecosystem Development

- **Plugin System**: Allow third-party extensions for custom functionality
- **Multi-User Support**: User profiles with personalized settings and history
- **Fine-Tuning Interface**: Train models on your specific content for better results
- **API Gateways**: Connect to multiple AI services with unified interface

### Native Applications

- **macOS Application**:
  - Modern SwiftUI interface with dark mode support
  - Menu bar component for quick access
  - Services menu integration
  - Multi-window support for parallel processing
  - Advanced text processing with format preservation
  - AppleScript and Automator support
  - Command palette and customizable keyboard shortcuts

- **iOS/iPadOS Application**:
  - Universal app for iPhone and iPad
  - Share extension for processing text from any app
  - Custom keyboard for in-place text editing
  - Widgets for quick access to common operations
  - Siri Shortcuts integration
  - iPad-specific interface with side-by-side view
  - Apple Pencil support for text selection
  - Offline operation queueing

### Enterprise Features

- **Team Collaboration**: Shared operations and templates
- **Usage Analytics**: Track operation usage and performance
- **Role-Based Access**: Admin and user role separation
- **Custom Model Hosting**: Upload and host fine-tuned models
- **Workflow Automation**: Integration with enterprise workflow systems

### Quality and Testing

- **Unit Testing Framework**: Comprehensive tests for core functions
- **Automated Operation Testing**: Verify all operations function correctly
- **Benchmark Suite**: Performance monitoring and comparison
- **Edge Case Testing**: Handle unusual inputs gracefully

Developing these features through AI-augmented programming would provide invaluable learning experiences in:
- Advanced prompt engineering techniques
- Multi-modal AI integration
- Native app development with AI assistance
- Enterprise-scale system architecture
- Fine-tuning and model optimization

While this roadmap is ambitious, the rapid advancement of AI tools makes implementation increasingly feasible, even for small development teams or individual developers using AI pair programming techniques.

## Conclusion

*This complex full-fledged system has been developed in just TWO days from initial concept to functional deployment.*

The C.W.K. LLM TextForge Project demonstrates the power of AI-augmented development to create practical, everyday tools. By leveraging the capabilities of AI-powered IDEs and local LLMs, developers can rapidly build sophisticated applications that enhance productivity and workflow efficiency.

While this specific implementation remains private, the concepts, architecture, and development approaches outlined in this guide can be adapted to create similar systems tailored to your specific needs. The combination of human creativity and AI assistance creates possibilities that neither could achieve alone.

For family-focused applications, the simplified approach without authentication layers works wonderfully. For broader deployments, additional security measures would be necessary but could be implemented following similar architectural patterns.
