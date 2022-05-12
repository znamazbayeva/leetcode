class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int j = 0, i = 0, k = 1, max= 0;
        for(; i < nums.size(); i++) {
            if(!k && nums[i] == 0) {
                while(nums[j++] != 0 ){}
                ++k;
            }
            if(nums[i] == 0) k--;
            max = max > i - j ? max : i-j;
        }
        return max;
    }
};