class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        for ind, num in enumerate(nums):
            res ^= (ind^num)
        return res
        