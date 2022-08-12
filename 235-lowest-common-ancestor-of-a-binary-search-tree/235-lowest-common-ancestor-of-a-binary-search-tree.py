# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        global ancestor
        ancestor = None
        def is_p_or_q(root):
            global ancestor
            if not root:
                return False
            left = is_p_or_q(root.left)
            right = is_p_or_q(root.right)
            if not ancestor:
                if (left or right) and (root == p or root == q):
                    ancestor = root
                if left and right:
                    ancestor = root
            if left or right or root == p or root == q:
                return True
            return False
        is_p_or_q(root)
        return ancestor
        