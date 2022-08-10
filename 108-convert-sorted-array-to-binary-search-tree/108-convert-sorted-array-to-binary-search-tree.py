# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def constructBST(nums):
            if not nums:
                return None
            n = len(nums)
            median = nums[n//2]
            
            root = TreeNode(median)
            left = constructBST(nums[:n//2])
            right = constructBST(nums[n//2+1:])
            root.left = left
            root.right = right
            return root
        return constructBST(nums)
    
        