# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def generate(array):
            if not array:
                return None
            if len(array) == 1:
                return TreeNode(array[0])
            med_pos = len(array)//2
            left_array, right_array = array[:med_pos], array[med_pos+1:]
            left, right= generate(left_array), generate(right_array)
            root = TreeNode(array[med_pos])
            root.left, root.right = left, right
            return root
        return generate(nums)
        