class Solution:
    
    def climbStairs(self, n: int) -> int:
        if n == 1: 
            return 1
        dic = [-1 for i in range(n)]
        dic[0], dic[1]  = 1,2

        
        def helper(n, dic):
            if dic[n] < 0:
                dic[n] = helper(n-1, dic) + helper(n-2, dic)
            return dic[n]
        
        return helper(n-1, dic)