class Solution:
    def rob(self, nums: List[int]) -> int:
        # 2 3 2
        n= len(nums)
        if n<= 3:
            return max(nums)
        def helper(nums):
            n= len(nums)
            dp = [0]+[0]*n
            dp[1] = nums[0]
            for i in range(2, n+1):
                dp[i] = max(dp[i-1], nums[i-1] + dp[i-2])
            return max(dp)
        l,r = helper(nums[:n-1]), helper(nums[1:])
        return max(l,r)
            