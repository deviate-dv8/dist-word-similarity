from rapidfuzz.distance import JaroWinkler
from rapidfuzz import fuzz


def jaro_winkler_similarity(text1: str, text2: str) -> float:
    score: float = JaroWinkler.normalized_similarity(text1, text2)
    return score


def token_set_similarity(text1: str, text2: str) -> float:
    score: float = fuzz.token_set_ratio(text1, text2)
    return score / 100.0


def partial_ratio_similarity(text1: str, text2: str) -> float:
    score: float = fuzz.partial_ratio(text1, text2)
    return score / 100.0


def token_sort_similarity(text1: str, text2: str) -> float:
    score: float = fuzz.token_sort_ratio(text1, text2)
    return score / 100.0
