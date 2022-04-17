# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        def pushLeft(node):
            while node:
                stack.append(node)
                node = node.left
        pushLeft(root)
        visited = dict()
        while stack:
            top = stack[-1]
            if top.left == None or top.left in visited:
                res.append(top.val)
                stack.pop()
                visited[top] = 1
                pushLeft(top.right)
        return res
                
        