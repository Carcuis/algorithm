import unittest


# @leet start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        negative = s[0] == "-"
        s = s[1:] if s[0] in "+-" else s

        num = 0
        digits = [str(i) for i in range(10)]
        for char in s:
            if char not in digits:
                break
            num = 10 * num + int(char)

        return max(-2147483648, -num) if negative else min(2147483647, num)
# @leet end


class Test(unittest.TestCase):
    myAtoi = Solution().myAtoi

    def test_1(self):
        self.assertEqual(self.myAtoi("42"), 42)

    def test_2(self):
        self.assertEqual(self.myAtoi("   -42"), -42)

    def test_3(self):
        self.assertEqual(self.myAtoi("1337c0d3"), 1337)

    def test_4(self):
        self.assertEqual(self.myAtoi("0-1"), 0)

    def test_5(self):
        self.assertEqual(self.myAtoi("words and 987"), 0)

    def test_6(self):
        self.assertEqual(self.myAtoi("-91283472332"), -2147483648)

    def test_7(self):
        self.assertEqual(self.myAtoi("91283472332"), 2147483647)

    def test_8(self):
        self.assertEqual(self.myAtoi(""), 0)

    def test_9(self):
        self.assertEqual(self.myAtoi(" "), 0)

    def test_10(self):
        self.assertEqual(self.myAtoi("+-12"), 0)


if __name__ == "__main__":
    unittest.main()
