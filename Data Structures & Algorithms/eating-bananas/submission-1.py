import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #worst case of k is the # of bananas in maximum pile
        l= 1
        r = max(piles)

        while l<r:
            k = (l+r)//2

            actual_hours = 0
            for bananas in piles:
                actual_hours += math.ceil(bananas/k)

            
            if actual_hours > h:
                #which mean we have to increase k:
                l = k+1
            
            else:
                r = k
        

        return l
        


            

