class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j, num in enumerate(nums):
            if num != val:
                nums[i], nums[j] = nums[j], nums[i]
                i = i + 1
        return i
                
                
                
        