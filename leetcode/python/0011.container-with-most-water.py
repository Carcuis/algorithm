import unittest


# @leet start
class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
# @leet end


class Test(unittest.TestCase):
    calc = Solution().maxArea

    def test_1(self):
        self.assertEqual(self.calc([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_2(self):
        self.assertEqual(self.calc([1, 1]), 1)

    def test_3(self):
        self.assertEqual(self.calc([4, 3, 2, 1, 4]), 16)


if __name__ == "__main__":
    unittest.main()
