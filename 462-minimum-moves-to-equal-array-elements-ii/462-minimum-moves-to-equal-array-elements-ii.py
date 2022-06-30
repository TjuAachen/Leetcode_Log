class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        subarray = [0] * (n + 1)
        for i, num in enumerate(nums):
            subarray[i+1] = subarray[i] + num
        count = float('inf')
        for i, num in enumerate(nums):
            left_decre = num * i - subarray[i]
            right_incre = subarray[-1] - subarray[i+1] - num * (n-i-1)
            count = min(count,left_decre + right_incre)
        return count
            
            
        