class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-1,-1,-1):
            maxIndex = i
            for j in range(i):
                if nums[j] > nums[maxIndex]:
                    maxIndex = j
            nums[i], nums[maxIndex] = nums[maxIndex], nums[i]
        return nums
        