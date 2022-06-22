class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(target, arr, nums):
            if target == 0:
                res.append(arr.copy())
                return
            if target < 0 or not nums:
                return 
            for i in range(len(nums)):
                if i== 0 or (i > 0 and nums[i] != nums[i-1]):
                    dfs(target - nums[i], arr + [nums[i]], nums[i+1:])
        dfs(target, [], candidates)
        return res