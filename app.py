
import os

# Store Hugging Face model downloads on D: instead of C:
os.environ["HF_HOME"] = r"D:\huggingface_cache"
os.environ["HF_HUB_CACHE"] = r"D:\huggingface_cache\hub"
os.environ["HF_XET_CACHE"] = r"D:\huggingface_cache\xet"

import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="AI News Summarizer",
    page_icon="📰",
    layout="centered"
)

# Your fine-tuned T5 model on Hugging Face
MODEL_NAME = "vashu-7/t5-news-summarizer-v2"


# -----------------------------
# Load model once and cache it
# -----------------------------
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = model.to(device)
    model.eval()

    return tokenizer, model, device


# -----------------------------
# Summarize the article
# -----------------------------
def summarize_article(article, tokenizer, model, device):
    inputs = tokenizer(
        "summarize: " + article,
        return_tensors="pt",
        max_length=512,
        truncation=True
    ).to(device)

    with torch.inference_mode():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=100,
            num_beams=4,
            no_repeat_ngram_size=3,
            early_stopping=True
        )

    summary = tokenizer.decode(
        output_ids[0],
        skip_special_tokens=True
    ).strip()

    return summary


# -----------------------------
# Streamlit user interface
# -----------------------------
st.title("📰 AI News Summarizer")

st.write(
    "Paste a news article below and generate a concise summary "
    "using a fine-tuned T5 model."
)

article = st.text_area(
    "News article",
    height=250,
    placeholder="Paste your news article here..."
)

if st.button("Generate Summary", type="primary"):
    if not article.strip():
        st.warning("Please paste a news article first.")
    else:
        try:
            with st.spinner("Loading model and generating summary..."):
                tokenizer, model, device = load_model()

                summary = summarize_article(
                    article,
                    tokenizer,
                    model,
                    device
                )

            st.subheader("Generated Summary")
            st.write(summary)

            st.caption(
                f"Model: {MODEL_NAME} | Device: {device.upper()}"
            )

            with st.expander("View original article"):
                st.write(article)

        except OSError:
            st.error(
                "The model could not be loaded. Check your internet "
                "connection, Hugging Face access, and disk space."
            )

        except Exception as error:
            st.error("Something went wrong while generating the summary.")
            st.exception(error)


st.divider()
st.caption(
    "Built with Streamlit, PyTorch, and Hugging Face Transformers."
)
