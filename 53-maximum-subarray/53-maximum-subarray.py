class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(side):
            total = 0
            res = 0
            for ind in  range(len(side)-1,-1,-1):
                total += side[ind]
                res = max(res, total)
            return res
        def find(nums):
            if not nums:
                return -10**4-1
            mid = len(nums)//2
            left_side = nums[:mid]
            right_side = nums[mid+1:]
            left_best_sum, right_best_sum = 0, 0
            if left_side:
                left_best_sum = helper(left_side)
            if right_side:
                right_best_sum = helper(right_side[::-1])
            mid_best = nums[mid] + left_best_sum + right_best_sum
            return max(mid_best, find(left_side), find(right_side))
        return find(nums)
                
            
        