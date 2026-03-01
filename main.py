from tester import MethodTester
from methods.bpemb_method import bpemb_word_similarity


def main():
    tester = MethodTester([bpemb_word_similarity])
    print(tester.run_tests())


if __name__ == "__main__":
    main()
