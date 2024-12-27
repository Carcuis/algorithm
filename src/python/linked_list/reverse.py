from doubly_linked_list import LinkedList


def reverse(ddl: LinkedList) -> None:
    current = ddl.head

    while current is not None:
        temp = current.next
        current.next = current.prev
        current.prev = temp
        ddl.head = current
        current = temp


def main():
    dll = LinkedList([1, 2, 3, 4, 5])
    print("Original List:\n")
    dll.draw()

    reverse(dll)
    print("\nReversed List:\n")
    dll.draw()


if __name__ == "__main__":
    main()

