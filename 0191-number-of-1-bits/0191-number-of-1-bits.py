class Solution:
    def hammingWeight(self, n: int) -> int:
        # tc -> O(logn), sc -> O(1)
        numberOf1s = 0
        while n:
            numberOf1s += 1
            n = n&(n-1) # unset the rightmost bit

        # n1 = 32
        # while n1:
        #     numberOf1s = numberOf1s + 1 if n & 1 else numberOf1s
        #     n1 -= 1
        #     n >>= 1
        return numberOf1s