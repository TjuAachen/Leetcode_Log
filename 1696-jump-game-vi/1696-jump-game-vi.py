class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        max_value = 0
        heap = []
        heapify(heap)
        for i in range(min(k+1, n)):
            if heap:
                max_value, _ = heap[0]
                max_value = - max_value
            dp[i] += max_value + nums[i]
            heappush(heap,[-dp[i], i])
        for i in range(min(k+1,n), n):
            while heap and heap[0][1] < i - k:
                heappop(heap)
            max_value, _ = heap[0]
            dp[i] = -max_value + nums[i]
            heappush(heap,[-dp[i], i])
        return dp[-1]
            
        