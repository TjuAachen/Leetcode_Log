# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root):
            if root == p or root == q or not root:
                return root
            elif not (root.left or root.right):
                return None
            left, right = helper(root.left), helper(root.right)
            if left and right:
                return root
            elif not left and right:
                return right
            elif not right and left:
                return left     
            else:
                return None
        return helper(root)
                
                
        