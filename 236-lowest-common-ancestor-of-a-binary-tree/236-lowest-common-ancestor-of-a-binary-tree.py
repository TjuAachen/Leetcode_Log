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
        stackp, stackq =[], []
        final = []
        def find(root ,p, stack):
            if not root:
                return
            if root != p:
                stack.append(root)
            else:
                stack.append(root)
                final.append(stack[:])
                return
            find(root.left, p, stack)
            find(root.right,p,stack)
            stack.pop()
            return
        find(root,p,stackp)
        find(root,q,stackq)
        stackp, stackq = final[0], final[1]
        while(stackp and stackq):
            first, second = stackp.pop(0), stackq.pop(0)
            if first == second:
                res = first
        return res
            
        

            
        