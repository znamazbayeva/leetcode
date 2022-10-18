class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix, suffix, maxCurr = 0, 0, float(-inf)
        for i in range(0, len(nums)):
            prefix = (prefix or 1)*nums[i]
            suffix = (suffix or 1)*nums[~i]
            print(~i)
            maxCurr = max(maxCurr, prefix, suffix)
        return maxCurr