import unittest


# @leet start
class Solution:
    def reverse(self, x: int) -> int:
        if -10 < x < 10:
            return x

        sign = 1 if x > 0 else -1
        x, x_rev = abs(x), 0

        while x:
            x, mod = divmod(x, 10)
            x_rev = x_rev * 10 + mod

        x_rev *= sign

        return x_rev if -2147483648 <= x_rev <= 2147483647 else 0
# @leet end


class Test(unittest.TestCase):
    reverse = Solution().reverse

    def test_1(self):
        self.assertEqual(self.reverse(123), 321)

    def test_2(self):
        self.assertEqual(self.reverse(-123), -321)

    def test_3(self):
        self.assertEqual(self.reverse(120), 21)

    def test_4(self):
        self.assertEqual(self.reverse(0), 0)

    def test_5(self):
        self.assertEqual(self.reverse(1534236469), 0)


if __name__ == '__main__':
    unittest.main()
