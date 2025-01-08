import unittest


# @leet start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        len_s = len(s)

        def _expand(i1: int, i2: int) -> tuple[int, int, int]:
            while i1 >= 0 and i2 < len_s and s[i1] == s[i2]:
                i1 -= 1
                i2 += 1
            return i1 + 1, i2, i2 - i1

        start, end, max_len = 0, 0, 0
        for i in range(len_s):
            start1, end1, len1 = _expand(i, i)
            start2, end2, len2 = _expand(i, i + 1)
            if len1 > max_len or len2 > max_len:
                start, end, max_len = (start1, end1, len1) if len1 > len2 else (start2, end2, len2)

        return s[start:end]
# @leet end


class Test(unittest.TestCase):
    func = Solution().longestPalindrome

    def test_1(self):
        self.assertIn(self.func("babad"), ("bab", "aba"))

    def test_2(self):
        self.assertEqual(self.func("cbbd"), "bb")

    def test_3(self):
        self.assertEqual(self.func(""), "")

    def test_4(self):
        self.assertEqual(self.func("a"), "a")

    def test_5(self):
        self.assertIn(self.func("ac"), ("a", "c"))

    def test_6(self):
        self.assertEqual(self.func("bb"), "bb")

    def test_7(self):
        self.assertEqual(self.func("ccc"), "ccc")

    def test_8(self):
        self.assertEqual(self.func("aaaa"), "aaaa")

    def test_9(self):
        self.assertIn(self.func("abacdfgdcada"), ("aba", "ada"))

    def test_10(self):
        self.assertEqual(self.func("abacdfgdcabba"), "abba")


if __name__ == "__main__":
    unittest.main()

