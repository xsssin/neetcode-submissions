from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:


        #use a deque

        #construct the first window:
        queue = deque()
        res = []

        for i, number in enumerate(nums):


            while queue and queue[0] <= i-k:
                queue.popleft()
            

            while queue and number > nums[queue[-1]]:
                queue.pop()
            
            queue.append(i)

            if k-1 <= i :
                res.append(nums[queue[0]])

        
        return res


            
        