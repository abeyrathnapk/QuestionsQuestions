<<<<<<< HEAD
# QuestionsQuestions    
<p style="color: red;">Works good with relaxed assertions and gives logical relevant answers with human reading .</p>
=======
# RAG API with OpenAI Embeddings and Vision

This project provides a FastAPI-based API for answering questions using Retrieval-Augmented Generation (RAG) with OpenAI embeddings and vision capabilities. It supports both text and image-based queries.

## Features
- Accepts questions as text, with optional image input (base64-encoded).
- Uses OpenAI GPT-4o for both text and image understanding.
- Retrieves relevant context from your own markdown content using precomputed OpenAI embeddings.
- Returns answers and relevant links in a clean JSON format.

## Endpoints

### `POST /api/`
Request body (JSON):
```
{
  "question": "Your question here",
  "image": "<base64-encoded image string>" // optional
}
```

Response (JSON):
```
{
  "answer": "Direct, natural answer with code formatting and quotations as needed.",
  "links": [
    { "url": "https://discourse.onlinedegree.iitm.ac.in/...", "text": "Short, human-friendly summary." },
    ...
  ]
}
```

## Setup
1. Clone the repository.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and add your OpenAI API key:
   ```sh
   cp .env.example .env
   # Edit .env and set OPENAI_API_KEY
   ```
4. Ensure `openai_embeddings.npy` and `openai_embeddings_metadata.json` are present in the project root.

## Running Locally
Start the API server:
```sh
uvicorn rag_api:app --reload
```

## Example Request (with image)
Convert your image to base64 (macOS/Linux):
```sh
base64 samplephoto.webp | tr -d '\n'
```
Then send a request:
```sh
curl "http://127.0.0.1:8000/api/" \
  -H "Content-Type: application/json" \
  -d '{"question": "Should I use gpt-4o-mini which AI proxy supports, or gpt3.5 turbo?", "image": "<base64 string here>"}'
```

## Deployment
- Do **not** commit your real `.env` file or API keys.
- Set the `OPENAI_API_KEY` environment variable in your Railway (or other) deployment platform.

## Notes
- Only links from your own markdown content (e.g., `discourse.onlinedegree.iitm.ac.in`) are included in responses.
- Answers are concise, direct, and use code formatting/quotations as needed.

---

For questions or issues, open an issue on GitHub.
>>>>>>> 481369d (Initial commit)
