import unittest


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        def _add(l: ListNode | None, r: ListNode | None, carry: int) -> tuple[ListNode | None, int]:
            if l is None or r is None:
                if l is None:
                    l, r = r, l
                if l is None:
                    return (ListNode(1), 0) if carry == 1 else (None, 0)

            carry, l.val = divmod(l.val + (r.val if r else 0) + carry, 10)
            l.next, carry = _add(l.next, r.next if r else None, carry)
            return l, carry

        return _add(l1, l2, 0)[0]
# @leet end


class Test(unittest.TestCase):
    add = Solution().addTwoNumbers

    def list_to_array(self, node: ListNode | None) -> list[int]:
        array = []
        while node:
            array.append(node.val)
            node = node.next
        return array

    def array_to_list(self, array: list[int]) -> ListNode | None:
        if not array:
            return None
        head = ListNode(array[0])
        current = head
        for val in array[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def test_1(self):
        l1 = self.array_to_list([2, 4, 3])
        l2 = self.array_to_list([5, 6, 4])
        self.assertEqual(self.list_to_array(self.add(l1, l2)), [7, 0, 8])

    def test_2(self):
        l1 = self.array_to_list([0])
        l2 = self.array_to_list([0])
        self.assertEqual(self.list_to_array(self.add(l1, l2)), [0])

    def test_3(self):
        l1 = self.array_to_list([9, 9, 9, 9, 9, 9, 9])
        l2 = self.array_to_list([9, 9, 9, 9])
        self.assertEqual(self.list_to_array(self.add(l1, l2)), [8, 9, 9, 9, 0, 0, 0, 1])

    def test_4(self):
        l1 = self.array_to_list([2, 4, 9])
        l2 = self.array_to_list([5, 6, 4, 9])
        self.assertEqual(self.list_to_array(self.add(l1, l2)), [7, 0, 4, 0, 1])


if __name__ == '__main__':
    unittest.main()

