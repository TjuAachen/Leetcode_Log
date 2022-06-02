# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        global res, final
        res = 0
        final = 0
        def dfs(root):
            global res, final
            if not root.left and not root.right:
                final += res * 10 + root.val
                return
            res = res * 10 + root.val
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            res = (res - root.val) // 10
        dfs(root)
        return final