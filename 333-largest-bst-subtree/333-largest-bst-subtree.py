# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        global ans
        ans = 1
        def verify(root):
            global ans
            if not root.left and not root.right:
                return root.val, root.val, 1
            left_max, right_min = -float('inf'), float('inf')
            right_max, left_min = -float('inf'), float('inf')
            left_num, right_num = 0, 0
            if root.left:
                left_max, left_min, left_num = verify(root.left)
            if root.right:
                right_max, right_min, right_num = verify(root.right)
            total_num = 0
            if  left_max < root.val and right_min > root.val and (left_num or not root.left) and (right_num or not root.right):
                total_num = left_num + right_num + 1
                ans = max(ans, total_num)
                return max(root.val,right_max), min(root.val,left_min), total_num
            ans = max(ans, total_num)
            return root.val, root.val, total_num
        verify(root)
        return ans
                
        