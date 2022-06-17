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
    int cnt = 0;
    int val = 0;
    void helper(TreeNode* root, int k) 
    {
        if(!root) return;
        kthSmallest(root->left, k);
        cnt++;
        if(k == cnt) {val =  root->val; return;}
        kthSmallest(root->right, k);
    }
    int kthSmallest(TreeNode* root, int k) {
        helper(root, k);
        return val;
        // Solution 1. Using DFS and stack
        // Time O(n)
        // Space O(1)? or O(n)
        // stack<TreeNode*> occ;
        // while(root || !occ.empty()) {
        //     while(root) {
        //         occ.push(root);
        //         root = root->left;
        //     }
        //     root = occ.top();
        //     if(k==1) return root->val;
        //     k--;
        //     occ.pop();
        //     root = root->right;
        // }
        // return -1;
        
        
    }
};