class Solution:
    def minWindow(self, s: str, t: str) -> str:

       

        l = 0
        r = 0

        res = [l, r]
        

        
        #construct need map
        need = {}
        for i in t:
            if i in need:
                need[i] += 1
            else:
                need[i] = 1
        
        need_count = len(need)

        
        #contruct have map
        have = {}
        for i in need.keys():
            have[i] = 0

        min_length = float("inf")
        #contruct first substring
        for r in range(len(s)):
            if s[r] in need:
                have[s[r]] += 1
            
            if s[r] in have and have[s[r]] == need[s[r]]:
                need_count -= 1
            
            while need_count == 0:
                if r-l+1 < min_length:
                    min_length = r-l+1
                    res = [l,r]

                
                if s[l] in need:
                    have[s[l]] -= 1
                
                

                if s[l] in have and have[s[l]] < need[s[l]]:
                    need_count += 1
                l += 1
                
                

            
        
        return s[res[0]: res[1]+1] if min_length != float("inf") else ""


            

            





        