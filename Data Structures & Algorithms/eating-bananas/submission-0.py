class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_b = 1
        max_b = max(piles)

        while min_b < max_b:
            b = (max_b+min_b)//2

            total = 0
            for pile in piles:
                total += math.ceil(pile/b)
            
            if total >h:
                min_b = b+1
            else:
                max_b = b
            

        return min_b

        

        