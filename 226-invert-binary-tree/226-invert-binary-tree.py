# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(rootleft,left,rootright,right,flag):
            if left and right:
                left.val, right.val = right.val, left.val
                invert(left,left.left,right,right.right,0)
                invert(left,left.right,right,right.left,1)
            elif not left and right:
                if flag == 0:
                    rootleft.left = right
                    rootright.right = None
                else:
                    rootleft.right = right
                    rootright.left = None                    
                invert(right,right.left,right,right.right,0)
            elif not right and left:
                if flag == 0:
                    rootleft.left = None
                    rootright.right = left
                else:
                    rootleft.right = None
                    rootright.left = left                    
                invert(left,left.left,left,left.right,0)
            return
        if root:
            invert(root,root.left,root,root.right,0)
        return root
            