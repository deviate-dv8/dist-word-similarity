# methods/jellyfish_method.py
import jellyfish


def jellyfish_jaro_similarity(text1: str, text2: str) -> float:
    score: float = jellyfish.jaro_winkler_similarity(text1, text2)
    return score


def jellyfish_levenshtein_similarity(text1: str, text2: str) -> float:
    dist: int = jellyfish.levenshtein_distance(text1, text2)
    max_len = max(len(text1), len(text2))
    if max_len == 0:
        return 1.0
    return 1.0 - (dist / max_len)


def jellyfish_hamming_similarity(text1: str, text2: str) -> float:
    max_len = max(len(text1), len(text2))
    if max_len == 0:
        return 1.0
    t1 = text1.ljust(max_len)
    t2 = text2.ljust(max_len)
    dist: int = jellyfish.hamming_distance(t1, t2)
    return 1.0 - (dist / max_len)
