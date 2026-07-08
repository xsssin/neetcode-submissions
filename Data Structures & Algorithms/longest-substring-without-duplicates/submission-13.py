class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        letter_map = {}


        l = 0
        r = 0

        while r < len(s):
            if s[r] not in letter_map:
                letter_map[s[r]] = r
                max_len = max(max_len, r-l+1)
            
            else:
                #letter_map[s[r]] = r 
                l = max(l, letter_map[s[r]]+1)
                letter_map[s[r]] = r
                max_len = max(max_len, r-l+1)
            r +=1
        

        return max_len




        