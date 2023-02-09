class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        
        i = 0
        for j in range(n):
            #eliminate the one which cannot reach j
            while (i < j and i + nums[i] < j):
                i += 1
            if i < j:
                dp[j] = dp[i] + 1
        
        return dp[n - 1]
        