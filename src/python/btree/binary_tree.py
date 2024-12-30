from collections import deque

import binarytree as bt


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right
        self.height: int = 1

    def copy(self) -> "TreeNode":
        # Create a new node with the same value
        new_node = TreeNode(self.val)

        # Recursively copy the left and right children
        if self.left:
            new_node.left = self.left.copy()
        if self.right:
            new_node.right = self.right.copy()

        # Copy the height
        new_node.height = self.height
        return new_node


class BinaryTree:
    def __init__(self, show_rotation: bool = False):
        self.root: TreeNode | None = None

    def build_from_leetcode_list(self, values: list) -> None:
        self.root = None
        self.root = self._build_from_leetcode_list(values, 0)

    def _build_from_leetcode_list(self, values: list, index: int) -> TreeNode | None:
        if index >= len(values) or values[index] is None:
            return None

        node = TreeNode(values[index])    # pyright: ignore[reportArgumentType]
        node.left = self._build_from_leetcode_list(values, 2 * index + 1)
        node.right = self._build_from_leetcode_list(values, 2 * index + 2)

        self.update_height(node)
        return node

    def update_height(self, node: TreeNode) -> None:
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    @staticmethod
    def get_height(node: TreeNode | None) -> int:
        if node is None:
            return 0
        return node.height

    def convert_to_leetcode_list(self, root: TreeNode | None = None) -> list:
        if root is None:
            if self.root is None:
                return []
            root = self.root

        result = []
        queue = deque([(root, 0)])
        while queue:
            node, index = queue.popleft()
            if index >= len(result):
                result.extend([None] * (index - len(result) + 1))
            result[index] = node.val
            if node.left:
                queue.append((node.left, 2 * index + 1))
            if node.right:
                queue.append((node.right, 2 * index + 2))
        return result

    def convert_to_leetcode_string(self, root: TreeNode | None = None) -> str:
        return str(self.convert_to_leetcode_list(root)).replace("None", "null")

    def draw(self, node: TreeNode | None = None) -> None:
        print(bt.build(self.convert_to_leetcode_list(node)))

    @property
    def preorder(self) -> list:
        return self._preorder(self.root)

    def _preorder(self, node: TreeNode | None) -> list:
        if node is None:
            return []

        result = []
        result.append(node.val)
        result.extend(self._preorder(node.left))
        result.extend(self._preorder(node.right))
        return result

    @property
    def inorder(self) -> list:
        return self._inorder(self.root)

    def _inorder(self, node: TreeNode | None) -> list:
        if node is None:
            return []

        result = []
        result.extend(self._inorder(node.left))
        result.append(node.val)
        result.extend(self._inorder(node.right))
        return result

    @property
    def postorder(self) -> list:
        return self._postorder(self.root)

    def _postorder(self, node: TreeNode | None) -> list:
        if node is None:
            return []

        result = []
        result.extend(self._postorder(node.left))
        result.extend(self._postorder(node.right))
        result.append(node.val)
        return result


def test_traversal() -> None:
    input = ["T", "A", "B", "C", "D", "E", "F", None, None, None, "G", None, None, "H"]
    tree = BinaryTree()
    tree.build_from_leetcode_list(input)
    assert tree is not None

    print("Input tree:")
    tree.draw()
    print("Preorder traversal:")
    print(tree.preorder)
    print()
    print("Inorder traversal:")
    print(tree.inorder)
    print()
    print("Postorder traversal:")
    print(tree.postorder)


if __name__ == "__main__":
    test_traversal()
