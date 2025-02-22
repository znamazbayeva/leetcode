class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        max_len = 0
        while l < r:
            len_h = min(height[l], height[r]) * (r-l)
            max_len = max(max_len, len_h)
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        return max_len
            
        
        