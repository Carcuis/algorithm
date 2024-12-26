from binary_tree import BinaryTree, TreeNode


class AVLTree(BinaryTree):
    def __init__(self, show_rotation: bool = False):
        super().__init__()
        self.show_rotation = show_rotation

    def build_from_list(self, values: list[int]) -> None:
        self.root = None
        for value in values:
            if value is not None:
                self.root = self._insert(self.root, value)

    def insert(self, key: int) -> None:
        self.root = self._insert(self.root, key)

    def _insert(self, node: TreeNode | None, key: int) -> TreeNode:
        if node is None:
            return TreeNode(key)
        if key < node.val:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        self.update_height(node)
        balance = self.get_balance(node)

        if balance >= 2:
            assert node.left is not None

            if key < node.left.val:
                # Left Left Case
                return self.right_rotate(node)
            else:
                # Left Right Case
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        elif balance <= -2:
            assert node.right is not None

            if key > node.right.val:
                # Right Right Case
                return self.left_rotate(node)
            else:
                # Right Left Case
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

        return node

    def delete(self, key: int) -> None:
        self.root = self._delete(self.root, key)

    def _delete(self, node: TreeNode | None, key: int) -> TreeNode | None:
        if node is None:
            print(f"Warning: Key {key} not found in the tree")
            return None

        # Find the node to be deleted
        if key < node.val:
            node.left = self._delete(node.left, key)
        elif key > node.val:
            node.right = self._delete(node.right, key)
        else:  # key == node.val
            # Found the node, do the deletion

            # Node with only one child or no child, directly return the child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            successor = self.get_min_value_node(node.right)
            node.val = successor.val
            node.right = self._delete(node.right, successor.val)

        # Update the height of the current node
        self.update_height(node)

        # Rebalance the tree
        balance = self.get_balance(node)

        if balance >= 2:
            assert node.left is not None

            if self.get_balance(node.left) >= 1:
                # Left Left Case
                return self.right_rotate(node)
            else:
                # Left Right Case
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        if balance <= -2:
            assert node.right is not None

            if self.get_balance(node.right) <= -1:
                # Right Right Case
                return self.left_rotate(node)
            else:
                # Right Left Case
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

        return node

    def left_rotate(self, x: TreeNode) -> TreeNode:
        assert x.right is not None

        if self.show_rotation:
            self.draw()
            print(" " * 10 + "|")
            print(f"Left Rotate: ( {x.val}, {x.right.val} )")
            print(" " * 10 + "↓")

        y = x.right
        x.right = y.left    # Make y's left subtree x's right subtree
        y.left = x
        self.update_height(x)
        self.update_height(y)

        return y

    def right_rotate(self, x: TreeNode) -> TreeNode:
        assert x.left is not None

        if self.show_rotation:
            self.draw()
            print(" " * 10 + "|")
            print(f"Right Rotate: ( {x.left.val}, {x.val} )")
            print(" " * 10 + "↓")

        y = x.left
        x.left = y.right    # Make y's right subtree x's left subtree
        y.right = x
        self.update_height(x)
        self.update_height(y)

        return y

    def get_balance(self, node: TreeNode | None) -> int:
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def get_min_value_node(self, node: TreeNode) -> TreeNode:
        if node.left is None:
            return node
        return self.get_min_value_node(node.left)


def test_insertion() -> None:
    input = [12, 23, 34, 45, 56, 67, 78, 89]
    avl_tree = AVLTree(show_rotation=True)
    for value in input:
        print(f"- [[ Inserting ( {value} ) ]]:\n")
        avl_tree.insert(value)
        avl_tree.draw()


def test_deletion() -> None:
    input = [43, 15, 79, None, 28, 66, 81, None, None, None, None, 58, 75]
    avl_tree = AVLTree(show_rotation=True)
    avl_tree.build_from_leetcode_list(input)

    print("- Initial tree:")
    avl_tree.draw()

    delete_values = [28, 43, 58, 15]
    for value in delete_values:
        print(f"- [[ Deleting ( {value} ) ]]:\n")
        avl_tree.delete(value)
        avl_tree.draw()


if __name__ == "__main__":
    test_insertion()
    test_deletion()

