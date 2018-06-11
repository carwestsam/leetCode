from unittest import TestCase

from p126.Solution import Solution


class TestSolution(TestCase):
	def test_should_not_give_answer(self):
		sol = Solution()
		self.assertEqual(sol.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), [])

	def test_should_give_one_step_answer(self):
		sol = Solution()
		self.assertEqual(sol.findLadders("hi", "bi", ["bi"]), [["hi", "bi"]])


	def test_should_give_two_step_answer(self):
		sol = Solution()
		self.assertEqual(sol.findLadders("hi", "lo", ["li", "lo"]), [["hi", "li", "lo"]])

	def test_should_find_example_case(self):
		sol = Solution()
		self.assertEqual(sol.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
						 [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]])

	def test_should_pass_case(self):
		sol = Solution()
		self.assertEqual(sol.findLadders("red", "tax", ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]),
						 [["red", "ted", "tad", "tax"], ["red", "ted", "tex", "tax"], ["red", "rex", "tex", "tax"]])

	def test_should_pass_case_2(self):
		sol = Solution()
		self.assertEqual(sol.findLadders("hot", "dog", ["hot", "dog"]),[])

	def test_should_pass_case_3(self):
		sol = Solution()
		self.assertEqual(sol.findLadders("talk", "tail", ["talk","tons","fall","tail","gale","hall","negs"]),[])
