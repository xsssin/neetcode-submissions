class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        min_len = float('inf')

        need = {}
        for letter in t:
            if letter in need:
                need[letter] +=1 
            else:
                need[letter] = 1

        
        have = {}
        for key in need.keys():
            have[key] = 0
        
        l = r =0

        need_len = len(need)

        #construct base input
        while r <len(s):
            if have and s[r] in have:
                have[s[r]] += 1
                if have[s[r]] == need[s[r]]:
                        need_len -= 1
            
            while need_len == 0:
                
                if r-l+1 < min_len:
                    min_len = r-l+1
                    res = s[l:r+1]
                if s[l] in have:
                    have[s[l]] -= 1
                    if have[s[l]] < need[s[l]]:
                        need_len += 1
                l+=1
            r+=1
        

        

        return res
            
            


        