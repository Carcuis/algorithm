import unittest


# @leet start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], index]
            seen[num] = index

        return []
# @leet end


class Test(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_2(self):
        self.assertEqual(self.solution.twoSum([3, 2, 4], 6), [1, 2])

    def test_3(self):
        self.assertEqual(self.solution.twoSum([3, 3], 6), [0, 1])


if __name__ == '__main__':
    unittest.main()

