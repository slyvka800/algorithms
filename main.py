import math

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

    # printing graph stuff
    def print_ascii_graph(self):
        pairs = self._get_pairs_in_order()
        self.print_by_lines(pairs)

    def print_spaces(self, num):
        str = num * " "
        print(str, end="")

    def print_arrows(self, nodes_count, space_from_start):
        self.print_spaces(space_from_start)
        for i in range(nodes_count // 2):
            print("/", end="")
            self.print_spaces(space_from_start * 2)
            print("\\", end="")
            self.print_spaces(space_from_start * 2)

    def print_nodes(self, nodes, space_from_start):
        self.print_spaces(space_from_start)
        while nodes:
            print(nodes.pop(0), end="")
            self.print_spaces(space_from_start * 2)

    def print_by_lines(self, pairs):

        if self.root is None:
            return

        count_pairs = len(pairs)
        count_lines = int(math.log2(count_pairs)) + 1
        nums_on_last_line = pow(count_lines, count_lines - 1)

        pairs_per_line = 1
        spaces_from_start = nums_on_last_line // 2

        # print root
        self.print_spaces(spaces_from_start*2)
        print(self.root.value)

        for i in range(count_lines):

            nums_in_line = []

            for j in range(pairs_per_line):
                if not pairs:
                    break

                # print(pairs.pop(0), end=" ")
                pair = pairs.pop(0)
                nums_in_line.append(pair[0])
                nums_in_line.append(pair[1])

            self.print_arrows(len(nums_in_line), spaces_from_start)
            print()
            self.print_nodes(nums_in_line, spaces_from_start)
            print()

            spaces_from_start //= 2

            pairs_per_line *= 2

    def _get_pairs_in_order(self):
        if self.root is None:
            return

        queue = [self.root]
        pairs = []
        for i in queue:
            pair = []
            if i.left is not None:
                queue.append(i.left)
                pair.append(i.left.value)
            else:
                pair.append("N")

            if i.right is not None:
                queue.append(i.right)
                pair.append(i.right.value)
            else:
                pair.append("N")

            pairs.append(pair)

        return pairs

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
    tree.insert(78)

    # print(tree.search(4))
    # print(tree.search(7))

    # tree.print_tree()
    tree.print_ascii_graph()
