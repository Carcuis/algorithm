class ListNode:
    def __init__(self, data: int):
        self.data = data
        self.next: ListNode | None = None
        self.prev: ListNode | None = None

    def copy(self) -> "ListNode":
        new_node = ListNode(self.data)
        new_node.next = self.next.copy() if self.next is not None else None
        return new_node


class LinkedList:
    def __init__(self, values: list[int] = []):
        self.head: ListNode | None = None
        if len(values) > 0:
            self.build_from_list(values)

    def build_from_list(self, values: list[int]) -> None:
        if not values or len(values) == 0:
            raise ValueError
        self.head = ListNode(values[0])
        current = self.head
        for value in values[1:]:
            new_node = ListNode(value)
            current.next = new_node
            new_node.prev = current
            current = new_node

    def insert(self, value: int, position: int) -> None:
        assert position >= 0 and isinstance(position, int)
        new_node = ListNode(value)
        if position == 0:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    break
                current = current.next
            if current is None:
                raise ValueError
            new_node.next = current.next
            new_node.prev = current
            if current.next is not None:
                current.next.prev = new_node
            current.next = new_node

    def delete(self, position: int) -> None:
        assert position >= 0 and isinstance(position, int)
        if self.head is None:
            raise ValueError
        current = self.head
        if position == 0:
            self.head = current.next
            if self.head is not None:
                self.head.prev = None
            return
        for _ in range(position):
            if current is None:
                break
            current = current.next
        if current is None:
            raise ValueError
        if current.prev is not None:
            current.prev.next = current.next
        if current.next is not None:
            current.next.prev = current.prev

    def draw(self) -> None:
        print("head -> ", end="")
        current = self.head
        while current is not None:
            print(f"({current.data})", end="")
            if current.next is not None:
                print(" <=> ", end="")
            current = current.next
        print()


def main():
    print("Creating a doubly linked list with values [1, 2, 3, 4, 5]")
    dll = LinkedList([1, 2, 3, 4, 5])
    dll.draw()

    print("\nInserting 6 at position 2")
    dll.insert(6, 2)
    dll.draw()

    print("\nDeleting node at position 3")
    dll.delete(3)
    dll.draw()


if __name__ == "__main__":
    main()

