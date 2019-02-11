__author__ = "Just_kiy"

from spellchecker import Spellchecker
from pprint import pprint


def normalize(word: str):
    return word.lower().strip()


if __name__ == "__main__":
    checker = Spellchecker()

    # Loading words base from txt file
    words = []
    with open("test_text.txt") as f:
        for line in f:
            words += line.split(' ')
    words = list(map(normalize, words))
    checker.load_words(map(normalize, words))

    while True:
        user_input = input("Write any word: ")
        result = checker.suggest_corrections_by_word(word=normalize(user_input))
        # if not result.count():
        #     print("full")
        # else:
        #     print("empty")
        if len(result) > 0:
            if result[0] == user_input:
                print("The word is correct")
            else:
                print("Did you mean: ")
                for suggestion in result:
                    print(suggestion)
        else:
            print("No suggestions for this word")
