# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        global ans
        ans = None
        def find(original, cloned):
            global ans
            if not original or not cloned:
                return
            if original == target:
                ans = cloned
                return 
            find(original.left, cloned.left)
            find(original.right, cloned.right)
        find(original, cloned)
        return ans
        