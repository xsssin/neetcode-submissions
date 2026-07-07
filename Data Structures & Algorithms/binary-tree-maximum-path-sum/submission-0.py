# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = [root.val]

        def dfs(node):
            #1. calculate curve node and not return it, only update it to know if it is larger thanre


            #2 calculate return val
            if not node:
                return 0

            new_left = dfs(node.left)
            new_right = dfs(node.right)

            newl= max(new_left, 0)
            newr = max(new_right, 0)

            res[0] = max(res[0], node.val+newl+newr)

            return node.val + max(newl, newr)

        
        dfs(root)




        return res[0]

            

        