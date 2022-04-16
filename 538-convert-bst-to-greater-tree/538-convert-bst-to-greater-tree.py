# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        used = dict()
        global add
        add = 0
        def find(root):
            global add
            if not root:
                return
            find(root.right)
            add += root.val
            root.val = add
            find(root.left)
            return            
        find(root)
        return root