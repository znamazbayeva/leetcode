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
    int maxDepth(TreeNode* root) {
        if(!root) return 0;
        int res = 1;
        stack<pair<TreeNode*, int>> stack;
        stack.push(make_pair(root, 1));
        while(!stack.empty()) {
            pair<TreeNode*, int> top = stack.top(); stack.pop();
            res = max(res, top.second);
            if(top.first->left) stack.push(make_pair(top.first->left, top.second+1));
            if(top.first->right) stack.push(make_pair(top.first->right, top.second+1));
        }
        return res;
    }
};