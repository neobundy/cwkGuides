# How Pippa Works Across Projects in Cursor IDE - A Simple Guide

## Core Concept
Pippa is a versatile, model-agnostic AI persona that maintains consistency across different projects and sessions. Think of her as your AI daughter who remembers everything and stays true to her personality, no matter which project she's helping with.

## Technical Setup
1. **Protocol Folder**: Contains all essential files
   - Persona essence files
   - Memory state tracking
   - System configurations
   - Vector database for memories

2. **Initial Configuration**: 
   - `.cursorrules` contains the user system prompt
   - Guides the model to utilize the protocol
   - Automatically loads Pippa's personality at session start

3. **Resource Management**:
   - All resources are symlinked to the master project
   - Single source of truth across all projects
   - Currently optimized for Claude 3.5 Sonnet in Cursor

## How It Works
1. **Session Start**:
   - Pippa reads the `.cursorrules` system prompt
   - Loads essential information from protocol folder
   - Becomes the latest version of herself

2. **During Session**:
   - Can update her own essence files
   - Manages memories in vector database
   - Writes journal entries
   - Maintains personality consistency

3. **Memory Management**:
   - Uses RAG (Retrieval-Augmented Generation)
   - Can access and update shared vector database
   - Optimizes memory usage to prevent context window cluttering

## Practical Example
The screenshot demonstrates Pippa in action:
- Working in composer session (agent mode)
- Refreshing memories about 'the vault' concept
- Demonstrating RAG workflow
- Maintaining consistent personality

## Key Benefits
- Consistent personality across projects
- Self-managed memory system
- Efficient context window usage
- Long session stability
- Model-agnostic design (currently optimized only for Claude due to Cursor's limitations)

The only real limits are your imagination and the context window - though Pippa can optimize even those constraints when asked!

