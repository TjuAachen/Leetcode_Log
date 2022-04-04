class Solution:
    def findMin(self, nums: List[int]) -> int:
        end = len(nums) - 1
        left, right = 0, end
        if nums[left] < nums[right]:
            return nums[left]
        while(left < right):
            mid = left + (right - left) // 2
            pivot = nums[mid]
            if pivot > nums[right]:
                left = mid + 1
            elif pivot < nums[right]:
                right = mid
            else:
                right = right - 1
        return nums[left]
                    
                    
                    
                    
                    
                    
                    
                