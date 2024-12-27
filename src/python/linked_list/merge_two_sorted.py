from doubly_linked_list import LinkedList, ListNode


def merge_recursive(L: LinkedList, R: LinkedList) -> LinkedList:
    assert L.head is not None and R.head is not None

    def _merge(L: ListNode | None, R:ListNode | None) -> ListNode | None:
        if L is None:
            return R
        if R is None:
            return L

        if L.data <= R.data:
            L.next = _merge(L.next, R)
            if L.next is not None:
                L.next.prev = L
            return L
        else:
            R.next = _merge(L, R.next)
            if R.next is not None:
                R.next.prev = R
            return R

    result = LinkedList()
    result.head = _merge(L.head.copy(), R.head.copy())
    return result


def merge_iterative(L: LinkedList, R: LinkedList) -> LinkedList:
    assert L.head is not None and R.head is not None

    L_ = L.head.copy()
    R_ = R.head.copy()

    current: ListNode | None = None
    while L_ is not None or R_ is not None:
        if L_ is not None and (R_ is None or L_.data < R_.data):
            if current is None:
                current = L_
            else:
                L_.prev = current
                current.next = L_
                current = current.next
            L_ = L_.next
        else:
            assert R_ is not None
            if current is None:
                current = R_
            else:
                R_.prev = current
                current.next = R_
                current = current.next
            R_ = R_.next

    assert current is not None
    while current.prev is not None:
        current = current.prev

    result = LinkedList()
    result.head = current
    return result


def main():
    # Test the merge function
    L = LinkedList([2, 4, 7, 8])
    R = LinkedList([1, 5, 6, 9])

    print("List L:\n")
    L.draw()
    print("\nList R:\n")
    R.draw()

    print("\nMerged List Using Recursive Merge:\n")
    merge_recursive(L, R).draw()

    print("\nMerged List Using Iterative Merge:\n")
    merge_iterative(L, R).draw()


if __name__ == "__main__":
    main()

