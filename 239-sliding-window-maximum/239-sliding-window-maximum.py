class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []
        result = []
        for i in range(len(nums)):
            while(queue and nums[queue[0]]<=nums[i]):
                    queue.pop(0)
            while(queue and nums[queue[-1]]<=nums[i]):
                    queue.pop()
            if i >= k-1:
                if queue and queue[0] < i - k + 1:
                    queue.pop(0)
                
            queue.append(i)
            if i >= k-1:
                result.append(nums[queue[0]])
        return result
            
                
                
            
            