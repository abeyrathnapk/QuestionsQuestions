from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import numpy as np
import json
import openai
import os
import base64
import re

app = FastAPI()

EMBEDDINGS_PATH = "openai_embeddings.npy"
METADATA_PATH = "openai_embeddings_metadata.json"

embeddings = np.load(EMBEDDINGS_PATH)
with open(METADATA_PATH, "r") as f:
    metadata = json.load(f)

openai.api_key = os.getenv("OPENAI_API_KEY")

class AskRequest(BaseModel):
    question: str
    image: Optional[str] = None

@app.post("/api/")
async def ask_api(request: AskRequest):
    question = request.question
    image_b64 = request.image
    image_description = None
    image_bytes = None
    if image_b64:
        try:
            image_bytes = base64.b64decode(image_b64)
            response = openai.chat.completions.create(
                model="gpt-4-vision-preview",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that describes images in detail."},
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Describe this image in detail."},
                            {"type": "image_url", "image_url": {"data": image_bytes, "detail": "high"}}
                        ]
                    }
                ],
                max_tokens=300
            )
            image_description = response.choices[0].message.content.strip()
        except Exception as e:
            image_description = f"Error processing image: {e}"

    full_query = question
    if image_description:
        full_query += "\n" + image_description

    try:
        embedding_response = openai.embeddings.create(
            input=full_query,
            model="text-embedding-3-large"
        )
        query_embedding = np.array(embedding_response.data[0].embedding)
    except Exception as e:
        return JSONResponse(content={"error": f"Embedding failed: {e}"}, status_code=500)

    def cosine_similarity(a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    similarities = [cosine_similarity(query_embedding, emb) for emb in embeddings]
    top_indices = np.argsort(similarities)[-3:][::-1]
    top_contexts = [metadata[i]["text"] for i in top_indices]
    top_metadatas = [metadata[i] for i in top_indices]

    link_pattern = re.compile(r"https?://\S+")
    allowed_domain = "discourse.onlinedegree.iitm.ac.in"
    links = []
    for meta in top_metadatas:
        text = meta.get("text", "")
        urls = link_pattern.findall(text)
        for url in urls:
            url = url.rstrip(').,;\'"')
            if allowed_domain not in url:
                continue
            idx = text.find(url)
            snippet = text[max(0, idx-60):idx+len(url)+60]
            try:
                summary_prompt = f"Summarize the following context into a short, clear sentence for a link preview.\n\nContext: {snippet}\nURL: {url}"
                summary_response = openai.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that writes concise, natural link previews."},
                        {"role": "user", "content": summary_prompt}
                    ],
                    max_tokens=50
                )
                link_text = summary_response.choices[0].message.content.strip()
            except Exception as e:
                link_text = "Relevant link."
            links.append({"url": url, "text": link_text})
    links = links[:2]

    try:
        answer_prompt = (
            "Answer the following question using the provided context. "
            "If an image description is given, use it as well. "
            "Respond in a single, direct, and natural sentence, using code formatting and quotations where appropriate. "
            "Do not add unnecessary explanations.\n\n"
            f"Question: {question}\n"
            f"Image Description: {image_description or ''}\n"
            f"Context: {' '.join(top_contexts)}"
        )
        answer_response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for a RAG system."},
                {"role": "user", "content": answer_prompt}
            ],
            max_tokens=150
        )
        answer_text = answer_response.choices[0].message.content.strip()
    except Exception as e:
        answer_text = f"Error generating answer: {e}"

    answer = {
        "answer": answer_text,
        "links": links
    }
    return JSONResponse(content=answer)
