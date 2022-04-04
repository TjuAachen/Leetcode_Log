class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0]*n
        for i in range(n):
            if s[i] == ")":
                if i > 0 and s[i-1] == "(":
                    dp[i] = dp[i-2] + 2
                elif i > 0 and s[i-1] == ")":
                    if i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == "(":
                        if i-dp[i-1]-2 >= 0:
                            dp[i] = dp[i-dp[i-1]-2] + dp[i-1] + 2
                        else:
                            dp[i] = dp[i-1] + 2
        if not dp:
            return 0
        return max(dp)
                
        