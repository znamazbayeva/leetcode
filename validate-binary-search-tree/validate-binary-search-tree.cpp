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
    bool isValidBST(TreeNode* root) {
        if(!root) return true;
        stack<TreeNode*>stack;
        TreeNode* prev = NULL;
        while(root != NULL || !stack.empty()) {
            while(root) {
                stack.push(root);
                root = root->left;
            }
            root = stack.top();
            stack.pop();
            if(prev != NULL && root->val <= prev->val) return false;
            prev= root;
            root = root->right;
        }
        return true;
    }
};