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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(!p && !q) return true;
        bool left = isSameTree(p ? p->left : NULL, q ? q->left : NULL);
        bool right = isSameTree(p ? p->right : NULL, q ? q->right : NULL);
        bool d;
        if(p && q) d = (p->val == q->val);
        else if (p || q) d = p && q;
        return left && right && d;
    }
};