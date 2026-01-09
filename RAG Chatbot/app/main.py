from fastapi import FastAPI
from schemas import QueryRequest, QueryResponse
from rag import answer_question
from hallucination import evaluate_hallucination    

app = FastAPI(title="Free Local RAG Chatbot")

@app.post("/ask", response_model=QueryResponse)
def ask(req: QueryRequest):
    answer, context = answer_question(req.question)

    # 👇 NEW: hallucination evaluation
    hallucination = evaluate_hallucination(
        answer=answer,
        context_chunks=context
    )

    return {
        "answer": answer,
        "context": context,
        "hallucination": hallucination
    }
