class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map: dict[int, int] = {}

        for index, rnum in enumerate(nums):
            lnum = target - rnum
            if lnum in hash_map:
                return [hash_map[lnum], index]
            hash_map[rnum] = index

        raise ValueError("No solution")
