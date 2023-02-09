class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if n == 1:
            return 0
        
        curMax = 0
        step = 0
        prevMax = 0
        for i, num in enumerate(nums):
            curMax = max(curMax, num + i)
            if i >= prevMax and prevMax != n - 1:
                prevMax = curMax
                step += 1
            
        
        return step
        