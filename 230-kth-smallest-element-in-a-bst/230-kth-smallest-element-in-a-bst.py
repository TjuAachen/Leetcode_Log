# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        global m
        m = 1
        global res
        res = 0
        def output(root):
            global res
            global m
            if not root:
                return
            output(root.left)
            if k == m:
                res = root.val
                m += 1
                return
            else:
                m += 1
            output(root.right)
        output(root)
        return res