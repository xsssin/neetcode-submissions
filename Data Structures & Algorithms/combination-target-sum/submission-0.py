class ListNode:
    def __init__(self):
        self.children = {}
        self.isTarget = False


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if i >= len(nums) or total > target:
                return 

            #we chose to append nums[i] to current
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            #we chose not to append nums[i]
            dfs(i+1, curr, total)


        dfs(0, [], 0)

        return res



        