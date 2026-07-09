class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []



        def dfs(past_indexes, curr):
            if len(past_indexes) == len(nums):
                res.append(curr.copy())
                return
            
            if len(past_indexes) > len(nums):
                return 
            
            
            for j in range(len(nums)):
                if j not in past_indexes:
                    curr.append(nums[j])
                    past_indexes.append(j)
                    
                    dfs(past_indexes, curr)

                    past_indexes.pop()
                    curr.pop()
            

        

        dfs([],[])

        return res



        