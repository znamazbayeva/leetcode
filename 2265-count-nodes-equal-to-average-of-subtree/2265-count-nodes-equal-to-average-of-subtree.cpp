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
    int ans;
    int averageOfSubtree(TreeNode* root) {
        solution(root);
        return ans;
    }
    pair<int,int> solution(TreeNode* root) {
        if(!root) return {0,0};
        pair<int,int> left = solution(root->left);
        pair<int,int> right = solution(root->right);
        
        int sum = left.first + right.first + root->val;
        int cnt = left.second + right.second + 1;
        if (sum/cnt == root->val) ans++;
        return {sum, cnt};
    }
};