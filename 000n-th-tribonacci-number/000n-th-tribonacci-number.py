class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        def dp(i):
            if i == 0:
                memo[0] = 0
            elif i == 1 or i == 2:
                memo[i] = 1
            elif i not in memo:
                memo[i] = dp(i-1) + dp(i-2) + dp(i-3)
            return memo[i]
        
        return dp(n)
                
        