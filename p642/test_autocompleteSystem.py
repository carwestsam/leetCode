from unittest import TestCase

from p642.Solution import AutocompleteSystem


class TestAutocompleteSystem(TestCase):
    def test_input(self):
        sol = AutocompleteSystem(['hello', 'hella', 'help', 'hell'], [3, 3, 4, 5])

        # print(sol.trie.children['h'].children['e'].children['l'].children['l'].top3)

        self.assertEqual(['hell', 'help', 'hella'], sol.input('h'))
        self.assertEqual(['hell', 'help', 'hella'], sol.input('e'))
        self.assertEqual(['hell', 'help', 'hella'], sol.input('l'))
        self.assertEqual(['hell', 'hella', 'hello'], sol.input('l'))
        self.assertEqual(['hello'], sol.input('o'))
        self.assertEqual([], sol.input('#'))

        self.assertEqual(['hell', 'hello', 'help'], sol.input('h'))
        self.assertEqual(['hell', 'hello', 'help'], sol.input('e'))
        self.assertEqual(['hell', 'hello', 'help'], sol.input('l'))
        self.assertEqual(['hell', 'hello', 'hella'], sol.input('l'))
        self.assertEqual(['hello'], sol.input('o'))
        self.assertEqual([], sol.input('#'))

