from bisect import *
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        ans = 0
        while(left <= right and nums[left] <= target):
            right_value  = target - nums[left]
            
            right = bisect_right(nums, right_value, left, right+1) - 1
           # print(left, right, right_value)
            if right < left:
                break
            ans += (1<<(right - left))
            left += 1
        return ans%(10**9+7)
            
        