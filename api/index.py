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

    # Format contexts for clarity
    context_str = "\n\n".join([f"Context {i+1}: {ctx}" for i, ctx in enumerate(top_contexts)])
    # Chain-of-thought few-shot examples and instructions
    few_shot_examples = (
        "Examples:\n"
        "Q: The question asks to use gpt-3.5-turbo-0125 model but the ai-proxy provided by Anand sir only supports gpt-4o-mini. So should we just use gpt-4o-mini or use the OpenAI API for gpt3.5 turbo?\n"
        "A: Let's think step by step. The context says the AI Proxy only supports gpt-4o-mini. Therefore, you should use `gpt-4o-mini` with the provided AI Proxy. Do not use gpt-3.5-turbo-0125 unless the proxy supports it.\n\n"
        "Q: If a student scores 10/10 on GA4 as well as a bonus, how would it appear on the dashboard?\n"
        "A: Let's think step by step. The context says a bonus is added to the score. If you score 10/10 and receive a bonus, the dashboard will show '110'.\n\n"
        "Q: When is the TDS Sep 2025 end-term exam?\n"
        "A: Let's think step by step. The context does not provide a date for the exam. Therefore, I don't know based on the provided information.\n\n"
        "Q: I know Docker but have not used Podman before. Should I use Docker for this course?\n"
        "A: Let's think step by step. If you're already familiar with Docker, you can use it for this course, but Podman is recommended for better security and compatibility.\n\n"
    )
    answer_prompt = (
        "Answer the following question using the provided context(s). "
        "If an image description is given, use it as well. "
        "Think step by step and explain your reasoning before giving the final answer. "
        "If the answer is not present in the provided context(s), say 'I don't know based on the provided information.' "
        "If a relevant link is present in the context, include it in your answer. "
        "If the answer is a score or number, use the exact format as shown in the context. "
        "If the question is about which model to use, clarify the model name and why, based on the context. "
        "If the question is about exam dates or deadlines, only answer if the date is explicitly present in the context; otherwise, say you don't know. "
        "Do not add unnecessary explanations.\n\n"
        f"{few_shot_examples}"
        f"Question: {question}\n"
        f"Image Description: {image_description or ''}\n"
        f"Contexts:\n{context_str}"
    )
    print("[DEBUG] Chain-of-thought Answer prompt:")
    print(answer_prompt)
    try:
        answer_response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for a RAG system."},
                {"role": "user", "content": answer_prompt}
            ],
            max_tokens=200
        )
        answer_text = answer_response.choices[0].message.content.strip()
    except Exception as e:
        answer_text = f"Error generating answer: {e}"

    answer = {
        "answer": answer_text,
        "links": links
    }
    return JSONResponse(content=answer)
