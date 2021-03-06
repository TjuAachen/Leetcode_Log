class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        nums_len = len(nums)
        
        #calculate the prefix sum
        
        cur_sum = 0
        min_length = float('inf')
        #right is exclusive
        while(right < nums_len):
            cur_sum += nums[right]
            right += 1
            while(left < right and cur_sum >= target):
                cur_sum = cur_sum - nums[left]
                min_length = min(min_length, right - left)
                left = left + 1
        if min_length == float('inf'):
            return 0
        return min_length
        