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
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> occ;
        while(root || !occ.empty()) {
            while(root) {
                occ.push(root);
                root = root->left;
            }
            root = occ.top();
            if(k==1) return root->val;
            k--;
            occ.pop();
            root = root->right;
        }
        
        return -1;
    }
};