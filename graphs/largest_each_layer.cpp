/*
Given a binary tree, return a vector of the largest element in each row.
*/

#include <queue>
#include <stdio>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// TreeNode that also stores its height in a tree.
struct TreeNodeHeight : TreeNode {
    int height;
    TreeNodeHeight(TreeNode* t, int h) : TreeNode(t->val), height(h) {
        left = t->left;
        right = t->right;
    };
};

class Solution {
public:
    std::queue<TreeNodeHeight*> Q;
    
    vector<int> largestValues(TreeNode* root) {
        std::vector<int> largest;
        
        if (root) {
            TreeNodeHeight *augRoot = new TreeNodeHeight(root, 0);
            Q.push(augRoot);
        }
        
        while (!Q.empty()) {
            
            // Get item from the queue, check if it is largest in its layer
            TreeNodeHeight *node = Q.front();
            if (node->height >= largest.size()) {
                largest.push_back(node->val);
            } else if (node->val > largest[node->height]) {
                largest[node->height] = node->val;
            }
            Q.pop();

            if (node->left) {
                TreeNodeHeight *left = new TreeNodeHeight(node->left, node->height+1);
                Q.push(left);
            }
            if (node->right) {
                TreeNodeHeight *right = new TreeNodeHeight(node->right, node->height+1);
                Q.push(right);
            }
        }
        return largest;
    }
};