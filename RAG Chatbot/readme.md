
# Production-Grade RAG Chatbot with Reliability, Hybrid Retrieval & MLOps

This project is a **production-oriented Retrieval-Augmented Generation (RAG) system** designed to go beyond basic vector search and address real-world issues such as **hallucinations, retrieval precision, and system reliability**.

The system combines **hybrid retrieval (dense + sparse)**, **hallucination detection**, and **MLOps best practices** to deliver grounded, explainable, and maintainable LLM-based responses.

---

## Key Features

### Hybrid Retrieval (Dense + Sparse)

* Uses **FAISS-based dense vector search** for semantic understanding
* Uses **BM25 sparse keyword search** for exact term matching
* Combines both using weighted score fusion to improve factual precision
* Especially useful for **legal, medical, and technical documents** where exact terms matter

### Hallucination Detection Layer

* Evaluates whether generated answers are grounded in retrieved context
* Uses embedding similarity to measure answer–context alignment
* Assigns hallucination / coverage scores for every response

### Evaluation & Experiment Tracking

* Logs retrieval and generation metrics using **MLflow**
* Tracks hallucination scores, coverage scores, and query performance
* Enables comparison between different retrieval strategies

### Production-Ready API

* Built using **FastAPI**
* Clean REST endpoints for querying the RAG system
* Designed for easy integration with frontend or downstream services

### MLOps & Reliability

* Dockerized for consistent deployments
* CI/CD pipelines with automated checks
* Unit tests and guardrails to prevent unreliable deployments

---

## Why This Project Exists

Basic RAG systems rely only on vector similarity, which often fails when:

* Queries contain **exact identifiers** (IPC sections, error codes, medicine dosages)
* Precision matters more than semantic similarity
* Domain-specific keywords must not be missed

This project addresses those gaps by combining **semantic recall** with **keyword precision**, while also measuring and monitoring **LLM reliability** instead of assuming correctness.

---

## System Architecture (High-Level)

1. User submits a query
2. Query is sent to:

   * Dense retriever (FAISS)
   * Sparse retriever (BM25)
3. Results are merged using hybrid scoring
4. Top-ranked context is passed to the LLM
5. Generated answer is evaluated for grounding
6. Metrics are logged and returned with the response

---

## Project Structure

```
advanced-rag/
├── app/                # FastAPI application
├── retrieval/          # Dense, sparse, and hybrid retrievers
├── notebooks/          # Experiments and retrieval testing
├── data/               # Sample documents / embeddings
├── tests/              # Unit tests
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## Tech Stack

* **Python**
* **FastAPI**
* **FAISS**
* **BM25 (rank-bm25)**
* **Transformers / Sentence-Transformers**
* **MLflow**
* **Docker**
* **GitHub Actions (CI/CD)**

---

## Example Use Cases

* Legal document Q&A (IPC sections, clauses)
* Medical knowledge retrieval (drug names, dosages)
* Technical manuals and error code lookups
* Internal enterprise knowledge bases

---

## Future Enhancements

* Cross-encoder re-ranking for improved relevance
* Agentic workflows for self-corrective RAG
* LLM-as-a-judge based evaluation
* High-throughput inference with optimized serving

---

##  Author

**Ben Jose**
AI Engineer focused on building reliable, production-grade LLM systems
🔗 GitHub: [https://github.com/BENJOSE51](https://github.com/BENJOSE51)
🔗 LinkedIn: [https://linkedin.com/in/ben-jose-aa9537190](https://linkedin.com/in/ben-jose-aa9537190)

---
