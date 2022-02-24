class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)
        result = [-1]*2
        if not nums:
            return result
        while(left < right):
            mid = left + (right - left)//2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if 0<=left < len(nums) and nums[left] == target:
            result[0] = left
        left, right = 0, len(nums) 
        while(left < right):
            mid = left + (right - left)//2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if 0<= left-1 < len(nums) and nums[left-1] == target:
            result[1] = left-1
        return result
        
        
            