class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #1.discuss by case
        #2.attach another group array to the end
        n = len(nums)
        nums.extend(nums)
        prefix = [0] * (2 * n + 1)
        
        for i in range(1, 2 * n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        queue = deque()
        queue.append([0, prefix[0]])
        ans = -float('inf')
        
        for j in range(1, 2 * n + 1):
            #[idx, prefix val]

            ans = max(ans, prefix[j] - queue[0][1])
            
            #update the queue
            while(queue and queue[-1][1] >= prefix[j]):
                queue.pop()
            while(queue and j - queue[0][0] >= n):
                queue.popleft()
            queue.append([j, prefix[j]])
        
        return ans
            
        
        