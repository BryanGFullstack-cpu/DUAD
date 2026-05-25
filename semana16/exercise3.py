#Binary Tree


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert_left(self, parent, value):
        new_node = Node(value)
        parent.left = new_node
        return new_node

    def insert_right(self, parent, value):
        new_node = Node(value)
        parent.right = new_node
        return new_node

    def print_tree(self):
        self._print_recursive(self.root, 0)

    def _print_recursive(self, node, level):
        if node is None:
            return
        indent = "   " * level
        print(f"{indent}- {node.value}")
        self._print_recursive(node.left, level + 1)
        self._print_recursive(node.right, level + 1)



tree = BinaryTree("A")

b = tree.insert_left(tree.root, "B")
c = tree.insert_right(tree.root, "C")

tree.insert_left(b, "D")
tree.insert_right(b, "E")

tree.insert_left(c, "F")
tree.insert_right(c, "G")

tree.print_tree()



#batalle un poco, en entenderlo pero ahi le dejo el resultado... Investigue un poco mas sobre este.


#los agregue en main por error
