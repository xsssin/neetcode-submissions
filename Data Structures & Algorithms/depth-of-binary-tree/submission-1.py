# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_d = 0


        def dfs(node,curr):
            if not node:
                return 0
            self.max_d = max(self.max_d, curr)
            dfs(node.left, curr+1)
            dfs(node.right,curr+1)
        
        
        dfs(root, 1)
        return self.max_d

            

            
        