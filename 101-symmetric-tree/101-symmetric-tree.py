# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def mirror(left, right):
            if (not left and right) or (not right and left):
                return False
            if not left and not right:
                return True
            if left and right:
                if left.val != right.val:
                    return False
                elif left != right:
                    return (mirror(left.left, right.right) and mirror(left.right,right.left))
                else:
                    return mirror(left.left,right.right)
        return mirror(root,root)
        
            