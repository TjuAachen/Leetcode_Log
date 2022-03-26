# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root):
            if not root:
                return (2**31,-2**31-1,True)
            val_left, val_right=validate(root.left),validate(root.right)
            if val_left[2] and val_right[2]:
                if root.left and root.left.val >= root.val:
                    return (0,0,False)
                if root.right and root.right.val <= root.val:
                    return (0,0,False)
                if val_left[1] >= root.val:
                    return (0,0,False)
                if val_right[0] <= root.val:
                    return (0,0,False)
                m, n = 2**31, -2**31-1
                if root.left:
                    m = root.left.val
                if root.right:
                    n = root.right.val
                return(min(val_left[0],m),max(val_right[1],n),True)
                
            return (0,0,False)
        return validate(root)[2]
                
        