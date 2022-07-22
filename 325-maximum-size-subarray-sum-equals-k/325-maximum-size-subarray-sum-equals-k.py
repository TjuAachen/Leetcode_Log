class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        
        record = defaultdict(list)
        
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
            record[prefix_sum[i]].append(i) 
        
        maximum = 0
        for i in range(n):
            target = k + prefix_sum[i]
            if target not in record:
                continue
            right = record[target][-1]
            if right >= i:
                maximum = max(maximum, right - i)
        return maximum
        