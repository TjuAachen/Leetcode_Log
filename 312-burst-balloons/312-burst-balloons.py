class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [[0] * (n+2) for i in range(n+2)]
        nums.append(1)
        nums = [1] + nums
        for i in range(n+1,-1,-1):
            for j in range(n+2):
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j])
        return dp[0][-1]
        
                
                    