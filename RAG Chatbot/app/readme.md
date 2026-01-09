# Application Layer (FastAPI)

This folder contains the **production application layer** for the RAG system, implemented using **FastAPI**.

The `app/` module is responsible for:
- Handling user requests
- Orchestrating retrieval and generation
- Enforcing reliability and evaluation logic
- Exposing clean, documented APIs for external use

All experimental logic is intentionally excluded from this layer.

---

## Responsibilities of the App Layer

The application layer focuses on **system orchestration**, not experimentation.

Specifically, it:
1. Accepts user queries via HTTP endpoints
2. Invokes the retrieval pipeline (dense, sparse, or hybrid)
3. Passes retrieved context to the LLM
4. Applies hallucination and grounding checks
5. Returns structured, reliable responses
6. Logs metrics for monitoring and evaluation

---
