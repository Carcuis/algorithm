class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def list_to_array(node: ListNode | None) -> list[int]:
    array = []
    while node:
        array.append(node.val)
        node = node.next
    return array


def array_to_list(array: list[int]) -> ListNode | None:
    if not array:
        return None
    head = ListNode(array[0])
    current = head
    for val in array[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

