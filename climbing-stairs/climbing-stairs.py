class Solution(object):
    memo = {}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        if n == 0:
            return 1
        if n-1 not in self.memo:
            self.memo[n-1]= self.climbStairs(n-1)
        if n-2 not in self.memo:
            self.memo[n-2] = self.climbStairs(n-2)
        return self.memo[n-1] + self.memo[n-2]
        