class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        nums_len = len(nums)
        record = dict()
        max_len = 0
        while(right < nums_len):
            if nums[right] not in record:
                record[nums[right]] = 1
            else:
                record[nums[right]] += 1
            
            while(left < right and record[nums[right]] == 2):
                if record[nums[left]] == 1:
                    del record[nums[left]]
                else:
                    record[nums[left]] = record[nums[left]] - 1
                left = left + 1
            max_len = max(max_len, sum(nums[left:right+1]))
            right = right + 1
        return max_len
            
        