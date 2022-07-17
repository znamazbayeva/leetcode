class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)-1
        while(left<=right):
            if nums[left] == target or nums[right] == target:
                return True
            left = left + 1
            right = right-1
        return False
    #O(n/2) n/2 operations in every case
#         # if len(nums) == 1 and nums[0] == target:
#         #     return True
#         while left <= right:
#             while left+1 <= right and nums[left] == nums[left+1]:
#                 left = left + 1
#             while right-1 >= 0 and nums[right] == nums[right-1]:
#                 right = right-1
#             mid = left + (right-left)//2
#             print(nums[mid], mid, left, right)
#             if nums[mid] == target:
#                 return True
#             elif nums[left] <= nums[mid]:
#                 if nums[mid] >= target and nums[left] <= target:
#                     right = mid-1
#                 else:
#                     left = mid +1
#             else:
#                 if nums[mid] <= target and nums[right] >= target:
#                     left = mid +1
#                 else:
#                     right = mid-1
# O(n)- worst case = duplicates
# O(logn) - best case = no duplicates
                    
                    
        return False
    
# nums = [2,5,6,0,0,1,2], target = 6
# l = 0, r = 6, mid = 3
# nums[l] 2 < target 6
# 2 < 6 < 2 nums[left] <= target and nums[right] >= target: not true
# right = mid -1  = 2
# l =0, r = 2, mid = 1
# 5 < 6
# 2 <= 6 <= 6 nums[left] <= target and nums[right] >= target: true
# left = mid+1 = 1
# l = 1 right = 2, 
                
        
        