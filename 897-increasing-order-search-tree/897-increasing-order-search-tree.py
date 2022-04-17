# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res = TreeNode()
        global p
        p = res
        def order(root):
            global p
            if not root:
                return None
            order(root.left)
            p.right = root
            root.left = None
            p = p.right
            order(root.right)
        order(root)
        return res.right
        