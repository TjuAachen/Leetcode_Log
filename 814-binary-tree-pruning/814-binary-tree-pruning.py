# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def delete(root):
            if not root:
                return True
            if root.val == 0 and not root.left and not root.right:
                return True
            left, right = delete(root.left), delete(root.right)
            if left:
                root.left = None
            if right:
                root.right = None
            if left and right and root.val == 0:
                return True
            return False
        sanitel = TreeNode()
        sanitel.left = root
        delete(sanitel)
        return sanitel.left
                
        