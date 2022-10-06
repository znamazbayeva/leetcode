class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        majorityElement = None
        for num in nums:
            if counter == 0:
                majorityElement = num
            counter += (1 if num == majorityElement else -1)
        return majorityElement
                