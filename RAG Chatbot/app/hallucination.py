import numpy as np
from typing import List, Dict
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

_embed_model = None


def get_embedding_model():
    global _embed_model
    if _embed_model is None:
        _embed_model = SentenceTransformer(EMBEDDING_MODEL_NAME)
    return _embed_model


def split_sentences(text: str) -> List[str]:
    return [s.strip() for s in text.split(".") if len(s.strip()) > 10]


def evaluate_hallucination(
    answer: str,
    context_chunks: List[str],
    similarity_threshold: float = 0.6,
    hallucination_threshold: float = 0.45,
) -> Dict[str, float]:

    # Edge case: no context or empty answer
    if not answer or not context_chunks:
        return {
            "coverage_score": 0.0,
            "unsupported_ratio": 1.0,
            "hallucination_score": 1.0,
            "flag": "HALLUCINATION",
        }

    model = get_embedding_model()
    answer_sentences = split_sentences(answer)

    # Edge case: very short answer
    if not answer_sentences:
        return {
            "coverage_score": 0.0,
            "unsupported_ratio": 1.0,
            "hallucination_score": 1.0,
            "flag": "HALLUCINATION",
        }

    # Encode once per request
    answer_embeddings = model.encode(answer_sentences)
    context_embeddings = model.encode(context_chunks)

    # Similarity matrix: (answer_sentences × context_chunks)
    similarity_matrix = cosine_similarity(
        answer_embeddings, context_embeddings
    )

    # Best supporting chunk per sentence
    max_similarities = similarity_matrix.max(axis=1)

    coverage_score = float(np.mean(max_similarities))

    unsupported_count = np.sum(
        max_similarities < similarity_threshold
    )
    unsupported_ratio = float(
        unsupported_count / len(max_similarities)
    )

    hallucination_score = (
        (1 - coverage_score) * 0.6 +
        unsupported_ratio * 0.4
    )

    flag = (
        "HALLUCINATION"
        if hallucination_score > hallucination_threshold
        else "OK"
    )

    return {
        "coverage_score": round(coverage_score, 3),
        "unsupported_ratio": round(unsupported_ratio, 3),
        "hallucination_score": round(hallucination_score, 3),
        "flag": flag,
    }
