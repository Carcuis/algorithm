import unittest


# @leet start
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        if not prefix:
            return ""
        for s in strs[1:]:
            if not s or not prefix:
                return ""
            while prefix and not s.startswith(prefix):
                prefix = prefix[:-1]
        return prefix
# @leet end


class Test(unittest.TestCase):
    get = Solution().longestCommonPrefix

    def test_1(self):
        self.assertEqual(self.get(["flower", "flow", "flight"]), "fl")

    def test_2(self):
        self.assertEqual(self.get(["dog", "racecar", "car"]), "")

    def test_3(self):
        self.assertEqual(self.get(["", ""]), "")


if __name__ == "__main__":
    unittest.main()
