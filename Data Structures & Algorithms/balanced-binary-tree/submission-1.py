# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(curr):

            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            if left is False or right is False:
                return False
            
            if abs(left-right) >1:
                return False

            
            return max(left, right)+1

        return dfs(root) is not False
        