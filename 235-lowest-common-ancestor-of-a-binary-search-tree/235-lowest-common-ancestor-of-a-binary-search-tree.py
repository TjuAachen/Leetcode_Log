# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack1, stack2 = [], []
        def find(stack, p):
            node = root
            while(node != p):
                stack.append(node)
                if node.val < p.val:
                    node = node.right
                else:
                    node = node.left
            stack.append(node)
        find(stack1,p)
        find(stack2,q)
        while(stack1 and stack2):
            first, second = stack1.pop(0), stack2.pop(0)
            
            if first == second:
                res = first
        return res
                