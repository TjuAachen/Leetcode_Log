class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        remaining = sum(nums) - x
        left, right = 0, 0
        nums_len = len(nums)
        
        prefix_sum = [0] * (nums_len + 1)
        
        for i in range(1, nums_len + 1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i - 1]
        
        min_num = float('inf')
        if remaining == 0:
            return nums_len
        while(right < nums_len):
            cur = prefix_sum[right + 1] - prefix_sum[left]
            
            #when left needs shrinking
            while(left < right and cur > remaining):
                left = left + 1
                cur = prefix_sum[right + 1] - prefix_sum[left]
            if cur == remaining:
                min_num = min(min_num, left + nums_len - 1 - right)
            right = right + 1
        if min_num == float('inf'):
            return -1
        return min_num
                
            
            
            