import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #worst case of k is the # of bananas in maximum pile
        l= 1
        r = max(piles)

        while l<r:
            k = (l+r)//2

            actual_hours = 0
            actual_hours += sum(math.ceil(bananas/k) for bananas in piles)

            
            if actual_hours > h:
                #which mean we have to increase k:
                l = k+1
            
            else:
                r = k
        

        return l
        


            

