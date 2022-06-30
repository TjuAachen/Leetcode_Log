class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        n = len(nums)
        for i in range(n):
            cur = nums[i]
            if i%2 == 0:
                right = float('inf')
                if 0 <= i + 1 < n:
                    right = nums[i+1]
                if cur > right:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            else:
                right = -float('inf')
                if 0 <= i + 1 < n:
                    right = nums[i+1]
                if cur < right:
                    nums[i], nums[i+1] = nums[i+1], nums[i]   
        
                
        