class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        smap = {}

        l = 0
        r = 0

        for r in range(len(s)):
            if s[r] in smap and smap[s[r]]>=l:
                l = smap[s[r]] +1
            
            smap[s[r]] = r
        
            max_len = max(max_len, r-l+1)
            
        
        
        return max_len
        