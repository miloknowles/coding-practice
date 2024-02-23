""" Checks whether a BST is valid using recursion. """

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def checkSubtree(self, node, lower_bound, upper_bound):
        if (node == None):
            return True
        elif (node.val <= lower_bound or node.val >= upper_bound):
            return False
        else:
            leftValid, rightValid = False, False
            leftValid = self.checkSubtree(node.left, lower_bound, node.val)
            rightValid = self.checkSubtree(node.right, node.val, upper_bound)
            return leftValid and rightValid
            
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.checkSubtree(root, float('-inf'), float('inf'))