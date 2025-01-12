import unittest


# @leet start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        if x < 10:
            return True

        x_rev = 0
        while x > x_rev:
            x, r = divmod(x, 10)
            x_rev = x_rev * 10 + r

        return x == x_rev or x == x_rev // 10
# @leet end


class Test(unittest.TestCase):
    check = Solution().isPalindrome

    def test_1(self):
        self.assertEqual(self.check(121), True)

    def test_2(self):
        self.assertEqual(self.check(-121), False)

    def test_3(self):
        self.assertEqual(self.check(10), False)

    def test_4(self):
        self.assertEqual(self.check(0), True)

    def test_5(self):
        self.assertEqual(self.check(-1), False)

    def test_6(self):
        self.assertEqual(self.check(11), True)


if __name__ == '__main__':
    unittest.main()
