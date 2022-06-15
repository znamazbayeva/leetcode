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
    void findGoodNodes(TreeNode* root, int &goodNodesSum, int maximumNumber) {
        if(!root) return;
        if(root->val >= maximumNumber) { 
            goodNodesSum++; 
            maximumNumber = max(root->val, maximumNumber); 
        } 
        findGoodNodes(root->left, goodNodesSum, maximumNumber);
        maximumNumber = max(root->val, maximumNumber);
        findGoodNodes(root->right, goodNodesSum, maximumNumber);
    }
    int goodNodes(TreeNode* root) {
        if(!root) return 0;
        int goodNodesSum = 0;
        int max = root->val;
        findGoodNodes(root, goodNodesSum, max);
        return  goodNodesSum;
    }
};