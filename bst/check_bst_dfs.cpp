
 // Definition for a binary tree node.
 struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };

struct BoundedTreeNode {
    long lower_bound;
    long upper_bound;
    
    int val;
    TreeNode *left;
    TreeNode *right;
    
    BoundedTreeNode(TreeNode* n, long l, long h) :
        val(n->val),
        left(n->left),
        right(n->right),
        lower_bound(l),
        upper_bound(h) {};
};


class Solution {
public:
    bool isValidBST(TreeNode* root) {

        std::stack<BoundedTreeNode*> stack;
        if (root) { stack.push(new BoundedTreeNode(root, -2147483649, 2147483648)); } // deal with largest ints
        
        while (!stack.empty()) {
            BoundedTreeNode *btn = stack.top();
            stack.pop();
            if (btn->val <= btn->lower_bound || btn->val >= btn->upper_bound) {
                std::cout << btn->val << btn->lower_bound << btn->upper_bound << std::endl;
                return false;
            } else {
                if (btn->left) {
                    stack.push(new BoundedTreeNode(btn->left, btn->lower_bound, btn->val));
                }
                if (btn->right) {
                    stack.push(new BoundedTreeNode(btn->right, btn->val, btn->upper_bound));
                }
            }
        }
        return true;
    }
};