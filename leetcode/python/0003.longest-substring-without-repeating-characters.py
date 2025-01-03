class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = -1
        max_length = 0
        hash_table: dict[str, int] = {}

        for index, char in enumerate(s):
            if char in hash_table and hash_table[char] > start:
                start = hash_table[char]
                hash_table[char] = index
            else:
                hash_table[char] = index
                max_length = max(index - start, max_length)

        return max_length

