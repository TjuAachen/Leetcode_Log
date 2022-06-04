# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        global head
        if not root:
            return root
        def upside_down(root):
            global head
            if not root.left and not root.right:
                head = root
                return
            upside_down(root.left)
            if root.left:
                root.left.left = root.right
                root.left.right = root
                root.left = None
                root.right = None
        upside_down(root)
        return head
        