# 🔍 Semantic Search Engine — Incremental Indexing with FAISS & HNSW

This project demonstrates how to build a **Semantic Search Engine** capable of retrieving documents **by meaning instead of keywords**, using **Transformer-based embeddings** and **vector similarity search** with **FAISS / HNSW**.

It features an **incremental indexing mechanism** that processes text data in batches, making it **memory-efficient** and suitable for environments like **Google Colab** or low-resource systems.

---

## 🧠 Project Overview

Traditional keyword search often fails when query wording differs from document phrasing.  
This project implements a **semantic retrieval system** that understands the *context* of queries — similar to how modern **RAG (Retrieval-Augmented Generation)** systems work.

For example:
> Searching “vector similarity library” correctly retrieves documents about **FAISS** and **semantic search**, even if those exact words don’t appear.

---

## 💼 Business Context

Modern enterprises accumulate millions of text documents — manuals, FAQs, reports, legal files — that are difficult to search with traditional methods.  
Semantic Search provides meaningful retrieval across:

- 🧾 **Knowledge bases** (internal company docs)  
- 💬 **Chatbots** (context-aware question answering)  
- 📚 **Research & academic archives**  
- ⚙️ **RAG pipelines** for LLM-based systems  

This project replicates the **retrieval backbone** of such AI-powered systems.

---

## ⚙️ Key Features

| Feature | Description |
|----------|--------------|
| 🧠 **Transformer Embeddings** | Uses SentenceTransformer (`all-MiniLM-L6-v2`) for text vectorization |
| ⚡ **Incremental Indexing** | Embeddings added to FAISS/HNSW in small batches to prevent OOM |
| 🧮 **Vector Search** | Cosine similarity–based retrieval for semantic relevance |
| 🧰 **Memory-Efficient** | Works efficiently on Colab or low-RAM setups |
| 💾 **Index Persistence** | Saves FAISS/HNSW index + metadata for future reuse |
| 🔁 **Fallback Support** | Auto-fallback to `hnswlib` if FAISS not available |

---

## 🧩 Technical Stack

- **Language:** Python  
- **Libraries:** `sentence-transformers`, `faiss-cpu`, `hnswlib`, `numpy`, `pandas`, `scikit-learn`  
- **Environment:** Jupyter Notebook / Google Colab  

---
## 👨‍💻 Author & Project Summary

**Author:** Ben Jose  
**Project:** Semantic Search Engine — Incremental Indexing with FAISS / HNSW  
**Domain:** Natural Language Processing (NLP), Information Retrieval  

This project was developed as part of a modern **AI/NLP portfolio** to demonstrate expertise in **semantic understanding, vector search, and retrieval engineering** — the same technologies behind **RAG (Retrieval-Augmented Generation)** systems and intelligent enterprise search solutions.

### ⚙️ **Manual Setup**
```bash
# Clone this repository
git clone https://github.com/yourusername/SemanticSearchEngine.git
cd SemanticSearchEngine

# Install dependencies
pip install -r requirements.txt

# Run notebook
jupyter notebook Semantic_Search_Engine_FAISS_Enhanced.ipynb
---


