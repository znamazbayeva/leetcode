class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*(len(nums))
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[i] + 1, dp[j])
        return max(dp)