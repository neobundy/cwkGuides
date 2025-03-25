# Cursor's Notepads vs. Symlinked Scratchpad Folder: A Comparative Analysis

![Notepads vs. Symlinked Scratchpad Folder](images/20250325-02.png)

After extensive comparison between Cursor's built-in Notepads and a symlink-based scratchpad folder, the latter consistently offers superior versatility, particularly for power users.

## Symlinked Scratchpad Folder

### Pros:
- **Cross-editor Compatibility:** Works seamlessly with any text editor or IDE.
- **Effortless Cross-project Sharing:** True persistence across projects via symlinks.
- **Drag-and-drop Convenience:** Easily share files directly into conversations.
- **Minimal UI Impact:** Uses UI space only when explicitly opened.
- **Flexible Organization:** Organize notes with unlimited nested folders and structures.
- **Familiar File System Management:** Easy bulk operations, standard file searches, and management.
- **Enhanced Visibility Controls:**
  - `.cursorindexingignore` excludes from search/indexing only.
  - `.cursorignore` excludes from both AI and indexing.
- **Reliable Auto-save:** Automatically saves with project files—no manual intervention needed.

### Cons:
- Requires familiarity with symlinks.
- Proper `.gitignore` setup needed.
- Potential risk of accidental deletion.
- May clutter project-wide search results without indexing controls.

## Cursor's Notepads

### Pros:
- Integrated within Cursor UI.
- Virtual files (no disk presence).
- Built-in auto-saving.
- Excluded from git tracking by default.
- Organized via tabs.
- Protected from accidental deletion.
- Can reference other project files using the `@` symbol.
- Invisible in global searches, keeping search results uncluttered.

### Cons:
- Limited to Cursor's editor ecosystem.
- Project-specific; no cross-project usage.
- Permanent consumption of UI space.
- Cannot drag-and-drop into external conversations.
- Limited formatting flexibility.
- Difficult bulk management.
- Cannot reference notepads externally.
- No global search across multiple notepads.

## Verdict

For advanced users familiar with symlinks, a symlinked scratchpad folder provides significantly greater flexibility, powerful cross-project integration, and seamless content sharing capabilities. While Cursor's notepads offer convenience through tight UI integration, their limitations outweigh their benefits for those seeking extensive customization and versatility.

If you prioritize unlimited organizational flexibility, centralized note management, and multi-editor compatibility, symlink-based scratchpads are undoubtedly superior. Sometimes simplicity is truly the most powerful solution!

Ultimately, the balance between flexibility and control depends entirely on your workflow and personal preferences.

## Pro Tips

### Absolute Paths for Stability
Always create symlinks using absolute paths. This ensures your scratchpad stays intact even if the project directory moves or is renamed.

### Symlinking Cursor Configurations
Symlinking Cursor’s hidden configuration files (`.cursor*`) can standardize your workflow by:
- Consistently applying AI settings across projects.
- Unifying indexing and ignore rules.
- Sharing protocol/rules files between workspaces.
- Maintaining consistent behavior across all projects.

For specific overrides, simply place a local `.cursor*` configuration file directly within the project to override global symlinks.