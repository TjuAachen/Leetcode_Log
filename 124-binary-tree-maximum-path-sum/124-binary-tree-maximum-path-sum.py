# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global res
        res = float('-inf')
        def maxGain(node):
            global res 
            if not node:
                return 0
            left = node.left
            right = node.right
            maxleft = max(maxGain(left),0)
            maxright = max(maxGain(right),0)
            res = max(res,max(maxleft,0)+max(maxright,0)+node.val)
            return max(maxleft,maxright)+node.val
        maxGain(root)
        return res
                
        