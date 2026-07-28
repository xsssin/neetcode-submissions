class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}

        def dfs(i, total):
            if i == len(nums) and total == target:
                return 1
            if i == len(nums) and total !=target:
                return 0 
            if i>= len(nums):
                return
            
            if (i, total) in dp:
                return dp[(i, total)]

            total1 = dfs(i+1, total+nums[i])
            total2 = dfs(i+1, total-nums[i])



            dp[(i, total)] = total1+total2

            return dp[(i, total)]

        
        return dfs(0,0)


            


        