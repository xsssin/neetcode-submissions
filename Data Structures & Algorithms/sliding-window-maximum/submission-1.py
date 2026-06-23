from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()


        l = 0
        r = k-1

        res = [] #we document the indecies instead of th eactual number here

        for i, number in enumerate(nums):

            #if the index is outside window, 
            while queue and queue[0] <=i-k:
                queue.popleft()

            while queue and nums[queue[-1]] <=number:
                queue.pop()

            
            queue.append(i)

            if i>=k-1:
                res.append(nums[queue[0]])

        return res




        
        