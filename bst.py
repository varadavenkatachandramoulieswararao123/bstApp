from binarytree import Node, bst


class BinarySearchTree:
    def __init__(self):
        self.root = bst(height=3, is_perfect=True)

    def __str__(self) -> str:
        return str(self.root)

    def clearAll(self):
        self.root = bst(height=0)

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, root, value):
        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self._insert_recursive(root.left, value)
        elif value > root.value:
            root.right = self._insert_recursive(root.right, value)

        return root

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, root, value):
        if root is None:
            return root

        if value < root.value:
            root.left = self._delete_recursive(root.left, value)
        elif value > root.value:
            root.right = self._delete_recursive(root.right, value)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor
            root.value = self._min_value_node(root.right).value

            # Delete the inorder successor
            root.right = self._delete_recursive(root.right, root.value)

        return root

    def _min_value_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        print(result)
        return result

    def _inorder_recursive(self, root, result):
        if root:
            self._inorder_recursive(root.left, result)
            result.append(root.value)
            self._inorder_recursive(root.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, root, result):
        if root:
            result.append(root.value)
            self._preorder_recursive(root.left, result)
            self._preorder_recursive(root.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, root, result):
        if root:
            self._postorder_recursive(root.left, result)
            self._postorder_recursive(root.right, result)
            result.append(root.value)


# Example usage:
if __name__ == "__main__":
    myBst = BinarySearchTree()

    myBst.insert(50)
    myBst.insert(30)
    myBst.insert(20)
    myBst.insert(40)
    myBst.insert(70)
    myBst.insert(60)
    myBst.insert(80)

    # myBst.print()
    print(str(myBst))

    print("Inorder Traversal:")
    print(myBst.inorder_traversal())

    print("Search for 30:")
    result = myBst.search(30)
    if result:
        print(f"Found: {result.value}")
    else:
        print("Not Found")

    print("Delete 30:")
    myBst.delete(30)
    print("Inorder Traversal after deletion:")
    print(myBst.inorder_traversal())
