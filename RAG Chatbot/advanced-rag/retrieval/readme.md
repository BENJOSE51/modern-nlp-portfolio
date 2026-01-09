# Retrieval Layer (Dense, Sparse & Hybrid)

This folder contains the **core retrieval logic** used by the RAG system.

Retrieval quality is the most critical component of any RAG pipeline.  
This module is intentionally designed to be **modular, testable, and extensible**, allowing different retrieval strategies to be developed, evaluated, and composed without affecting the application layer.

---

## Purpose of the Retrieval Layer

The retrieval layer is responsible for:
- Fetching the most relevant context for a given user query
- Balancing semantic understanding with factual precision
- Exposing a clean interface for downstream generation logic

This separation allows retrieval strategies to evolve independently from the rest of the system.

---

## Modules in This Folder

### `dense.py` — Dense Vector Retrieval
Implements **semantic retrieval** using embeddings and FAISS.

- Converts documents into dense embeddings
- Uses cosine similarity (inner product on normalized vectors)
- Optimized for semantic recall and paraphrase understanding

**Strengths**
- Captures intent and meaning
- Works well for conversational and open-ended queries

**Limitations**
- May miss exact terms, codes, or identifiers

---

### `sparse.py` — Sparse Keyword Retrieval (BM25)
Implements **keyword-based retrieval** using BM25.

- Uses term frequency–inverse document frequency (TF-IDF–based scoring)
- Matches exact tokens from the query
- Does not rely on embeddings

**Strengths**
- Excellent for exact matches (IDs, codes, numbers)
- Deterministic and interpretable

**Limitations**
- Does not understand semantic similarity

---

### `hybrid.py` — Hybrid Retrieval
Combines dense and sparse retrieval into a **single retrieval strategy**.

- Executes both dense and sparse retrieval
- Normalizes and fuses scores using weighted combination
- Balances semantic recall with keyword precision

Hybrid retrieval is especially important for **legal, medical, and technical documents**, where both meaning and exact terminology matter.

---

## Design Philosophy

- **Separation of concerns**  
  Each retrieval strategy is implemented independently.

- **Composable architecture**  
  Dense and sparse retrievers can be reused, swapped, or reweighted.

- **Production-first thinking**  
  Retrieval logic is written as reusable modules, not notebook code.

---

##  Typical Flow

1. User query enters the system
2. Dense retriever captures semantic similarity
3. Sparse retriever captures exact keyword matches
4. Hybrid retriever fuses both signals
5. Top-ranked context is returned to the generation layer

---

## Extensibility

This folder is designed to support:
- Cross-encoder re-ranking
- Query rewriting
- Domain-specific weighting strategies
- Graph-based retrieval augmentation

New retrieval components can be added without modifying existing ones.

---

This folder exists to ensure **retrieval is treated as a first-class system component**, not an afterthought.
