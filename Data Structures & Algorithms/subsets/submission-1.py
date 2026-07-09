class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i,curr):
            if i == len(nums):
                res.append(curr.copy())
                return
            
            #the choice where we include i
            curr.append(nums[i])
            dfs(i+1, curr)

            curr.pop()

            #the choid where we not include nums[i]
            dfs(i+1, curr)


        dfs(0,[])
        return res
        