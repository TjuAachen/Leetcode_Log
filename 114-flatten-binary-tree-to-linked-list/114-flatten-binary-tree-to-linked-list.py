# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        stack = []
        tail = dict()
        def pushLeft(root):
            pointer = root
            while(pointer):
                stack.append(pointer)
                pointer = pointer.left
        visited = dict()
        pushLeft(root)
        while(stack):
            top = stack[-1]
            if (not top.left or top.left in visited) and top.right not in visited:
                pushLeft(top.right)
                if top.left:
                    tail[top] = tail_node
            if not top.right or top.right in visited:
                if not top.left and not top.right:
                    tail_node = top
                stack.pop()
                visited[top] = 1
                if top.left and top.right:
                    tail_left = tail[top]
                    tail_left.right = top.right
                    top.right = top.left
                    top.left = None
                elif not top.right:
                    top.right = top.left
                    top.left = None
            

                
                
        