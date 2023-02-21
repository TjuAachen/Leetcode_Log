from bisect import *
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = nums[-1]
        
        while (left + 1 < right):
            mid = left + (right - left) // 2
            count = bisect_right(nums, mid)
            if count % 2 == 1:
                right = mid
            else:
                left = mid
        countLeft = bisect_right(nums, left)
        if countLeft % 2 == 1:
            return left
        return right
        