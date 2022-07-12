class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = math.floor((left + right)/2)
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid
            print(mid, right, left)
        return left + k
#[2,3,4,7,11]
#[1,1,1,3,6] mid = 2 < 5 l = 3
# 0,1,2,3,4
#[3,6] mid = 3 < 5 l = 4
# 3,4
# 4+ 5 = 9

        