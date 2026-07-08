class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            if i >=len(nums):
                res.append(subset.copy())
                return

            #the choice to add the next node
            subset.append(nums[i])
            dfs(i+1)

            #the choice to not add the next node
            subset.pop()
            dfs(i+1)

        
        dfs(0)
        return res
        