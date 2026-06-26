class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
      l = 1
      r = max(piles)


      while l < r:
        mid = (l+r)//2


        total_time = 0
        for pile in piles:
          total_time += math.ceil(pile/mid)

        
        if total_time > h:
          #means need to eat more
          l = mid+1
        
        else:
          r = mid
      

      return l

     