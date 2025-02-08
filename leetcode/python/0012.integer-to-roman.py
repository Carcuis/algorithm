import unittest


# @leet start
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_map: dict[int, str] = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I",
        }
        result = ""
        for value, symbol in roman_map.items():
            result += (num // value) * symbol
            num %= value
        return result
# @leet end


class Test(unittest.TestCase):
    get = Solution().intToRoman

    def test_1(self):
        self.assertEqual(self.get(3749), "MMMDCCXLIX")

    def test_2(self):
        self.assertEqual(self.get(58), "LVIII")

    def test_3(self):
        self.assertEqual(self.get(1994), "MCMXCIV")


if __name__ == "__main__":
    unittest.main()
