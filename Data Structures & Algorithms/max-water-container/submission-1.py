class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l = 0
        r = len(heights)-1

        while l<r:
            new = (r-l)*min(heights[l], heights[r])

            max_water = max(max_water, new)

            if heights[l] <= heights[r]:
                l+= 1
            else:
                r-=1
            
        
        return max_water




        