class Tree:

    def __init__(self):
        self.root = None

    def search(self, value: int):
        found_node = self._search(self.root, value)
        if found_node is None:
            return False
        return True

    def insert(self, value):

        if self.root is None:
            self.root = Node(value=value)
            return

        return self._insert(self.root, value)

    def print_tree(self):
        self._print_tree(self.root)

    def max_value(self):
        pass

    def min_value(self):
        pass

    def delete(self):
        pass

    def _search(self, node_to_check, value):
        if (node_to_check is None) or (node_to_check.value == value):
            return node_to_check

        if value > node_to_check.value:
            return self._search(node_to_check.right, value)
        else:
            return self._search(node_to_check.left, value)

    def _insert(self, current_node, value):
        if value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value=value, parent=current_node)
                return
            return self._insert(current_node.right, value)
        else:
            if current_node.left is None:
                current_node.left = Node(value=value, parent=current_node)
                return
            return self._insert(current_node.left, value)

    def _print_tree(self, current):
        if current is None:
            return
        print(current.value)
        self._print_tree(current.right)
        self._print_tree(current.left)


class Node:
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.value = value
        self.parent = parent


if __name__ == "__main__":
    tree = Tree()
    tree.insert(10)
    tree.insert(8)
    tree.insert(11)
    tree.insert(4)

    print(tree.search(4))
    print(tree.search(7))

    tree.print_tree()
