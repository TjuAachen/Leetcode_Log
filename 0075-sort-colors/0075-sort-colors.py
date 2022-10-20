class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pointer2 = n - 1
        pointer0 = 0
        i = 0
        
        while(i <= pointer2):
            curNum = nums[i]
            if curNum == 0:
                nums[pointer0], nums[i] = nums[i], nums[pointer0]
                pointer0 += 1
                i += 1
            elif curNum == 1:
                i += 1
            else:
                nums[pointer2], nums[i] = nums[i], nums[pointer2]
                pointer2 -= 1
        
                
        
            
            
                    
                
                

            