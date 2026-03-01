import time


class MethodTester:
    def __init__(self, methods):
        self.methods = methods
        self.word_pairs = [
            ("cat", "dog"),
            ("king", "queen"),
            ("apple", "orange"),
            ("car", "bicycle"),
            ("house", "home"),
        ]

    def test_methods_time(self):
        results = {}
        for method in self.methods:
            start_time = time.time()
            for word1, word2 in self.word_pairs:
                method(word1, word2)
            end_time = time.time()
            results[method.__name__] = end_time - start_time
        return results

    def test_methods_similarity_word(self):
        results = {}
        for method in self.methods:
            similarities = []
            for word1, word2 in self.word_pairs:
                similarity = method(word1, word2)
                similarities.append(f"{word1} - {word2}: {similarity:.4f}")
            results[method.__name__] = similarities
        return results

    def run_tests(self):
        time_results = self.test_methods_time()
        similarity_results = self.test_methods_similarity_word()
        test_results = {
            "time_results": time_results,
            "similarity_results": similarity_results,
        }
        return test_results
