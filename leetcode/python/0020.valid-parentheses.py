import unittest


# @leet start
class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        mapping: dict[str, str] = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack
# @leet end


class Test(unittest.TestCase):
    check = Solution().isValid

    def test_1(self):
        self.assertEqual(self.check("()"), True)

    def test_2(self):
        self.assertEqual(self.check("()[]{}"), True)

    def test_3(self):
        self.assertEqual(self.check("(]"), False)

    def test_4(self):
        self.assertEqual(self.check("([])"), True)

    def test_5(self):
        self.assertEqual(self.check("(])"), False)


if __name__ == "__main__":
    unittest.main()
