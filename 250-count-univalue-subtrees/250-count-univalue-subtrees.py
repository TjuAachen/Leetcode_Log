# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        #record the number of nodes for each val
        global count
        count = 0
        if not root:
            return 0
        def subtree(root):
            global count
            if not root.left and not root.right:
                count += 1
                return True
            left, right = True, True
            leftval, rightval = root.val, root.val
            if root.left:
                left = subtree(root.left)
                leftval = root.left.val
            if root.right:
                right = subtree(root.right)
                rightval = root.right.val
            if left and right and leftval == rightval == root.val:
                count += 1
                return True
            return False
        subtree(root)
        return count
        
                