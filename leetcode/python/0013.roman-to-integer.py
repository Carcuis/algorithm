import unittest


# @leet start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map: dict[str, int] = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }

        result = 0
        for c in reversed(s):
            num = roman_map[c]
            result += num if result < 5 * num else -num

        return result
# @leet end


class Test(unittest.TestCase):
    get = Solution().romanToInt

    def test_1(self):
        self.assertEqual(self.get("III"), 3)

    def test_2(self):
        self.assertEqual(self.get("LVIII"), 58)

    def test_3(self):
        self.assertEqual(self.get("MCMXCIV"), 1994)


if __name__ == "__main__":
    unittest.main()
