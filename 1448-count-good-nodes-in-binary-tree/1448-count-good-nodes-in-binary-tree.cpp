/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int findGoodNodes(TreeNode* root, int maxNumber) {
        if(!root) return 0;
        int res = root->val >= maxNumber ? 1 : 0;
        res += findGoodNodes(root->left, max(root->val, maxNumber));
        res += findGoodNodes(root->right, max(root->val, maxNumber));
        return res;
        
    }
    int goodNodes(TreeNode* root) {
        if(!root) return 0;
        int max = root->val;
        return findGoodNodes(root, max);
    }
};