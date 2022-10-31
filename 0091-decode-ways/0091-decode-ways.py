class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        dp = [0 for x in range(len(s) + 1)] 

        # base case initialization
        dp[0] = 1 
        dp[1] = 0 if s[0] == "0" else 1   #(1)

        for i in range(2, len(s) + 1): 
            # One step jump
            if 0 < int(s[i-1:i]) <= 9:    #(2)
                dp[i] += dp[i - 1]
            # Two step jump
            if 10 <= int(s[i-2:i]) <= 26: #(3)
                dp[i] += dp[i - 2]
        return dp[len(s)]
        # 226
        # 2 -> 1 way to decode -> B dp[0] = 1
        # 2 -> ns[2] 1 + ns[22] 1 -> 2  dp[1] = 2
        # 6 -> ns[6] 1 + ns[26] 1 -> 2  dp[2] = 2
        
        # 2         22
        # 2     26       6 (1)
        # 6 (1) (1)