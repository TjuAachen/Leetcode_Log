# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        sanitel = TreeNode(low)
        sanitel.left = root
        def delete(root):
            if not root:
                return None
            if root.val > high:
                return delete(root.left)
            if root.val < low:
                return delete(root.right)
            left = delete(root.left)
            right = delete(root.right)
            root.left = left
            root.right = right
            return root
        delete(sanitel)
        return sanitel.left
                
                    
            
        