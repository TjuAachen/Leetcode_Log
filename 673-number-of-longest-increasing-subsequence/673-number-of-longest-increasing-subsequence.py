class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        longest = [1] * n
        
        dp = [[0] * 2 for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    longest[i] = max(longest[i], longest[j] + 1)
        for i in range(n):
            if longest[i] == 1:
                dp[i][0] = 1
                dp[i][1] = 1
        for i in range(1, n):
            for j in range(2):
                cur_length = longest[i] - j
                for k in range(i):
                    if nums[k] < nums[i]:
                        for m in range(2):
                            prev_length = longest[k] - m
                            if prev_length + 1 == cur_length:
                                dp[i][j] += dp[k][m]
        maximum = max(longest)
        ans = 0
        for i in range(n):
            if longest[i] == maximum:
                ans += dp[i][0]
        return ans
                