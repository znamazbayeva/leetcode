class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(arr, nums):
            if not nums:
                res.append(arr.copy())
                return
            for i in range(len(nums)):
                dfs(arr+ [nums[i]], nums[: i] + nums[i+1:])
        dfs([], nums)
        return res
            
        