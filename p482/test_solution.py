from unittest import TestCase

from p482.Solution import Solution


class TestSolution(TestCase):
    def test_licenseKeyFormatting(self):
        sol = Solution()
        self.assertEqual("", sol.licenseKeyFormatting("", 2))
        self.assertEqual("5F3Z-2E9W", sol.licenseKeyFormatting("5F3Z-2e-9-w", 4))
        self.assertEqual("2-5G-3J", sol.licenseKeyFormatting("2-5g-3-J", 2))
