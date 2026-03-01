def jaccard_similarity(text1: str, text2: str) -> float:
    set1 = set(text1.lower().split())
    set2 = set(text2.lower().split())
    intersection = set1 & set2
    union = set1 | set2
    if not union:
        return 0.0
    return float(len(intersection) / len(union))


def overlap_coefficient_similarity(text1: str, text2: str) -> float:
    set1 = set(text1.lower().split())
    set2 = set(text2.lower().split())
    intersection = set1 & set2
    smaller = min(len(set1), len(set2))
    if smaller == 0:
        return 0.0
    return float(len(intersection) / smaller)


def dice_similarity(text1: str, text2: str) -> float:
    set1 = set(text1.lower().split())
    set2 = set(text2.lower().split())
    intersection = set1 & set2
    total = len(set1) + len(set2)
    if total == 0:
        return 0.0
    return float(2 * len(intersection) / total)
