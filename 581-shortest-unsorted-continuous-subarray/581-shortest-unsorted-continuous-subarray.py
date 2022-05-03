class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prev_min,prev_max=10**5+1, -10**5-1
        leftmost, rightmost = n-1,0
        for ind, num in enumerate(nums):
            if num < prev_max:
                leftmost = min(leftmost,ind)
                rightmost = max(rightmost,ind)
            prev_max = max(prev_max,num)
        for i in range(n-1,-1,-1):
            if nums[i] > prev_min:
                leftmost = min(leftmost,i)
                rightmost = max(rightmost,i)
            prev_min = min(prev_min, nums[i])
        if leftmost == n-1 and rightmost == 0:
            return 0
        else:
            return (rightmost - leftmost+1)
            
                    
            
        