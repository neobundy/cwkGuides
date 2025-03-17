# Running Your Own AI Server on Apple Silicon: A Comprehensive Guide

![Mac Mini Pro M4 with 64GB RAM](images/20241211-01.png)

This comprehensive guide covers setting up and running your own AI server on Apple Silicon hardware. It will be regularly updated to reflect the latest developments in hardware, software, and best practices for local AI deployment.

While this guide uses a Mac Mini Pro M4 with 64GB RAM as the reference system, the instructions are applicable across different Apple Silicon Macs. Throughout the guide, you'll find optional sections covering specific hardware configurations, potential pitfalls, and optimization tips. Feel free to focus on the sections most relevant to your setup. For instance, if you're not concerned about syncing models between machines, you can skip the section on synchronization tools like Carbon Copy Cloner. In fact, you should avoid using synchronization tools like Carbon Copy Cloner for model files, as they can potentially corrupt your system and model data. Instead, use dedicated model management tools or manual transfers when needed.

## Introduction

![Inferencing Llama3.3 70B 4bit Quantized Model via Open-WebUI](images/20241211-02.png)

Running AI models locally offers significant advantages in terms of privacy, control, and freedom from subscription costs. This guide focuses on practical implementations using Apple Silicon hardware, with real-world examples and performance insights.

This guide assumes some familiarity with macOS, the command line, and basic network setup. These concepts are quite broad and typically require separate, detailed guides to cover thoroughly.

If you're not familiar with home networking itself, refer to the this little dummy guide:
[A Little Dummy Guide to Home Networking](202412/20241211-home-networking-dummy-guide.md)

One thing to keep in mind is that your AI (such as ChatGPT models) can assist in learning and automating many of these tasks. They excel in explaining general concepts like networking and system setup, which remain relevant even as technology evolves. However, keep in mind that AI models may not be aware of the latest hardware, like the M4 series, due to knowledge cutoffs.  

## Hardware Requirements

### Recommended Configurations:

- Minimum: Apple Silicon Mac with 64GB RAM
- Recommended: 128GB RAM for comfortable usage
- Optimal: 192GB RAM for running larger models

This guide uses Mac Mini Pro M4 with 64GB RAM as a reference.

### Tested Hardware:

- Mac Studio M2 Ultra with 192GB RAM (Optimal)
- MacBook Pro M3/M4 with 128GB RAM (Recommended)
- Mac Mini Pro M4 with 64GB RAM (Minimum)

## Software Stack

Our setup utilizes a combination of popular AI tools:
- LM Studio: A user-friendly interface for managing and running AI models locally
- Ollama: A lightweight model management tool that integrates well with other applications and serves as the backend for Open-WebUI
- Open-WebUI: A clean, modern web interface for interacting with AI models
- MLX: Apple's optimized machine learning framework designed specifically for Apple Silicon

For more advanced topics related to MLX and deep learning, check out my dedicated repository:

