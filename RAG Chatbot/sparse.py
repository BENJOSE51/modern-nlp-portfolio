from rank_bm25 import BM25Okapi

class SparseRetriever:
    def __init__(self, documents):
        self.documents = documents
        tokenized = [doc.lower().split() for doc in documents]
        self.bm25 = BM25Okapi(tokenized)

    def search(self, query, k=5):
        tokenized_query = query.lower().split()
        scores = self.bm25.get_scores(tokenized_query)

        ranked = sorted(
            enumerate(scores),
            key=lambda x: x[1],
            reverse=True
        )[:k]

        return [
            {
                "text": self.documents[i],
                "score": float(score)
            }
            for i, score in ranked
        ]
