/*
Check if the tree "t" is equal to any subtree of "s".
*/

#include <stdio>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

bool cmpTrees(TreeNode *t1, TreeNode *t2) {
    // If both are NULL, they are equal.
    if (t1 == NULL && t2 == NULL) {
        return true;
    
    // If only one is NULL, they cannot be equal.
    } else if (t1 == NULL || t2 == NULL) {
        return false;
    }
    
    // t1 and t2 are not NULL, so check their values.
    if (t1->val != t2->val) {
        return false;
    
    // If values match, must recurse on children.
    } else {
        bool left = cmpTrees(t1->left, t2->left);
        bool right = cmpTrees(t1->right, t2->right);
        return (left && right);
    }
}

class Solution {
public:
    bool isSubtree(TreeNode* s, TreeNode* t) {
        // Check if s and t are equal.
        if (cmpTrees(s, t)) {
            return true;
        
        // Check t against the left and right children of s.
        } else {
            // Safe from case where s is NULL.
            bool left = s ? isSubtree(s->left, t) : false;
            bool right = s ? isSubtree(s->right, t) : false;
            return (left || right);
        }
    }
};

int main(int argc, char const *argv[])
{
    /* code */
    return 0;
}