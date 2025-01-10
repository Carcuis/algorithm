import unittest


# @leet start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        len_s = len(s)
        if numRows == 1 or numRows >= len_s:
            return s

        output_list = ["" for _ in range(numRows)]

        index, direction = 0, 1
        for char in s:
            output_list[index] += char
            index += direction
            if index == 0 or index == numRows - 1:
                direction *= -1

        return "".join(output_list)
# @leet end


class Test(unittest.TestCase):
    convert = Solution().convert

    def test_1(self):
        self.assertEqual(self.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")

    def test_2(self):
        self.assertEqual(self.convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")

    def test_3(self):
        self.assertEqual(self.convert("A", 1), "A")

    def test_4(self):
        self.assertEqual(self.convert("AB", 1), "AB")

    def test_5(self):
        self.assertEqual(self.convert("AB", 3), "AB")


if __name__ == '__main__':
    unittest.main()
