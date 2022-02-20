# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def path(node,pathsum):
            if not node:
                return False
            if not(node.left or node.right):
                if pathsum +node.val == targetSum:
                    return True
                return False
            return path(node.left,pathsum+node.val) or path(node.right,pathsum+node.val)
        return path(root,0)
                
                
            
                
        