from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0

        countmap = {}

        max_len = 0
        res =0
        max_freq = 0
        
        for r in range(len(s)):
            countmap[s[r]] = 1 + countmap.get(s[r],0)

            max_freq = max(max_freq, countmap[s[r]])

            while r-l+1 -max_freq >k:
                countmap[s[l]] -=1
                l +=1 
            
            max_len = max(max_len, r-l+1)


        return max_len

             
            

            
                

            


        