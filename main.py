__author__ = "Just_kiy"


WORDS = ("home", "kitten", "mother", "father", "son", "sin", "sheep", "ship")


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.children = {}
        self.is_leaf = False


class Trie(object):
    def __init__(self):
        self.node = Node()

    def __contains__(self, word):
        node = self.node
        for letter in word:
            if letter not in node.children:
                return False
            else:
                node = node.children[letter]
            return True

    def add(self, word):
        node = self.node
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                new_node = Node(letter)
                node.children[letter] = new_node
                node = new_node
            node.is_leaf = True

    def search(self, word):
        return self.__contains__(word)


class Spellchecker(object):
    def __init__(self):
        pass

    def check(self, word):
        pass


if __name__ == "__main__":
    checker = Spellchecker
    while True:
        user_input = input("Write any word: ")
        result = checker.check(word=user_input)
        if result:
            print("The word is correct")
        else:
            print("Did you mean %s", result)
