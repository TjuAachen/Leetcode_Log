class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        left, right = 0, n - 1
        res = [-1, -1]
        #find the left most
        while(left <= right):
            mid = left + (right - left) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid-1] != target:
                    res = [mid, mid]
                    break
                else:
                    right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        #find the rightmost
        if res[0] == -1:
            return [-1,-1]
        start, end = res[0], n - 1
        while(start < end and nums[start + 1] == target):
            start += 1
        return [res[0], start]
            