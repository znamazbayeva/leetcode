class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left < right:
            mid = left + math.floor((right-left)/2)
            if mid*mid > x:
                right = mid
            elif mid*mid < x:
                left = mid+1
            else:
                return mid
        if left*left > x:
            return left - 1
        else:
            return left
# 4
# 16 > 8
# l = 0 r = 4
# mid = 2 
# 2*2 < 8 
# l = 3 r = 4
# mid = 3
# 3*3 > 9 
# r = 3
