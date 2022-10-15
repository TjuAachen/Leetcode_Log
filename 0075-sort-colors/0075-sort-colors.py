class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pointer01, pointer2 = 0, n - 1
        pointer0 = 0
        i = 0
        while(i <= pointer2):
            curNum = nums[i]
            if curNum == 2:
                nums[i], nums[pointer2] = nums[pointer2], nums[i]
                pointer2 -= 1
            if curNum == 1:
                i += 1
            if curNum == 0:
                nums[i], nums[pointer0] = nums[pointer0], nums[i]
                pointer0+= 1
                i += 1
            
            
                    
                
                

            