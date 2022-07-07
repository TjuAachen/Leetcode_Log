# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global diameter
        diameter = 0
        def find_diameter(root):
            global diameter
            if not root:
                return -1
            left = find_diameter(root.left)
            right = find_diameter(root.right)
            temp = (max(left,right) + 1)
            diameter = max(diameter, left+right+2)
            return temp
        find_diameter(root)
        return diameter