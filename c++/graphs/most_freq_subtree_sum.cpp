/*
Given the root of a tree, return a vector of the most frequent subtree sums
(could be multiple if they all occur the same number of times.)

*/

#include <stdio>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    std::unordered_map<int, int> sumsFreq;
    
    int subtreeSum(TreeNode* root) {
        if (!root) {
            return 0;
        } else {
            int sum = (root->val + subtreeSum(root->left) + subtreeSum(root->right));
            if (sumsFreq.find(sum) != sumsFreq.end()) {
                sumsFreq[sum] += 1;
            } else {
                sumsFreq[sum] = 1;
            }
            return sum;
        }
    }
    
    vector<int> findFrequentTreeSum(TreeNode* root) {
        int sum = subtreeSum(root); // fills up the map

        int mostFreq = 0;
        std::vector<int> result;
        
        for (std::pair<int, int> el : sumsFreq) {
            if (el.second > mostFreq) {
                result.clear();
                mostFreq = el.second;
                result.push_back(el.first);
            } else if (el.second == mostFreq) {
                result.push_back(el.first);
            }
        }
        return result;
    }
};