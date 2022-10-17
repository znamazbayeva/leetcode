class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0, n-1
        # [4,5,6,7,0,1,2]
        # mid = 7, l =4, r =2
        # mid 7 > 4
        # l > r => l = 0
        # mid =1  l =0 r =2
        # mid 1 > 0
        # 0 < 2 r = 1
        # l = 0 r = 1 mid = 0
        
        
        while l < r:
            mid = (r+l)//2
            if nums[mid] < nums[l]:
                if nums[r] < nums[l]:
                    r = mid 
                else:
                    l = mid + 1
            else:
                if nums[l] > nums[r]:
                    l = mid + 1
                else:
                    r = mid 
        return nums[l]