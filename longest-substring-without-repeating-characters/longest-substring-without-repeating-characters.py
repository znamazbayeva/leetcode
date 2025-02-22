class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        occ = defaultdict(int)
        if len(s) == 0 or len(s) == 1:
            return len(s)
        j = 0
        occ[s[j]] = j
        max_len = 1
        for i in range(1, len(s)):
            if s[i] in occ:
                m = occ[s[i]]
                while j != occ[s[i]] and j < len(s):
                    del occ[s[j]]
                    j += 1
                j += 1
            max_len = max(max_len, i - j + 1)
            occ[s[i]] = i
        return max_len
                
            
            
            
        
        
        
        