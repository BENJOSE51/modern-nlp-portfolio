import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

class DenseRetriever:
    def __init__(self, documents):
        self.documents = documents
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        self.embeddings = self.model.encode(
            documents,
            normalize_embeddings=True
        )

        dim = self.embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dim)
        self.index.add(self.embeddings)

    def search(self, query, k=5):
        query_emb = self.model.encode(
            [query],
            normalize_embeddings=True
        )

        scores, indices = self.index.search(query_emb, k)

        return [
            {
                "text": self.documents[i],
                "score": float(scores[0][idx])
            }
            for idx, i in enumerate(indices[0])
        ]
