import unittest
from math import inf


# @leet start
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m, n = len(nums1), len(nums2)

        if m > n:
            # Ensure nums2 is longer, prevent `nums2[j := half_total_len - i]` out of range
            return self.findMedianSortedArrays(nums2, nums1)

        left, right = 0, m    # left and right edge of initial search interval in nums1
        half_total_len = (m + n + 1) // 2    # equals to ceil((m + n) / 2)

        while left < right:
            # right of new dividor in nums1, `+1` to prevent infinite loop
            # `(right - left) // 2` will always be 0 if `right - left == 1`
            # in this case, `i` will never reach right edge of nums1
            # note that `i = (left + right + 1) // 2` is also OK
            i = left + (right - left + 1) // 2

            # right of new dividor in nums2
            j = half_total_len - i

            if nums1[i - 1] > nums2[j]:
                # next search interval: [left, i - 1], move dividor to left
                # `i-1` means left of current dividor in nums1
                right = i - 1
            else:
                # next search interval: [i, right], move dividor to right
                # `i` means right of current dividor in nums1
                left = i

        i = left
        j = half_total_len - i
        nums1_left_max = -inf if i == 0 else nums1[i - 1]
        nums1_right_min = inf if i == m else nums1[i]
        nums2_left_max = -inf if j == 0 else nums2[j - 1]
        nums2_right_min = inf if j == n else nums2[j]

        if (m + n) % 2 == 1:
            return max(nums1_left_max, nums2_left_max)
        else:
            return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
# @leet end


class Test(unittest.TestCase):
    find = Solution().findMedianSortedArrays

    def test_1(self):
        self.assertEqual(self.find([1, 3], [2]), 2.0)

    def test_2(self):
        self.assertEqual(self.find([1, 2], [3, 4]), 2.5)

    def test_3(self):
        self.assertEqual(self.find([0, 0], [0, 0]), 0.0)

    def test_4(self):
        self.assertEqual(self.find([], [1]), 1.0)

    def test_5(self):
        self.assertEqual(self.find([2], []), 2.0)

    def test_6(self):
        self.assertEqual(self.find([1, 3], [2, 7]), 2.5)

    def test_7(self):
        self.assertEqual(self.find([1, 2, 3], [4, 5, 6, 7, 8]), 4.5)

    def test_8(self):
        self.assertEqual(self.find([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]), 5.5)

    def test_9(self):
        self.assertEqual(self.find([1, 2, 3, 4, 5], [6, 7, 8, 9]), 5.0)

    def test_10(self):
        self.assertEqual(self.find([1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]), 6.0)


if __name__ == '__main__':
    unittest.main()

