class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int j = 0, i = 0, k = 1, max= 0;
        for(; i < nums.size(); i++) {
            if(nums[i] == 0) k--;
            if(k < 0) {
                if(nums[j] == 0) k++;
                ++j;
            }
            
            max = max > i - j ? max : i-j;
        }
        return max;
    }
};