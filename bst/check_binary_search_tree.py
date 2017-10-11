# Checks whether a BST is valid.

class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def check_binary_search_tree(root):
    # store tuples of (node, lower_bound, upper_bound)
    # node must be between these bounds to be valid
    # lower bound is the value of the last node we turned right at
    # upper bound is the value of the last node we turned left at
    stack = [(root, -float('inf'), float('inf'))]

    while len(stack) > 0:
        parent = stack.pop()

        left = parent[0].left
        right = parent[0].right

        lower_bound = parent[1]
        upper_bound = parent[2]

        if parent[0].value < lower_bound or parent[0].value > lower_bound:
            return False

        if left != None:
            stack.append((left, lower_bound, parent[0].value))
        if right != None:
            stack.append((right, parent[0].value, upper_bound))

    return True

if __name__ == '__main__':
    pass
    # fuck it