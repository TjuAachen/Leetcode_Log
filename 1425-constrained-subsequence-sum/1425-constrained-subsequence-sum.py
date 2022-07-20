from heapq import *
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        heap = []
        heapify(heap)
        
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        heappush(heap, [-dp[0], 0])
        res = dp[0]
        for i in range(1,n):            
            while(-heap[0][1] + i > k):
                heappop(heap)
            dp[i] = max(nums[i],-heap[0][0] + nums[i])
            heappush(heap, [-dp[i], i])
            res = max(res, dp[i])
        return res