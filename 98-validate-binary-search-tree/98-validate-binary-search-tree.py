# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        #inorder traversal
        cur = root
        res = []
        while(cur or stack):
            while(cur):
                stack.append(cur)
                cur = cur.left
            popped = stack.pop()
            if popped and res and res[-1].val >= popped.val:
                return False
            res.append(popped)
            cur = popped.right
        return True