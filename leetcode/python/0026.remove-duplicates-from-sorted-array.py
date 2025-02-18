import unittest


# @leet start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        for n in nums:
            if n != nums[i]:
                i += 1
                nums[i] = n
        return i + 1
# @leet end


class Test(unittest.TestCase):
    remove = Solution().removeDuplicates

    def check(self, nums: list[int], expected_nums: list[int]):
        k = self.remove(nums)
        self.assertEqual(k, len(expected_nums))
        self.assertEqual(nums[:k], expected_nums)

    def test_1(self):
        nums = [1, 1, 2]
        self.check(nums, [1, 2])

    def test_2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        self.check(nums, [0, 1, 2, 3, 4])

    def test_3(self):
        nums = [-1, 0, 0, 0, 0, 3, 3]
        self.check(nums, [-1, 0, 3])


if __name__ == '__main__':
    unittest.main()
