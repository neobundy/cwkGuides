import os
import shutil
import streamlit as st

def list_huggingface_models(cache_dir):
    """
    Lists available models in the Hugging Face cache directory.
    """
    models = []
    for root, dirs, _ in os.walk(cache_dir):
        for dir_name in dirs:
            if dir_name.startswith("models--"):
                models.append(os.path.join(root, dir_name))
        break  # Only look at the top level
    return models

def convert_model(hf_model_path, lmstudio_model_path):
    """
    Converts a Hugging Face model to LM Studio format.
    """
    snapshots_path = os.path.join(hf_model_path, "snapshots")
    if not os.path.exists(snapshots_path):
        return f"Snapshots folder not found for {hf_model_path}"
    
    snapshot_subdirs = sorted(os.listdir(snapshots_path))
    if not snapshot_subdirs:
        return f"No snapshots found in: {snapshots_path}"
    latest_snapshot = os.path.join(snapshots_path, snapshot_subdirs[-1])
    
    for root, _, files in os.walk(latest_snapshot):
        for file in files:
            src_path = os.path.join(root, file)
            dest_path = os.path.join(lmstudio_model_path, file)

            if os.path.islink(src_path):
                target_path = os.readlink(src_path)
                resolved_path = os.path.join(hf_model_path, target_path.lstrip("../../"))
                if os.path.exists(resolved_path):
                    shutil.copy2(resolved_path, dest_path)
            else:
                shutil.copy2(src_path, dest_path)

    return f"Model converted to: {lmstudio_model_path}"

# Streamlit UI
st.title("Hugging Face to LM Studio Model Converter")

# User paths
home_dir = os.path.expanduser("~")
hf_cache_dir = os.path.join(home_dir, ".cache/huggingface/hub")
lmstudio_base_dir = os.path.join(home_dir, ".cache/lm-studio/models")

st.sidebar.header("Paths")
st.sidebar.text_input("Hugging Face Cache Directory", hf_cache_dir, disabled=True)
st.sidebar.text_input("LM Studio Base Directory", lmstudio_base_dir, disabled=True)

# List models
models = list_huggingface_models(hf_cache_dir)
if not models:
    st.error("No models found in the Hugging Face cache.")
else:
    selected_model = st.selectbox("Select a model to convert", models)
    convert_button = st.button("Convert Model")

    if convert_button:
        model_name = os.path.basename(selected_model).replace("models--", "").replace("--", "/")
        lmstudio_model_path = os.path.join(lmstudio_base_dir, model_name)
        os.makedirs(lmstudio_model_path, exist_ok=True)
        result = convert_model(selected_model, lmstudio_model_path)
        st.success(result)