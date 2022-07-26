# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        global commonAncestor
        commonAncestor = None
        def find_ancestor(root):
            global commonAncestor
            if not root:
                return False
            left = find_ancestor(root.left)
            right = find_ancestor(root.right)
            if left and right:
                commonAncestor = root
                return False
            if (left and not right) or (not left and right):
                if p == root or q == root:
                    commonAncestor = root
                    return False
                return True
            if p == root or q == root:
                return True
            return False
        find_ancestor(root)
        
        return commonAncestor
        
            
            
        
                
                
        