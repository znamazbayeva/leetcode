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
    
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ans;
        if(!root) return ans;
        queue<TreeNode*> occ;
        occ.push(root);
        while(!occ.empty()) {
            int len = occ.size();
            TreeNode* back = occ.back();
            ans.push_back(back->val);
            for (int i = 0; i < len; i++) {
                TreeNode* top = occ.front();
                occ.pop();
                if(top->left) occ.push(top->left);
                if(top->right) occ.push(top->right);
            }
        }
        return ans;
    }
};