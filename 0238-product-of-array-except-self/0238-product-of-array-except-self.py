class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force O(n^2) 
        # ans = [0]*len(nums)
        # print(ans)
        # for i, numi in enumerate(nums):
        #     mult = 1
        #     for j, numj in enumerate(nums):
        #         if j != i:
        #             mult *= nums[j]
        #     ans[i] = mult
        # return ans
        n = len(nums)
        prefix, suffix = [0]*n, [0]*n
        prefix[0], suffix[n-1] = nums[0], nums[n-1]
        ans = [0]*n
        for i in range(1, n):
            prefix[i] = prefix[i-1]*nums[i]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1]*nums[i]
        print(prefix, suffix)
        for i in range(0, n):
            ans[i] = (prefix[i-1] if i > 0 else 1) * (suffix[i+1] if i < n-1 else 1)
        return ans