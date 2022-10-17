class Solution:
    def hammingWeight(self, n: int) -> int:
        numberOf1s = 0
        n1 = 32
        while n1:
            numberOf1s = numberOf1s + 1 if n & 1 else numberOf1s
            n1 -= 1
            n >>= 1
        return numberOf1s