/*
Flatten a binary tree into a linked list, where the order is given by a preorder traversal of the tree.
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
*/

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
  void flatten(TreeNode* root) {
    std::vector<TreeNode*> stack;
    if (root) { stack.push_back(root); }
    
    TreeNode *prev = new TreeNode(0);
    while (!stack.empty()) {
      TreeNode *node = stack.back();
      stack.pop_back();
      
      // Make sure to push the left child LAST, so that its visited FIRST
      if (node->right) { stack.push_back(node->right); }
      if (node->left) { stack.push_back(node->left); }
  
      node->left = NULL;
      node->right = NULL;
      
      prev->right = node;
      prev = node;
    }
  }
};