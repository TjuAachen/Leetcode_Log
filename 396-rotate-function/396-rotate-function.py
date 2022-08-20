class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        
        prefix_sum = [0] * (n + 1)
        
        F = [0] * n
        total_sum = sum(nums)
        for i in range(1, n+1):
           # prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
            F[0] += (i-1)*nums[i-1]
        res = F[0]
        for j in range(1, n):
            
            F[j] = F[j-1] - (total_sum - nums[j-1]) + (n-1) * nums[j-1]
            res = max(res, F[j])
        return res