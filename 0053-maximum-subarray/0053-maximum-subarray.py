class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        monoQ = deque()
        ans = -float('inf')
        
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        
        monoQ.append(prefix[0])
        minPrefix = prefix[0]
        
        for j in range(1, n + 1):
            ans = max(ans, prefix[j] - minPrefix)
            minPrefix = min(minPrefix, prefix[j])
        
        return ans
            
            