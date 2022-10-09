# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.head = root
        self.target = k
        return self.findRes(root, k)
    def findRes(self, root, k):
        if not root:
            return False
        if self.findNum(self.head, self.target - root.val, root):
            return True
        return self.findRes(root.left, k) or self.findRes(root.right, k)
    
    
    def findNum(self, root, target, selected):
        if not root:
            return False
        if root.val == target and root != selected:
            return True
        if root.val < target:
            return self.findNum(root.right, target, selected)
        return self.findNum(root.left, target, selected)
        