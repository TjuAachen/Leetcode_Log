# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        global max_length
        max_length = 0
        def maximum_len(root):
            global max_length
            if not root.right and not root.left:
                max_length = max(max_length,1)
                return 1
            left, right = 0, 0
            if root.right:
                value = maximum_len(root.right)
                if root.right.val - root.val == 1:
                    right = value
            if root.left:
                value2 = maximum_len(root.left)
                if root.left.val - root.val == 1:
                    left = value2
            max_length = max(max_length, max(left,right) + 1)
            return max(left,right) + 1
        maximum_len(root)
        return max_length