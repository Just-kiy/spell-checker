__author__ = "Just_kiy"

from spellchecker import Spellchecker


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

    # while True:
    user_input = input("Write any word: ")
    result = checker.check_word(word=normalize(user_input))
    if result:
        print("The word is correct")
    else:
        print("No such word")
        # print("Did you mean {result}".format(result=result))
