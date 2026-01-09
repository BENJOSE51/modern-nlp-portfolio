# Notebooks – Retrieval Testing & Validation

This folder contains **exploratory and validation notebooks** used to test and reason about retrieval behavior before integrating logic into the production pipeline.

The notebooks are intentionally isolated from the main application code to support **safe experimentation and debugging**.

---

## Purpose of These Notebooks

The notebooks in this folder are used to:
- Validate retrieval strategies (dense, sparse, hybrid)
- Compare ranking behavior across methods
- Inspect failure cases and edge scenarios
- Build intuition about retrieval trade-offs

They are not intended for deployment.

---

## `test_retrieval.ipynb`

This notebook is used to **manually test and compare retrieval outputs**.

### What it does:
- Loads sample documents
- Executes dense retrieval (FAISS)
- Executes sparse retrieval (BM25)
- Executes hybrid retrieval
- Compares results for the same query

### Why it exists:
Retrieval systems often *appear* to work until tested with:
- Exact identifiers (codes, numbers)
- Domain-specific terminology
- Ambiguous queries

This notebook makes retrieval behavior **explicit and observable**.

---

## Design Rationale

Notebooks are used here because they:
- Allow rapid iteration
- Enable visual inspection of ranking results
- Make it easier to reason about failure modes
- Support hypothesis-driven system design

Once behavior is validated, logic is **refactored into modular Python files** under the `retrieval/` folder.

---


