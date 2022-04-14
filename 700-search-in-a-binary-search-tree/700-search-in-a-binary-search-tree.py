# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def find(root):
            if not root:
                return None
            if root.val > val:
                return find(root.left)
            elif root.val < val:
                return find(root.right)
            else:
                return root
        return find(root)
    
        