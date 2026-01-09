class HybridRetriever:
    def __init__(self, dense, sparse, alpha=0.6):
        self.dense = dense
        self.sparse = sparse
        self.alpha = alpha

    def search(self, query, k=5):
        dense_results = self.dense.search(query, k)
        sparse_results = self.sparse.search(query, k)

        combined = {}

        for r in dense_results:
            combined[r["text"]] = self.alpha * r["score"]

        for r in sparse_results:
            combined[r["text"]] = combined.get(
                r["text"], 0
            ) + (1 - self.alpha) * r["score"]

        ranked = sorted(
            combined.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return [
            {"text": text, "score": score}
            for text, score in ranked[:k]
        ]
