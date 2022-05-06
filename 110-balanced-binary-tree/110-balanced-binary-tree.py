# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        node_height = dict()
        def height(root):
            if root in node_height:
                return node_height[root]
            if not root:
                return 0
            node_height[root] = max(height(root.left),height(root.right))+1
            return node_height[root]
        def is_balanced(root):
            if not root:
                return True
            left_height, right_height = height(root.left), height(root.right)
            if abs(left_height - right_height) > 1:
                return False
            return is_balanced(root.left) and is_balanced(root.right)
        return is_balanced(root)
            
            
        