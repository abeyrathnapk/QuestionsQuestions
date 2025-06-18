# RAG Embedding Pipeline using Gemini and NumPy

"""
This script will:
- Collect all markdown files from image-free-course-content and discourse_markdown
- Chunk each file into overlapping chunks (300-500 tokens, 100 token overlap)
- Use Gemini embedding API to embed each chunk
- Save all embeddings in a NumPy .npy file
- Save metadata (file, chunk index, text) in a JSON file
"""

import os
import glob
import json
import numpy as np
from tqdm import tqdm
from typing import List, Dict
import google.generativeai as genai
import openai

# --- CONFIG ---
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
INPUT_FOLDERS = ["image-free-course-content", "discourse_markdown"]
EMBEDDING_DIM = 768  # Update to Gemini's embedding size
EMBEDDING_MODEL = "gemini-embedding-001"  # Update as needed
OPENAI_EMBEDDING_MODEL = "text-embedding-3-large"  # Or another available embedding model

# --- SIMPLE WORD-BASED CHUNKER (no external dependencies) ---
def chunk_text(text: str, chunk_size: int, overlap: int):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = words[i:i+chunk_size]
        if len(chunk) < 20:  # skip very small chunks
            break
        chunks.append(' '.join(chunk))
        i += chunk_size - overlap
    return chunks

# --- EMBEDDING FUNCTION ---
def get_gemini_embedding(text: str) -> np.ndarray:
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY environment variable not set.")
    genai.configure(api_key=api_key)
    result = genai.embed_content(
        model="models/embedding-001",
        content=text,
        task_type="retrieval_document"
    )
    return np.array(result["embedding"])

# --- OPENAI EMBEDDING SUPPORT ---
def get_openai_embedding(text: str) -> np.ndarray:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY environment variable not set.")
    openai.api_key = api_key
    response = openai.embeddings.create(
        input=text,
        model=OPENAI_EMBEDDING_MODEL
    )
    return np.array(response.data[0].embedding)

# --- MAIN PIPELINE ---
all_embeddings = []
all_metadata = []

for folder in INPUT_FOLDERS:
    for md_file in tqdm(glob.glob(os.path.join(folder, "*.md"))):
        with open(md_file, "r", encoding="utf-8") as f:
            text = f.read()
        chunks = chunk_text(text, CHUNK_SIZE, CHUNK_OVERLAP)
        for idx, chunk in enumerate(chunks):
            try:
                emb = get_openai_embedding(chunk)
            except Exception as e:
                print(f"Error embedding {md_file} chunk {idx}: {e}")
                continue
            all_embeddings.append(emb)
            all_metadata.append({
                "file": md_file,
                "chunk_index": idx,
                "text": chunk
            })

# Save embeddings and metadata
if all_embeddings:
    embeddings_np = np.vstack(all_embeddings)
    np.save("openai_embeddings.npy", embeddings_np)
    with open("openai_embeddings_metadata.json", "w", encoding="utf-8") as f:
        json.dump(all_metadata, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(all_embeddings)} embeddings and metadata.")
else:
    print("No embeddings were generated.")
