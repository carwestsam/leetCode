from unittest import TestCase

from p388.Solution import Solution


class TestSolution(TestCase):
    def test_lengthLongestPath(self):
        sol = Solution()
        self.assertEqual(len('dir/subdir2/subsubdir2/file2.ext'), sol.lengthLongestPath(
            "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
        self.assertEqual(len('dir/file.txt'), sol.lengthLongestPath("dir\n    file.txt"))
        self.assertEqual(len('dir/    file.txt'), sol.lengthLongestPath("dir\n        file.txt"))
        self.assertEqual(len('a/aaaa.txt'), sol.lengthLongestPath("a\n\tb\n\t\tc.txt\n\taaaa.txt"))
