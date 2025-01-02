# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        def _add(l: ListNode | None, r: ListNode | None, carry: int) -> tuple[ListNode | None, int]:
            if l is None:
                if r is None:
                    return (ListNode(1), 0) if carry == 1 else (None, 0)
                _carry = (r.val + carry) // 10
                r.val = (r.val + carry) % 10
                r.next, carry = _add(None, r.next, _carry)
                return r, carry

            if r is None:
                _carry = (l.val + carry) // 10
                l.val = (l.val + carry) % 10
                l.next, carry = _add(None, l.next, _carry)
                return l, carry

            _carry = (l.val + r.val + carry) // 10
            l.val = (l.val + r.val + carry) % 10
            l.next, carry = _add(l.next, r.next, _carry)
            return l, carry

        return _add(l1, l2, 0)[0]

