from heapq import *
class Solution(object):
    def kSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxSum = 0
        for i, num in enumerate(nums):
            if num <= 0:
                nums[i] = -nums[i]
            else:
                maxSum += num
        
        nums.sort()
        res = [maxSum]
        heap = []
        n = len(nums)
        heappush(heap, [nums[0], 0])
        while(k > 1):
            curVal, index = heappop(heap)
            if index < n - 1:
                heappush(heap, [curVal - nums[index] + nums[index + 1], index + 1])
                heappush(heap, [curVal + nums[index + 1], index + 1])
            res.append(maxSum - curVal)
            k -= 1
        return res[-1]
            
            
        
        
        
        
        