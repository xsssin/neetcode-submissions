class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_area = 0
        stack = []

        for i in range(len(heights)):
            #base cases

            #1. if the height is desending, we pop the top
            #of the stack while the top of the stack is higher than the new one
            #2. we insert the new element i and set its index to the lastly popped index
            #3. while doing this, we also check if (current_index- index)*popped_height > max area
            last_index = i
            while stack and heights[i] < stack[-1][1]:
                last_index, last_height = stack.pop()
                max_area = max(max_area, (i-last_index)*last_height)
            
            stack.append([last_index, heights[i]])

            

        

            #if its not desending, meaning its the same or increasint we just add the index and the height into the stack

        if stack:
            while stack:
                last_index, last_height = stack.pop()
                max_area = max(max_area, (len(heights)-last_index)*last_height)

        return max_area
                