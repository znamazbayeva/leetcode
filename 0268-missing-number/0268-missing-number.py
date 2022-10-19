class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # a^b^b = a
        xor, i = 0, 0
        for i in range(0, len(nums)):
            xor = xor^i^nums[i]
        return xor^len(nums)