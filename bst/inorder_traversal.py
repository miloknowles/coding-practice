# Traverse a BST in order.
"""
Recursive Idea: inorderTraversal(node.left) + node + inorderTraversal(node.right)

Tree Walk Idea:
- store a stack while going left
- if you can't go left any more, add top stack node to solution, then go right
"""

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class SolutionRecursive(object):
  def inorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    # Base case
    if (root == None):
      return []
    elif (root.left == None and root.right == None):
      return [root.val]
    else:
      result = []
      if (root.left != None):
        result.extend(self.inorderTraversal(root.left))
      result.append(root.val)
      if (root.right != None):
        result.extend(self.inorderTraversal(root.right))
      return result

class SolutionWalk(object):
	def inorderTraversal(self, root):
		"""
    :type root: TreeNode
    :rtype: List[int]
    """
    stack = []
    solution = []

    current = root
    while (len(stack) != 0 or current != None):

    	# Go left as far as possible
    	if (current != None):
    		stack.append(current)
    		current = current.left

    	# If no more lefts possible, add top node to solution and go right
    	else:
    		current = stack.pop()
    		solution.append(current.val)
    		current = current.right

    return solution
