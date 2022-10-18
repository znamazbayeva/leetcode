class Solution:
    def getSum(self, a: int, b: int) -> int:
        c = 0
        # 32 bit mask in hexadecimal
        mask = 0xffffffff

        while (b&mask) >  0:
            c = (a&b)<<1
            a = a^b
            b = c
        return (a&mask) if b > 0 else a
        # remainder = 0
        # ans = 0
        # while a or b:
        #     sum = a ^ b ^ remainder
        #     if sum == 0:
        #         remainder = 1
        #         ans <<= 1
        #     else:
        #         remainder = 0
        #         ans <<= 1
        #         ans = ans | 1
        #     a >>= 1
        #     b >>= 1
        # return ans
        
                