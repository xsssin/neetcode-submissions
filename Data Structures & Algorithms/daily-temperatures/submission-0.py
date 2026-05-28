class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        res = [0]*len(temperatures)

        for day_num, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]: 
                res[stack[-1][0]] = day_num - stack[-1][0]
                stack.pop()
            
            
            
            stack.append([day_num, temp])

        return res
            

             

        