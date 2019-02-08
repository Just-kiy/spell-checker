__author__ = "Just_kiy"


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


class Spellchecker(object):
    def __init__(self):
        self.dict = Trie()

    def load_words(self, word_list):
        """
        Append words from given variable
        :param word_list: list of words
        :return:
        """
        try:
            for word in word_list:
                self.dict.add(word)
        except Exception as e:
            print("Error while adding words to dictionary, message: {msg}".format(msg=e))

    def check_word(self, word: str):
        """
        Takes word and checks if this word is in dictionary of known words
        :param String word: word to check in words dictionary
        :return: Boolean: is given word in dictionary or not
        """

        if word in self.dict:
            return True
        else:
            return False

    def check_list(self, words: list):
        """
        Takes list of words and return unknown
        :param List words: words to check if they are in dictionary of known words
        :return: List result: list of unknown words due to dictionary
        """
        _result = []
        for word in words:
            if not self.check_word(word):
                _result.append(word)
        return _result

    def suggest_corrections_by_word(self, word: str, levenshtein_distance=1):

        def __recursion(self, path, cur_dist, cur_step, cur_node):
            if cur_dist > levenshtein_distance:
                return
            if cur_node.node.is_leaf and abs(len(word)-len(path)) + cur_dist <= levenshtein_distance:
                return path
            return path

        return __recursion(path='', cur_dist=0, cur_step=0, cur_node=self.dict)

    def suggest_corrections_by_list(self, words: list, levenshtein_distance=1):
        _result = {}
        for word in words:
            _result[word] = self.suggest_corrections_by_word(word, levenshtein_distance)
        return _result


if __name__ == "__main__":
    pass
