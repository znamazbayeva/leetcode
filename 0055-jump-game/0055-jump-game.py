class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        if nums[0] == 0:
            return False
        dp = [0]*(n-1)
        dp[0] = nums[0]
        for i in range(1, n-1):
            if nums[i] == 0 and dp[i-1] -1 == 0:
                return False
            dp[i] = max(dp[i-1] - 1, nums[i])
        return True if dp[-1] > 0 else False