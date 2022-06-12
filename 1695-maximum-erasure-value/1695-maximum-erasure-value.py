class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        nums_len = len(nums)
        record = dict()
        max_len = 0
        cur_sum = 0
        while(right < nums_len):
            while(left < right and nums[right] in record):
                del record[nums[left]]
                cur_sum = cur_sum - nums[left]
                left = left + 1
            record[nums[right]] = 1
            cur_sum += nums[right]
            max_len = max(max_len, cur_sum)
            right = right + 1
        return max_len
            
        