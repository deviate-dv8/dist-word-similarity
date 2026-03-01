import os

os.environ["CUDA_VISIBLE_DEVICES"] = ""
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

from tester import MethodTester
from methods import all_methods


def print_results(results: dict):
    print("\n" + "=" * 75)
    print(f"{'BENCHMARK RESULTS':^75}")
    print("=" * 75)

    for name, data in results.items():
        print(f"\n  Rank #{data['rank_overall']:.2f} - {name}")
        print(f"  {'-' * 55}")
        print(f"    {'Time':<30} {data['time']:.6f}s         (#{data['rank_time']})")
        print(
            f"    {'Memory Current':<30} {data['mem_current_mb']:.4f}MB        (#{data['rank_mem']})"
        )
        print(
            f"    {'Memory Peak':<30} {data['mem_peak_mb']:.4f}MB        (#{data['rank_mem']})"
        )
        print(
            f"    {'Word Accuracy':<30} {data['similarity_accuracy_word']:.4f}           (#{data['rank_word']})"
        )
        print(
            f"    {'Sentence Accuracy':<30} {data['similarity_accuracy_sentence']:.4f}           (#{data['rank_sentence']})"
        )

    print("\n" + "=" * 75)
    print(f"{'RANKING SUMMARY':^75}")
    print("=" * 75)
    print(
        f"  {'#':<4} {'Method':<35} {'Time':>8} {'MemPeak':>9} {'Word':>8} {'Sentence':>10}"
    )
    print(f"  {'-' * 72}")
    for i, (name, data) in enumerate(results.items(), start=1):
        print(
            f"  {i:<4}"
            f" {name:<35}"
            f" {data['time']:>7.4f}s"
            f" {data['mem_peak_mb']:>8.4f}MB"
            f" {data['similarity_accuracy_word']:>8.4f}"
            f" {data['similarity_accuracy_sentence']:>10.4f}"
        )
    print("=" * 75 + "\n")

    best_time = min(results, key=lambda n: results[n]["time"])
    best_mem = min(results, key=lambda n: results[n]["mem_peak_mb"])
    best_word = max(results, key=lambda n: results[n]["similarity_accuracy_word"])
    best_sentence = max(
        results, key=lambda n: results[n]["similarity_accuracy_sentence"]
    )
    best_overall = list(results.keys())[0]

    print("  WINNERS")
    print(f"  {'-' * 45}")
    print(f"  Fastest          : {best_time}")
    print(f"  Least Memory     : {best_mem}")
    print(f"  Best Word        : {best_word}")
    print(f"  Best Sentence    : {best_sentence}")
    print(f"  Best Overall     : {best_overall}")
    print("=" * 75 + "\n")


def main():
    tester = MethodTester(all_methods)
    results = tester.run_tests()
    print_results(results)


if __name__ == "__main__":
    main()
