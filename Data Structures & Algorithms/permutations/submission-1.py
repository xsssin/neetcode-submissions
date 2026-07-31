class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []


        def dfs(past_indicies, curr):
            if len(past_indicies) == len(nums):
                res.append(curr.copy())
                return
            
            if len(past_indicies)>len(nums):
                return 
            

            for j in range(len(nums)):
                if j not in past_indicies:
                
                    curr.append(nums[j])
                    past_indicies.append(j)

                    dfs(past_indicies, curr)

                    curr.pop()
                    past_indicies.pop()
        

        dfs([],[])

        return res
        