/*
Given a non-empty binary search tree, find the leftmost element in the bottom layer:
Approach: Do BFS, add right children before left children. Return the final element in the queue.
*/

#include <queue>
#include <stdio>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    std::queue<TreeNode*> BFSQueue;
    
    int findBottomLeftValue(TreeNode* root) {
        BFSQueue.push(root);
        
        TreeNode *currentNode;
        while (!BFSQueue.empty()) {
            currentNode = BFSQueue.front();
            BFSQueue.pop();
            
            // Always push right child first.
            if (currentNode->right) {
                BFSQueue.push(currentNode->right);
            }
            if (currentNode->left) {
                BFSQueue.push(currentNode->left);
            }
        }
        return currentNode->val;
    }
};

int main(int argc, char const *argv[])
{
    /* code */
    return 0;
}