# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxRes = -float('inf')
        self.findMax(root)
        
        return self.maxRes
    
    def findMax(self, root):
        if not root.left and not root.right:
            temp = max(0, root.val)
            self.maxRes = max(root.val, self.maxRes)
            return temp
        leftMax = 0
        rightMax = 0
        if root.left:
            leftMax = max(leftMax, self.findMax(root.left))
        if root.right:
            rightMax = max(rightMax, self.findMax(root.right))
        self.maxRes = max(self.maxRes, leftMax + rightMax + root.val)
        return max(leftMax, rightMax) + root.val