class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i, num in enumerate(nums):
            if num != 0:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                j = j+1
        
                
        