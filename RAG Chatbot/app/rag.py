import os
import faiss
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# ---------- PATHS (Docker-safe) ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "notebooks")

FAISS_PATH = os.path.join(DATA_DIR, "faiss.index")
CHUNKS_PATH = os.path.join(DATA_DIR, "chunks.txt")

# ---------- LOAD DATA ----------
embed_model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index(FAISS_PATH)

with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
    chunks = [c.strip() for c in f.readlines() if c.strip()]

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

# ---------- RAG CORE ----------
def retrieve(query, k=3):
    query_embedding = embed_model.encode([query])
    distances, indices = index.search(query_embedding, k)

    results = []
    for idx in indices[0]:
        results.append(chunks[idx])

    return results


def answer_question(query, k=3):
    context_chunks = retrieve(query, k)

    prompt = f"""
Use the context below to answer the question.
If the answer is not present, say "I don't know".

Context:
{chr(10).join(context_chunks)}

Question:
{query}

Answer:
""".strip()

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(
        **inputs,
        max_new_tokens=200,
        temperature=0
    )

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer, context_chunks
