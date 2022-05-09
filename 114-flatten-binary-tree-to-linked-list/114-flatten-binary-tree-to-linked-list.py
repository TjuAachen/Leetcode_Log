# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        self.flatten(root.left)
        self.flatten(root.right)
        
        if root.left:
            root.left.left, root.left.right = root.left.right, root.left.left
            root.left.right = root.right
            self.flatten(root.left)
            root.right = root.left
            root.left = None
            
        