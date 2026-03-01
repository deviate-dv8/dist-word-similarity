import numpy as np
import nltk
from nltk.corpus import wordnet as wn

nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)


def wordnet_similarity(text1: str, text2: str) -> float:
    def best_score(w1: str, w2: str) -> float:
        s1 = wn.synsets(w1)
        s2 = wn.synsets(w2)
        if not s1 or not s2:
            return 0.0
        scores: list[float] = []
        for s in s1:
            for t in s2:
                if s is None or t is None:
                    continue
                score = s.path_similarity(t)
                if score is not None:
                    scores.append(float(score))
        return max(scores) if scores else 0.0

    tokens1 = text1.lower().split()
    tokens2 = text2.lower().split()
    pair_scores = [best_score(w1, w2) for w1 in tokens1 for w2 in tokens2]
    return float(np.mean(pair_scores)) if pair_scores else 0.0
