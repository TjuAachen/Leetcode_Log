class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        b0, b2 = 0, n-1
        i, j = 0, n-1
        while(i<=b2):
            if nums[i] == 0:
                nums[i], nums[b0] = nums[b0], nums[i]
                b0 += 1
                if nums[i] == 2:
                    nums[i], nums[b2] = nums[b2], nums[i]
                    b2 -= 1
            if nums[i] == 2:
                while(b2 > b0 and nums[b2] == 2):
                    b2 = b2 - 1
                if nums[b2] != 2 and i <= b2:
                    nums[i], nums[b2] = nums[b2], nums[i]
                    if nums[i] == 0:
                        nums[i], nums[b0] = nums[b0], nums[i]
                        b0 += 1
                b2 = b2 - 1
            i = i + 1
        return nums
            
                

                
                
        