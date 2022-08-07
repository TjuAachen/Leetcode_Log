class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        memo = {}
        def max_score(i, j, nums):
            if (i,j) in memo: return memo[(i, j)]
            if i >= n or j < 0 or i > j:
                return 0
            #print(i, len(nums))
            maxScore = max(nums[i] - max_score(i+1, j, nums), nums[j] - max_score(i, j-1, nums))
            memo[(i,j)] = maxScore
            return maxScore
        return max_score(0, n - 1, nums) >= 0