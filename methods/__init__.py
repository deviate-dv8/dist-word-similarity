from methods.bpemb_method import bpemb_word_similarity
from methods.gensim_glove_method import glove_similarity
from methods.wordnet_method import wordnet_similarity
from methods.jellyfish_method import (
    jellyfish_jaro_similarity,
    jellyfish_levenshtein_similarity,
    jellyfish_hamming_similarity,
)
from methods.rapidfuzz_method import (
    jaro_winkler_similarity,
    token_set_similarity,
    partial_ratio_similarity,
    token_sort_similarity,
)
from methods.set_method import (
    jaccard_similarity,
    overlap_coefficient_similarity,
    dice_similarity,
)

all_methods = [
    bpemb_word_similarity,
    glove_similarity,
    wordnet_similarity,
    jaro_winkler_similarity,
    token_set_similarity,
    partial_ratio_similarity,
    token_sort_similarity,
    jellyfish_jaro_similarity,
    jellyfish_levenshtein_similarity,
    jellyfish_hamming_similarity,
    jaccard_similarity,
    overlap_coefficient_similarity,
    dice_similarity,
]
