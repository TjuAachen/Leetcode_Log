class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def max_score(nums):
            if not nums:
                return 0
            maxScore = max(nums[0] - max_score(nums[1:]), nums[-1] - max_score(nums[:-1]))
            return maxScore
        return max_score(nums) >= 0