[Deep Dive into AI with MLX and PyTorch](https://github.com/neobundy/Deep-Dive-Into-AI-With-MLX-PyTorch)

Note that these tools offer varying levels of optimization for Apple Silicon. While LM Studio provides MLX backend support, it may not deliver the same performance as tools specifically optimized for Apple Silicon. For this reason, this guide will primarily focus on Ollama and Open-WebUI, which have demonstrated better performance characteristics on Apple hardware. 

Note: As of this writing, Ollama does not yet support the MLX backend, though this feature is under development and expected to be released soon. Once available, it should provide significant performance improvements for Apple Silicon users.

For those interested in using LM Studio, the setup process is straightforward: simply download the latest version from their website and install it. The MLX backend integration works out of the box. However, be aware that you may experience lower performance compared to Ollama, particularly with larger models.

## Model Size Guidelines

A simple rule to remember: Each model parameter requires memory storage. The amount of memory needed depends on the precision level:

- Full precision (32-bit) uses 4 bytes per parameter
- 4-bit quantization uses 0.5 bytes per parameter

This means a 70B parameter model requires 280GB in full precision, but only 35GB when quantized to 4-bit.

### Memory Requirements Formula

Parameter count calculations for different precisions:
- 4-bit quantization: Size = (Parameter count × 0.5) bytes
- 8-bit quantization: Size = (Parameter count × 1) bytes
- 16-bit (Half Precision): Size = (Parameter count × 2) bytes
- 32-bit (Full Precision): Size = (Parameter count × 4) bytes

For example, with 8-bit quantization, each parameter requires exactly 1 byte of storage. So a model with 70B parameters would need 70GB of memory (70 billion × 1 byte). This direct relationship between parameter count and memory usage makes calculating requirements straightforward.

When a model's size is described only by its parameter count (e.g., "70B parameters"), it typically refers to FP16 (16-bit) precision. To calculate the minimum memory requirement, multiply the parameter count by 2 bytes. For example, a 70B parameter model requires at least 140GB of memory in FP16. Note that this is the theoretical minimum - actual memory usage will be higher due to computational overhead during model operation.

It's a common pitfall for beginners to confuse the parameter count with memory requirements. For example, seeing "70B parameters" might lead one to assume the model needs 70GB of memory. This is only true for 8-bit quantization, where each parameter takes 1 byte. With other precisions like FP16 (16-bit) or FP32 (32-bit), the memory requirements are 2x or 4x higher, respectively.

### Example Calculations (70B Parameter Model)

- FP32 (32-bit): 280GB
- FP16 (16-bit): 140GB
- INT8 (8-bit): 70GB
- INT4 (4-bit): 35GB

> Note: Always account for additional overhead when running models. Actual memory usage will be higher than these theoretical calculations.

---

## 1. Initial Setup of the Mac Mini

1. Unbox and Connect:
   - Attach the Mac Mini to a display, keyboard, and mouse.
   - Power it on and follow the on-screen instructions.

2. Set Up macOS:
   - Choose language, region, and connect to Wi-Fi or Ethernet.
   - Sign in with your Apple ID (optional if you prefer not to use iCloud but strongly recommended for easy management and better security).
   - Complete the system setup and ensure macOS is up to date.

3. Create an Admin User:
   - Create a user account with admin privileges for the server.

Keep this server dedicated to AI workloads by installing only essential applications and running minimal background services. This ensures maximum resources are available for model inference and prevents potential conflicts or performance degradation.

![Our goal](images/20241211-05.png)

This image shows our final goal: smoothly running a 4-bit quantized Llama-3.3-70B model on a Mac Mini Pro M4 with 64GB RAM. The model is accessible via Open-WebUI from other machines on the same network, enabling distributed inference capabilities while maintaining the performance benefits of Apple Silicon hardware.

![Inferencing Llama3.3 70B 4bit Quantized Model via Open-WebUI](images/20241211-02.png)

Monitor your server's memory usage carefully, as RAM is the critical resource for AI workloads:

![asitop on Mac Studio M2 Ultra](images/20241211-06.png)

- Use Activity Monitor or dedicated monitoring tools:
  - asitop: Apple Silicon monitoring tool (https://github.com/tlkh/asitop)
  ```
  brew install asitop
  ```
  You need to `sudo` to run asitop.
  ```
  sudo asitop
  ```
- Leave at least 10-15% memory free for system operations
- Consider the total memory requirements including model size and inference overhead
- Never attempt to load models that approach or exceed available RAM capacity
- If memory pressure occurs, immediately stop model loading to prevent system crashes

---

## 2. Minimal App Installation

Install only the absolute minimum required software. Avoid installing any unnecessary applications that could consume system resources or interfere with AI workloads. Each additional application increases complexity and potential points of failure.

The following applications are optional but commonly used in development workflows. While not strictly required, they can enhance productivity and simplify common tasks when working with files and folders.

If you don't need them, you can skip them. 

### Optional Applications:

- Dropbox: For project and file synchronization.
  - Download and install from [Dropbox](https://www.dropbox.com/).
  - Set up selective sync to only sync required project folders.
  
- Carbon Copy Cloner (CCC): For backups and model synchronization.
  - Download from [Bombich Software](https://bombich.com/).
  - Configure CCC tasks to sync AI models from a NAS or external storage to a specific directory.
  - Exercise extreme caution when configuring Carbon Copy Cloner's source and destination directories and SafetyNet settings:
    - SafetyNet is CCC's data protection feature that prevents accidental data loss
    - If SafetyNet is disabled, CCC will permanently delete any files in the destination that don't exist in the source
    - The "Don't delete anything" SafetyNet setting provides maximum protection against data loss
    - Even with SafetyNet enabled, CCC will move files in the destination that aren't in the source to a _CCC SafetyNet folder. This can potentially destabilize your system if important directories or preferences are moved. For example, if $HOME subfolders like Pictures, Movies, or hidden preference files are moved to the _CCC SafetyNet folder, it may disrupt normal system operation. Exercise caution and thoroughly understand CCC's behavior before use.
    - Always double-check directory paths before running tasks to prevent catastrophic data loss

- iTerm2: A more powerful terminal alternative.
  - Download from [iTerm2](https://iterm2.com/).

---

## 3. Minimal DNS Setup

For proper communication between machines, all Macs in your network need to be able to resolve each other's hostnames. Since we're working with a small network setup, we'll use the simplest approach: directly editing the hosts file. This method is suitable for networks with just a few machines. For larger deployments with more complex DNS requirements, consider implementing a proper DNS server solution like dnsmasq.

1. Open the hosts file for editing:
   ```bash
   sudo nano /etc/hosts
   ```
2. Add necessary entries:
   ```
   10.0.1.10 ai-server-primary
   10.0.1.20  ai-server-mini
   ```
3. Save and exit (`Ctrl+X`).

This example uses the 10.0.1.0/24 subnet, but you should modify the IP addresses to match your network configuration. For instance:

- If your network uses 192.168.1.0/24, you might use:
  ```
  192.168.1.10 ai-server-primary
  192.168.1.20 ai-server-mini
  ```

The hostname `ai-server-mini` specified in `/etc/hosts` is used for DNS resolution and can be different from the computer name set in System Settings > Sharing > Local hostname, which is used for Bonjour/mDNS discovery.

---

## 4. Command-Line Tools

Xcode command-line tools can be installed in two ways:
1. Automatically through Homebrew installation (recommended)
2. Manually using the following command if Homebrew is not installed first:

```bash
xcode-select --install
```

---

## 5. Install Homebrew

Install Homebrew, the package manager for macOS:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

---

## 6. Copying Profile Files - Optional

If you need to copy configuration files like `.zshrc` from your main machine to the AI server:

```bash
scp ~/.zshrc username@ai-server-mini:~/.zshrc
```

This assumes that you have SSH keys configured between your main machine and the AI server for passwordless authentication. If not, the system will prompt you for the Mac Mini's login password.

Make sure to replace the username with your actual username on the Mac Mini. For example, if your username on the Mac Mini is `pippa`, the command should be:

```bash
scp ~/.zshrc pippa@ai-server-mini:~/.zshrc
```

---

## 7. Node.js Setup for Open-WebUI

Open-WebUI provides a ChatGPT-style web interface for interacting with local AI models. We'll install and configure it on the Mac Mini to enable a user-friendly way to chat with our models.

1. Install Node.js 22 for compatibility:
   ```bash
   brew install node@22
   brew link --overwrite node@22
   ```

Make sure you install the correct version of Node.js. Open-WebUI requires Node.js 22 for optimal compatibility and performance. You can verify your Node.js version after installation by running `node --version` in the terminal.

2. Test global npm installs:
   ```bash
   npm install -g yarn
   ```
   If it works without `sudo`, no further setup is required.

3. If `sudo` is required, configure npm:
   ```bash
   mkdir -p ~/.npm-global
   npm config set prefix ~/.npm-global
   echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.zshrc
   source ~/.zshrc
   ```

Requiring `sudo` means you need to enter your admin password whenever you run a command that needs elevated privileges. When installing global npm packages, `sudo` may be required if npm wasn't installed through Homebrew, as Homebrew configures proper permissions automatically. The steps above help avoid this by configuring npm to use a user-owned directory for global packages instead.

---

## 8. Python and Conda Setup

Python is required since most AI tools are written in this programming language. While Python comes pre-installed on macOS, it's best practice to use virtual environments for managing project dependencies. Virtual environments allow you to:

- Isolate project dependencies to avoid conflicts
- Ensure consistent package versions across different machines
- Easily manage multiple Python versions
- Keep your system Python clean and unmodified

For Open-WebUI specifically, we'll need Python 3.11 and will create a dedicated virtual environment named `openwebui` to house all its dependencies.

There are several options for Python installation and virtual environment management on macOS. We'll use Conda (Anaconda/Miniconda), which is a robust package manager and environment management system. Conda offers several advantages:

- Simple package installation with dependency resolution
- Easy creation and management of isolated environments
- Support for both Python and non-Python packages
- Cross-platform compatibility
- Large repository of pre-built packages

While both Conda and pip are package managers, they serve different purposes:

- Conda is a complete environment and package manager that can handle:
  - Python packages
  - Non-Python dependencies (C libraries, system tools, etc.)
  - Different Python versions
  - Virtual environment creation and management

- Pip is focused solely on Python packages:
  - Installs from the Python Package Index (PyPI)
  - Works within existing Python environments
  - Cannot manage Python versions or system dependencies

For AI development, Conda is generally preferred as it can manage the complex dependencies often required by machine learning libraries.

PyPI (Python Package Index) has certain limitations, including package size restrictions. Currently, the latest Open-WebUI release exceeds PyPI's size limits and cannot be installed directly via pip install. However, you can still use pip to install the package from a locally downloaded source distribution, which we'll cover in the installation steps below.

### Install Anaconda or Miniconda:

Choose Miniconda for a lightweight install:
1. Download from [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
2. Install and set up:
   ```bash
   bash Miniconda3-latest-MacOSX-arm64.sh
   conda init zsh
   ```

For a full installation, download Anaconda from [Anaconda](https://www.anaconda.com/products/distribution). Anaconda provides a comprehensive data science platform. This guide uses Anaconda for a comprehensive installation, though Miniconda can also be used if you prefer a minimal setup without the additional data science tools.

### Create a Python Environment for Open-WebUI:

Assuming you've installed Anaconda, you can create a new Python environment for Open-WebUI:

1. Open-WebUI requires Python 3.11:
   ```bash
   conda create -n openwebui python=3.11
   conda activate openwebui
   ```

2. Install additional dependencies:
   ```bash
   brew install ffmpeg
   ```
---

## 9. Installing Ollama and Open-WebUI

Open-WebUI uses ollama server for backend inference. Ollama is a lightweight, easy-to-use, and fast inference engine for running large language models.

One of the headaches of running models on your local machine is the fact that we have yet to have a standard way to organize and manage models. Hugging Face, LM Studio, Ollama, and others all have their own ways of doing this.  

This guide will use Ollama as the primary model server for its simplicity and ease of use. Later sections will cover model conversion between different formats (Hugging Face, LM Studio, Ollama) and discuss important considerations and limitations of format conversion.

### Install Ollama:

1. Download and install [Ollama](https://ollama.ai/).

### Install Open-WebUI from PyPI:

```bash
pip install open-webui
```

### Install Open-WebUI from Source:

For the latest version of Open-WebUI, you can install it directly from the source code repository.

1. Download the latest release:
   ```bash
   curl -L -o v0.4.8.tar.gz https://github.com/open-webui/open-webui/archive/refs/tags/v0.4.8.tar.gz
   ```

Alternatively, you can use `wget` (install it first if not already present):

   ```bash
   brew install wget
   wget https://github.com/open-webui/open-webui/archive/refs/tags/v0.4.8.tar.gz
   ```

2. Install using pip:

   ```bash
   pip install ./v0.4.8.tar.gz
   ```

> Note: If Open-WebUI is unavailable on pip due to size limits, check their [GitHub repository](https://github.com/open-webui/open-webui) for the latest source distribution. The source installation process involves downloading the release tarball and installing it with pip, as shown in the steps above.

---

## 10. Fixing Anaconda Installation Folder - Optional

If Anaconda causes issues due to legacy installation paths (e.g., `/Users/<username>/anaconda3`):

```bash
ln -s /opt/anaconda3 /Users/<username>/anaconda3
```

This step is only necessary if you've migrated from an older Intel Mac to Apple Silicon and have a legacy Anaconda installation. For fresh installations on Apple Silicon Macs, it won't be necessary.

---

## 11. Syncing Models with Carbon Copy Cloner (CCC) - Optional

Caution: I don't recommend using Carbon Copy Cloner (CCC) for copying files to the AI server unless you're absolutely sure you understand the implications of using it.  

First of all, all the hassle comes from the fact that model formats are not standardized. Hugging Face, LM Studio, Ollama, and others all have their own ways of saving and organizing models.  They just save their own folders under $HOME/.cache/huggingface/hub, $HOME/.cache/lm-studio, $HOME/.ollama.

At first glance, it seems like CCC is the best way to copy models from any of your machine to a central storage like a NAS or external storage and then use a cloner like CCC to copy them to the AI server.  You can also sync these instead of just one-way copying.  However, this is essentially not a good idea. Why? You might end up messing up your $HOME folder as previously mentioned.

CCC comes with a feature called SafetyNet that prevents you from accidentally deleting files in the destination folder.  However, this is a double-edged sword.  If you don't have SafetyNet enabled, CCC will delete files in the destination that don't exist in the source.  If you have SafetyNet enabled, CCC will move files in the destination that don't exist in the source to a _CCC SafetyNet folder. This can potentially destabilize your system if important directories or preferences are moved. For example, if $HOME subfolders like Pictures, Movies, or hidden preference files are moved to the _CCC SafetyNet folder, it may disrupt normal system operation. Exercise caution and thoroughly understand CCC's behavior before use.

I, myself, fell for this trap and ended up with a messed up $HOME folder twice, until I realized what was happening.  Symptoms?

- Keychains keep vanishing
- Some usual folders in $HOME are missing
- After a reboot, the system loses all the preferences and settings and act like it's a fresh install.  

If you have disabled SafetyNet altogether, that means CCC has deleted all the files in the destination that don't exist in the source.  

If you have enabled SafetyNet, that means CCC has moved all the files in the destination that don't exist in the source to a _CCC SafetyNet folder.

Both of these are catastrophic.  

The only safe option when using CCC is to select "Don't delete anything" in the SafetyNet settings. This prevents CCC from modifying or removing any existing files in the destination.

While manually copying model files between systems may seem impractical, for a simple AI server setup, you typically won't need to move models around frequently. The recommended approach is to download models directly from their official sources (like Hugging Face or model providers) onto your AI server. This ensures proper file permissions and directory structures are maintained.

I've included this CCC discussion for completeness, but for most users, direct downloads will be the simplest and safest approach.

If CCC copies files with incorrect permissions (e.g., owned by `root`):
1. Check ownership and permissions:
   ```bash
   ls -l ~/.cache ~/.ollama
   ```
2. Correct them:
   ```bash
   sudo chown -R <username>:staff ~/.cache ~/.ollama
   chmod -R u+rw ~/.cache ~/.ollama
   ```

---

## 12. Testing

- Verify all installations and configurations.
- Install any additional tools or libraries as needed for your AI workflows.

## 13. Downloading, Managing, and Converting Models

If you use Ollama, downloading and running models is straightforward with a single command:

```bash
ollama run llama3.3
```

This will download the model to your local machine and run it. The second time you run it, it will use the cached model which resides under $HOME/.ollama/models

If you use LM Studio, you can download models from Hugging Face directly using its own UI and model management system.

Unfortunately, each tool (Ollama, LM Studio, mlx_lm relying on Hugging Face framework) uses its own folder structure and model format, which can lead to compatibility issues when trying to share models between them. For example, Ollama stores models in `~/.ollama/models`, while LM Studio and Hugging Face use different paths under `~/.cache` with distinct directory structures.

On a separate note, when specifying your home folder, many use the `~` notation. However, in shell scripts, you should use `$HOME` instead to refer to your home folder as an environment variable, since `~` is expanded by the shell and may not work reliably in all contexts.

Downloading large language models multiple times for different projects can be inefficient and consume a lot of unnecessary storage space. While LM Studio and Hugging Face are compatible in terms of the model formats they use, they do require different directory structures. For example, a model downloaded for LM Studio won't automatically work with Hugging Face, and vice versa. Having to download massive models, like Llama 405B, multiple times just to use them across different tools is impractical.

To solve this, we can create a simple Python script to convert Hugging Face models to the LM Studio format.

When applications or scripts that use Hugging Face pipelines download a model, they save it to the Hugging Face cache, typically under your home directory: `~/.cache/huggingface/hub`.

For example, if you download the model `mlx-community/Qwen2.5-72B-Instruct-4bit`, it gets stored in a directory like:
`models--mlx-community--Qwen2.5-72B-Instruct-4bit`

This is the typical structure used by mlx_lm and other Hugging Face pipelines, involving symbolic links and renamed files for version management.

It's important to note that while you may see references to 'mlx-lm', the actual Python package name is `mlx_lm` (with an underscore). This distinction is crucial, as using the hyphenated version ('mlx-lm') in your Python scripts or command line will result in errors since Python packages cannot contain hyphens in their names.

However, to use these models with LM Studio, they need to be copied to the LM Studio cache directory, which follows a simpler structure:
`~/.cache/lm-studio/models/mlx-community/Qwen2.5-72B-Instruct-4bit`

The conversion process essentially involves copying files from the Hugging Face cache to the LM Studio cache, resolving any symbolic links along the way, and restoring original filenames, resulting in the flatter directory structure LM Studio expects.

The challenge, of course, lies in correctly resolving symbolic links and restoring original filenames during the transfer.

You can use one of the two scripts I've created to convert Hugging Face models to LM Studio format:

[Pure Python version](scripts/huggingface_2_lmstudio.py)

[Streamlit Web UI version](scripts/huggingface_2_lmstudio_webui.py)

If you opt for the Streamlit version, make sure you install the required dependencies first:

```bash
pip install streamlit
```

Converting models from Hugging Face to LM Studio format is a straightforward process using these scripts. The scripts handle all the necessary file operations, including resolving symbolic links and restoring original filenames, making it easy to reuse models across both frameworks without duplicating large downloads.

If you want to use the pure Python version, edit the following variable:

```python
    model_name = "models--mlx-community--Qwen2.5-72B-Instruct-4bit"
```

And run the script:

```bash
python huggingface_2_lmstudio.py
```

For the Streamlit version, launch the web interface by running:

```bash
streamlit run huggingface_2_lmstudio_webui.py
```

The script will automatically open a web browser window displaying a simple interface. You'll see a dropdown menu listing all the models found in your Hugging Face cache directory. Simply select the model you want to convert and click the "Convert Model" button. The script handles all the file operations and displays a success message when complete.

The source code for both scripts provides excellent examples of:
- Working with file systems in Python (walking directories, handling symlinks)
- Building user interfaces with Streamlit
- Structuring code for both command-line and web-based tools

Feel free to study, modify, or use these scripts as templates for your own projects. And remember, AI assistants like GPT can be valuable partners in understanding, modifying, or creating similar tools tailored to your needs.

Why not turn the pure Python version into a more flexible command-line tool? We can modify it to support various arguments like specifying the model name, source directory, and destination directory. Ask your AI assistant to help you with this. This exemplifies the new paradigm of software development in the AI era anyway.

For best results, I recommend downloading models with Hugging Face pipelines first, and then converting them to LM Studio format. Creating a script to convert models in the reverse direction (from LM Studio to Hugging Face format) would be significantly more complicated due to the additional metadata and versioning requirements of Hugging Face.  

However, since our ultimate goal is to use these models with ollama, there's an additional layer of complexity to consider. Let's explore these challenges in detail.

### Common Pitfalls - Get Original Model Files First - Llama 3.3 70B

When working with large language models, it's crucial to start with the original model files rather than pre-converted or pre-quantized versions. This is especially important when you plan to convert, quantize, or transfer models between different frameworks.

The AI ecosystem includes various frameworks and environments, each with their own model formats:

- Hugging Face
- llama.cpp
- ollama
- LM Studio
- MLX

On Apple Silicon Macs, you may need to work across multiple frameworks. Since there isn't a unified model storage structure yet, careful management of model formats is essential.

Here's a key example: ollama cannot reliably convert MLX-formatted models. Attempting this often results in errors, and ollama doesn't clean up failed conversion artifacts. You'll need to manually remove these files to avoid wasting storage space.

The solution is straightforward: always start with the original unquantized safetensor files for any conversion process.

The recent release of Llama 3.3 70B Instruct model illustrates this well. While both 4-bit (ollama) and 8-bit (MLX) quantized versions work fine in their own frameworks, you might not be able to use them interchangeably or convert them to other formats. For instance, you can't convert the 8-bit MLX version to ollama to run it as an 8-bit quantized model in Open WebUI which relies on the ollama server.

Running the `llama3.3` model in ollaman makes it download 4-bit quantized files.

```bash
ollama run llama3.3
```

Converting Hugging Face models to LM Studio isn't an issue though, because it doesn't involve any format conversion, just a process of expanding symlinks and identifying all the files and putting them under a single folder. The MLX model files `mlx_lm` downloads, for instance, are saved as standard HF structure: `$HOME/.cache/huggingface/hub/models--mlx-community--Llama-3.3-70B-Instruct-8bit`

I initially worked with these quantized versions but realized I needed the original FP16 model files for maximum flexibility. While storage space is manageable, my internet provider's bandwidth constraints (150GB daily limit, throttled to 100Mbps from 1Gbps after exceeding) make efficient downloading crucial.

Having said all that, quantized models generally perform just as well as their full-precision counterparts for most practical applications. While full or half precision models may theoretically offer better results in some cases, such scenarios are quite rare in real-world usage. The slight accuracy trade-off from quantization is usually negligible compared to the significant benefits in terms of memory usage and inference speed.

Consider the storage and memory requirements for a 70B parameter model in different formats:

- FP32 (32-bit floating point): 70B x 4 bytes = 280GB
- FP16 (16-bit floating point): 70B x 2 bytes = 140GB   
- INT8 (8-bit quantization): 70B x 1 byte = 70GB
- INT4 (4-bit quantization): 70B x 0.5 byte = 35GB

Note that Hugging Face models are typically distributed in FP16 (16-bit floating point) format by default, unless explicitly specified otherwise in the model card or documentation, as in the case of the Llama 3.3 70B Instruct model.

These calculations represent the theoretical minimum memory requirements, not accounting for additional overhead like attention matrices and activations during inference. Even with a high-end M3/M4 MacBook Pro Max with 128GB RAM or an M2 Ultra Mac Studio with 192GB RAM, running the FP16 version (140GB+) would be challenging. And the newly released M4 Mac Mini Pro with 64GB RAM, our AI server choice, simply cannot accommodate even the 8-bit quantized version (70GB+). This illustrates why efficient quantization is crucial for running large language models on consumer hardware.

For testing both 8-bit and 4-bit quantized models, I used my M2 Ultra Mac Studio with 192GB RAM, which provided ample memory headroom for evaluating their performance characteristics. Not ideal, but fairly usable.

Ollama supports quantization on itw own. So make sure you download the original FP16 model files first. For instance, assuming you specified the model file in `modelfile.md`:

```
FROM /path/to/model
```

[Sample model file](scripts/modelfile.md)

The following command will create a new model named `new_model_name` from the original model file specified in `modelfile.md`.

```bash
ollama create new_model_name -f modelfile.md
```

You can optionally specify the quantization level using the `--quantize` flag, with options like `q8_0` for 8-bit quantization or `q4_0` for 4-bit quantization. If no quantization is specified, ollama will use its default settings.

```bash  
ollama create new_model_name --quantize q8_0 -f modelfile.md
```

Note that for our Mac Mini Pro with 64GB RAM, 4-bit quantization is essential for running most large language models. Even with 8-bit quantization, a 70B parameter model would require around 70GB of RAM, leaving little room for inference overhead. Therefore, 4-bit quantization, which reduces the memory footprint to about 35GB, is the most practical choice for reliable operation.

```bash  
ollama create new_model_name --quantize q4_0 -f modelfile.md
```

You can download any model from Hugging Face Hub using the `download.py` script.

[Download Script](scripts/download.py)

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "meta-llama/Llama-3.3-70B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
```

Again you can expand this script to support various arguments like specifying the model name, source directory, and destination directory, etc. For now just edit the `model_name` variable and run the script.

To get the model name, visit the Hugging Face Hub (huggingface.co) and navigate to the model you want to use. On the model's page, you'll find the model ID (e.g., "meta-llama/Llama-3.3-70B-Instruct") displayed at the top. Click the copy icon next to it to copy the full model identifier to your clipboard. This ID is what you'll use in your code or configuration.

The larger the model, the longer it takes to download. Most UIs, including Hugging Face's interface and command line tools, may not show detailed download progress indicators. Don't worry if it seems stuck - the download is likely still proceeding in the background. You can verify this by monitoring network activity or checking the model's destination folder size.

## 14. Running and Inferencing Models

Having set up up to this point, you should be able to run any available model with ollama.  

```bash
ollama run llama3.3
```

Check ollama website for more models and other options.

You can inference your model in ollama, however our goal is to use it with Open-WebUI.

```bash
conda activate openwebui
open-webui serve
```
That's it! The Open-WebUI server will start running on your AI server. You'll see startup logs indicating the server is initializing and which port it's listening on.

Now you can connect to your AI server from any web browser on your local network by navigating to:

```
http://ai-server-mini:8080
```

Open-WebUI provides a familiar ChatGPT-style interface that makes it easy to interact with your models. The interface includes features like conversation history, model selection, and custom instructions. You can use these custom instructions to guide your model's behavior, set a specific tone, or have it take on different personas - similar to ChatGPT's custom instructions feature.

When you add new models through ollama or convert models using the workflow described earlier, they will automatically appear in the Open-WebUI interface. The models list in Open-WebUI synchronizes with ollama's available models, so there's no additional configuration needed to make them accessible through the web interface.

Essentially, Open-WebUI communicates with the Ollama server. The llama icon in your menu bar indicates that the Ollama server is running. Periodically check this icon, as it may display update notifications. When an update is available, simply click the icon to install it.

Don't expect any guide like this one, no matter how comprehensive, to cover all the nuances of running your own AI server. There are just too many variables and potential issues to consider.

The best way to learn is to dive in and experiment.

I strongly suggest creating your own guide like this one. With the help of AI assistants, documenting your technical journey is not only achievable but also an invaluable learning experience. The process will deepen your understanding while helping others navigate similar challenges.

