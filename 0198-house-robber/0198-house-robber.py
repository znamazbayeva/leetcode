class Solution:
    def rob(self, nums: List[int]) -> int:
        n= len(nums)
        dp = [0]+[0]*n
        dp[1] = nums[0]
        for i in range(2, n+1):
            dp[i] = max([dp[j] + nums[i-1] for j in range(i-1)])
        return max(dp)