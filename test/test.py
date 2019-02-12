import unittest, os
from spellchecker import Trie, Spellchecker
from main import normalize

TEST_DIR = os.path.dirname(__file__)


class TrieTestCase(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()
        self.words = ['one', 'two', 'three', 'four']
        self.testword = 'testword'

    def test_add_one_word(self):
        self.trie.add(self.words[0])
        self.assertTrue(self.words[0] in self.trie)
        self.assertFalse(self.testword in self.trie)

    def test_add_many_words(self):
        for word in self.words:
            self.trie.add(word)
            self.assertTrue(word in self.trie)
            self.assertFalse(self.testword in self.trie)

    def tearDown(self):
        self.trie = None


class SpellcheckerTestCase(unittest.TestCase):

    def setUp(self):
        # TODO: read all this words from files
        self.known = open(os.path.join(TEST_DIR, 'known_words.txt'))
        self.unknown = open(os.path.join(TEST_DIR, 'unknown_words.txt'))
        self.similar = open(os.path.join(TEST_DIR, 'similar_words.txt'))
        self.known_words = list(map(normalize, self.known.read().replace('\n', ' ').split(' ')))
        self.unknown_words = list(map(normalize, self.unknown.read().replace('\n', ' ').split(' ')))
        self.similar_words = list(map(normalize, self.similar.read().replace('\n', ' ').split(' ')))
        # self.known_words = ['one', 'two', 'three', 'four', 'mother', 'father']
        # self.unknown_words = ['qwe', 'test']
        self.mixed_words = self.known_words[:len(self.known_words) // 2] \
                           + self.unknown_words[len(self.unknown_words) // 2:]
        # self.similar_words = ['onn', 'twoo', 'feur', 'ffur', 'mather', 'fother', 'one']
        self.spellchecker = Spellchecker()
        self.spellchecker.load_words(self.known_words)

    def test_loadwords(self):
        for word in self.known_words:
            self.assertTrue(word in self.spellchecker)

    def test_check_word(self):
        for word in self.known_words:
            self.assertEqual((word in self.spellchecker), (self.spellchecker.check_word(word)))

    def test_check_list(self):
        self.assertEqual([], self.spellchecker.check_list(self.known_words))
        self.assertEqual(self.unknown_words, self.spellchecker.check_list(self.unknown_words))
        result_of_mixed = self.spellchecker.check_list(self.mixed_words)
        for word in result_of_mixed:
            self.assertTrue(word in self.unknown_words and word not in self.known_words)

    def test_suggest_corrections_by_word(self):
        for word in self.similar_words:
            suggestions = self.spellchecker.suggest_corrections_by_word(word)
            self.assertEqual(type(suggestions), type([]))
            self.assertGreater(len(suggestions), 0)
            for suggestion in suggestions:
                self.assertTrue(suggestion in self.known_words)

        for word in self.unknown_words:
            suggestions = self.spellchecker.suggest_corrections_by_word(word)
            self.assertEqual(type(suggestions), type([]))
            self.assertEqual(len(suggestions), 0)

    def test_suggest_corrections_by_list(self):
        suggestions = self.spellchecker.suggest_corrections_by_list(self.similar_words)
        self.assertEqual(type(suggestions), type({}))
        self.assertGreater(len(suggestions), 0)
        for typo, variants in suggestions.items():
            for variant in variants:
                self.assertTrue(variant in self.known_words)

        suggestions = self.spellchecker.suggest_corrections_by_list(self.unknown_words)
        self.assertEqual(type(suggestions), type({}))
        self.assertEqual(len(suggestions), 0)

    def tearDown(self):
        self.spellchecker = None
        self.known.close()
        self.unknown.close()
        self.similar.close()


if __name__ == "__main__":
    unittest.main()
