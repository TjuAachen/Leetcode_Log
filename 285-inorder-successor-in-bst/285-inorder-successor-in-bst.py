# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        global ans, res
        res = None
        ans = None
        def find(root):
            global ans, res
            if not root:
                return
            find(root.left)
            if res != p.val:
                res = root.val
            else:
                ans = root
                res = root.val
                return
            find(root.right)
        find(root)
        return ans