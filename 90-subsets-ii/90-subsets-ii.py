class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, arr, nums):
            res.append(arr.copy())
            if not nums:
                return
            for i in range(len(nums)):
                if i==0 or (i-1>=0 and nums[i] != nums[i-1]):
                    print(i, arr, nums)
                    dfs(i, arr+[nums[i]], nums[i+1:])
        dfs(0, [], nums)
        return res