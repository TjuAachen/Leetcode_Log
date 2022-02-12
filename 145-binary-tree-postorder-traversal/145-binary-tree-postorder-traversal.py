# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        res = []
        visited = dict()
        def downLeft(node):
            while(node.left and node.left not in visited):
                node = node.left
            return node
        while stack:
            top = stack[-1]
            leftmost=downLeft(top)
            if not leftmost.right or leftmost.right in visited:
                res.append(leftmost.val)
                visited[leftmost] = 1
                if leftmost == top:
                    stack.pop()
            else:
                if leftmost != top:
                    stack.append(leftmost)
                stack.append(leftmost.right)
        return res
                
                
            
        