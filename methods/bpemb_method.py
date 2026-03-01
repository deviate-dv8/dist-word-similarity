from bpemb import BPEmb
import numpy as np

bpemb = BPEmb(lang="en", dim=100)

res = bpemb.encode("Hello world")


def bpemb_word_similarity(word1, word2):
    vec1 = bpemb.embed(word1).mean(axis=0).squeeze()
    vec2 = bpemb.embed(word2).mean(axis=0).squeeze()
    similarity = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
    return similarity
