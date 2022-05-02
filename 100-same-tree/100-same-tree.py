# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def isEqual(p,q):
            if (not p and q) or (not q and p):
                return False
            if not p and not q:
                return True
            if p.val != q.val:
                return False
            else:
                return (isEqual(p.left,q.left) and isEqual(p.right, q.right))
        return isEqual(p,q)
        