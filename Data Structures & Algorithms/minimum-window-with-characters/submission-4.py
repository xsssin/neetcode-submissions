class Solution:
    def minWindow(self, s: str, t: str) -> str:

        #edge case:

        res = [-1,-1]

        need_map = {}

        #build need map
        for letter in t:
            need_map[letter] = 1+ need_map.get(letter, 0)

        have_map = {}
        #build have_map
        for key in need_map.keys():
            have_map[key] = 0
        
        print(have_map)

       

        reslen = float("inf")
        need = len(need_map)
        have = 0
        #build initial substring

        l = 0
        for r in range(len(s)):
            #outside while loop:
            #we increment r until need == have
            if s[r] in need_map:
                have_map[s[r]] += 1
            
            if s[r] in need_map and have_map[s[r]] == need_map[s[r]]:
                have += 1
        
            while need == have:
                #shrink left
                if r-l+1 < reslen:
                    res = [l,r]
                    reslen = r-l+1
            
                if s[l] in need_map:
                    have_map[s[l]] -= 1
                if s[l] in need_map and have_map[s[l]] < need_map[s[l]]:
                    have -= 1
                

                
                l+= 1
            
            
        print(res[0])
        return s[res[0]:res[1]+1] if reslen != float("inf") else  ""
            

            





        