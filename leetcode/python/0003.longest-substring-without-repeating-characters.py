import unittest


# @leet start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = -1
        max_length = 0
        char_index: dict[str, int] = {}

        for index, char in enumerate(s):
            if char in char_index and char_index[char] > start:
                start = char_index[char]
            char_index[char] = index
            max_length = max(index - start, max_length)

        return max_length
# @leet end


class Test(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_2(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)

    def test_3(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)

    def test_4(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring(""), 0)

    def test_5(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("dvdf"), 3)

    def test_6(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("au"), 2)

    def test_7(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("tmmzuxt"), 5)


if __name__ == '__main__':
    unittest.main()

