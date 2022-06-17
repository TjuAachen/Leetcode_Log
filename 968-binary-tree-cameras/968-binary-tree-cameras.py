# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        #bottom-up, installed: 1, monitorer: 2
        global res
        res = 0
        head = root
        def install_cameras(root):
            global res
            if not root:
                return
            install_cameras(root.left)
            install_cameras(root.right)
            left_status, right_status = 2, 2
            if root.left:
                left_status = root.left.val
            if root.right:
                right_status = root.right.val
            if (left_status == 1 and right_status != 0) or (right_status == 1 and left_status != 0):
                root.val = 2
            elif left_status == 0 or right_status == 0:
                root.val = 1
                res += 1
            if root == head and left_status == 2 and right_status == 2:
                root.val = 1
                res += 1
        install_cameras(root)
        return res
            
        