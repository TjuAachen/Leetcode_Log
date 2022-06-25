class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.append(float('inf'))
        nums = [-float('inf')] + nums
        n = len(nums) - 1
        count = 0
        index = -1
        for i, num in enumerate(nums):
            if 0 < i and nums[i-1] > nums[i]:
                count += 1
                index = i
            if count > 1:
                return False
        if nums[index-2] <= nums[index] or nums[index-1] <= nums[index+1]:
            return True
        return False
                
        