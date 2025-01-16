import unittest

from util.linked_list import ListNode, array_to_list, list_to_array


# @leet start
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2
# @leet end


class Test(unittest.TestCase):
    merge = Solution().mergeTwoLists

    def test_1(self):
        l1 = array_to_list([1, 2, 4])
        l2 = array_to_list([1, 3, 4])
        self.assertEqual(list_to_array(self.merge(l1, l2)), [1, 1, 2, 3, 4, 4])

    def test_2(self):
        l1 = array_to_list([])
        l2 = array_to_list([])
        self.assertEqual(list_to_array(self.merge(l1, l2)), [])

    def test_3(self):
        l1 = array_to_list([])
        l2 = array_to_list([0])
        self.assertEqual(list_to_array(self.merge(l1, l2)), [0])


if __name__ == '__main__':
    unittest.main()
