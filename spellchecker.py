__author__ = "Just_kiy"


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.children = {}
        self.word = None


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
        node.word = word


class Spellchecker(object):
    def __init__(self):
        self.dict = Trie()

    def __contains__(self, word):
        return word in self.dict

    def load_words(self, word_list):
        """
        Append words from given variable
        :param word_list: list of words
        """
        try:
            for word in word_list:
                self.dict.add(word)
        except Exception as e:
            print("Error while adding words to dictionary, message: {msg}".format(msg=e))

    def check_word(self, word: str):
        """
        Takes word and checks if this word is in dictionary of known words
        :param word: word to check in words dictionary
        :return: Bool: is given word in dictionary or not, True if word in dict, False otherwise
        """

        if word in self.dict:
            return True
        else:
            return False

    def check_list(self, words: list):
        """
        Takes list of words and return unknown
        :param words: words to check if they are in dictionary of known words
        :return: result: list of unknown words due to dictionary
        """
        _result = []
        for word in words:
            if not self.check_word(word):
                _result.append(word)
        return _result

    def suggest_corrections_by_word(self, word: [str], levenshtein_distance: int=1) -> [str]:
        """
        Takes the word and find all suggestions that are nearer or the same to the original according to
        the Levenshtein distance.
        :param word:
        :param levenshtein_distance:
        :return: List[str]: words that are similar according to the given Levenshtein distance
        """

        def __recursion(node, letter, previous_row):
            """
            Inner recursive function to build Levenshtein distance table while going deeper into Trie
            :param node: current Trie node
            :param letter: letter that we are looking for in this node
            :param previous_row: row from Levenshtein distance table
            :return: This function does not return anything by itself yet it is working with "results"
            from outer suggest_corrections_by_word method. TODO: maybe change this as it is "best practice"
            """
            columns = len(word) + 1
            current_row = [previous_row[0] + 1]

            for column in range(1, columns):

                insert_cost = current_row[column - 1] + 1
                delete_cost = previous_row[column] + 1

                if word[column - 1] != letter:
                    replace_cost = previous_row[column - 1] + 1
                else:
                    replace_cost = previous_row[column - 1]

                current_row.append(min(insert_cost, delete_cost, replace_cost))

            # If current node represent a word and the way was less or equal the distance, then this is good result
            if current_row[-1] <= levenshtein_distance and (not (node.word is None)):
                results.append(node.word)

            # If there are still ways to go deeper - try them
            if min(current_row) <= levenshtein_distance:
                for letter in node.children:
                    __recursion(node.children[letter], letter, current_row)

            # __recursion END

        # Creating first row of the table
        current_row = range(len(word) + 1)

        results = []

        # Recursively trying to get similar words starting from all first letters in the dict
        for child in self.dict.node.children:
            __recursion(self.dict.node.children[child], child, current_row)

        return results

    def suggest_corrections_by_list(self, words: [str], levenshtein_distance: int=1) -> {str: [str]}:
        """
        Wrapper around suggest_correction_by_word. Takes list of words and Levenshtein distance to find words
        that differ from given less or equal from that distance.
        :param words: list of words that you want to find similar
        :param levenshtein_distance: a measure of the difference between two words
        :return: Dictionary {str: [str] - found suggestions] }
        """
        results = {}
        for word in words:
            result = self.suggest_corrections_by_word(word, levenshtein_distance)
            if len(result) > 0:
                results[word] = result
        return results


if __name__ == "__main__":
    pass
