class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        arr =[0] * (n+1)
        if len(arr) >=2:
            arr[1] = 1
        for i in range(2, n+1):
            arr[i] = arr[i-2] + arr[i-1]
        return arr[-1]
        