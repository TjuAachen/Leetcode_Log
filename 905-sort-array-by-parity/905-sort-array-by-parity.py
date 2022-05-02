class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        for ind, num in enumerate(nums):
            if num%2 == 0:
                nums[ind], nums[i] = nums[i], nums[ind]
                i += 1
        return nums
        