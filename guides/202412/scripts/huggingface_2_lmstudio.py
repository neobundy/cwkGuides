import os
import shutil

def convert_huggingface_to_lmstudio(model_name):
    """
    Converts a Hugging Face model directory to LM Studio format,
    resolving symbolic links and restoring original file names.
    
    Args:
        model_name (str): The name of the model to convert.
    """
    # Define prefixes for Hugging Face and LM Studio
    home_dir = os.path.expanduser("~")
    hf_prefix = os.path.join(home_dir, ".cache/huggingface/hub")
    lmstudio_prefix = os.path.join(home_dir, ".cache/lm-studio/models")

    # Full paths for source and destination
    hf_model_path = os.path.join(hf_prefix, model_name)
    lmstudio_model_path = os.path.join(
        lmstudio_prefix,
        model_name.replace("models--", "").replace("--", "/")
    )

    # Check if Hugging Face model path exists
    if not os.path.exists(hf_model_path):
        raise FileNotFoundError(f"Hugging Face model path does not exist: {hf_model_path}")

    # Create LM Studio path if it doesn't exist
    os.makedirs(lmstudio_model_path, exist_ok=True)

    # Locate the snapshots folder
    snapshots_path = os.path.join(hf_model_path, "snapshots")
    if not os.path.exists(snapshots_path):
        raise FileNotFoundError(f"Snapshots folder not found: {snapshots_path}")
    
    # Use the latest snapshot
    snapshot_subdirs = sorted(os.listdir(snapshots_path))
    if not snapshot_subdirs:
        raise FileNotFoundError(f"No snapshots found in: {snapshots_path}")
    latest_snapshot = os.path.join(snapshots_path, snapshot_subdirs[-1])

    # Copy files, restoring symbolic links
    for root, _, files in os.walk(latest_snapshot):
        for file in files:
            src_path = os.path.join(root, file)
            dest_path = os.path.join(lmstudio_model_path, file)

            # If it's a symbolic link, resolve it and restore the original name
            if os.path.islink(src_path):
                target_path = os.readlink(src_path)
                resolved_path = os.path.join(hf_model_path, target_path.lstrip("../../"))
                if os.path.exists(resolved_path):
                    shutil.copy2(resolved_path, dest_path)
                else:
                    print(f"Warning: Resolved path does not exist for {src_path}")
            else:
                # Regular file, copy directly
                shutil.copy2(src_path, dest_path)

    print(f"Model '{model_name}' converted to LM Studio format at: {lmstudio_model_path}")

# Example usage
if __name__ == "__main__":
    # Specify the model name
    model_name = "models--mlx-community--Qwen2.5-72B-Instruct-4bit"

    try:
        convert_huggingface_to_lmstudio(model_name)
    except Exception as e:
        print(f"Error: {e}")