class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.get_tree(tree.root, "")[:-1]
        else:
            print("Traversal type ", + str(traversal_type) + " is not supported")
            return False
    def get_tree(self, start, traversal):
        """Root->Left->Rigth"""
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.get_tree(start.left, traversal)
            traversal = self.get_tree(start.right, traversal)
        return traversal

    def sum_tree(self):
        values = self.get_tree(self.root, "")[:-1].split("-")
        values = [int(x) for x in values]
        return sum(values)


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(tree.print_tree("preorder"))
print(tree.sum_tree())