class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        end = len(nums) - 1
        pos = -10
        for i in range(end, -1, -1):
            if i == end:
                prev = nums[end]
            elif prev <= nums[i]:
                prev = nums[i]
            else:
                j = i + 1
                while(j <= end and nums[j] > nums[i]):
                    j = j + 1
                if j<= end and nums[j] > nums[i]:
                    pos = j
                else:
                    pos = j - 1
                break
        if pos == -10:
            nums.sort()
        else:
            nums[i], nums[pos] = nums[pos], nums[i]
            nums[i+1:] = sorted(nums[i+1:])
        
                
            
                
        