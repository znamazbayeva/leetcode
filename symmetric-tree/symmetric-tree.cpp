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
    bool isMirror(TreeNode* left, TreeNode* right) {
        if(!left || !right) return left == right;
        if(left->val != right->val) return false;
        return isMirror(left->right, right->left) && isMirror(left->left, right->right);
    }
    bool isSymmetric(TreeNode* root) {
        return !root || isMirror(root->left, root->right);
    }
};