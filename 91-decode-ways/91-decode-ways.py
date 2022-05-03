class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*n
        flag = True
        if s[0] == '0':
            return 0
        for ind, char in enumerate(s):
            if char != '0' and ind == 0:
                dp[ind] = 1
            elif char == '0':
                if s[ind-1] == '1' or s[ind-1] == '2':
                    if ind > 1:
                        dp[ind] = dp[ind-2]
                    else:
                        dp[ind] = 1
                else:
                    dp[ind] = 0
            elif char != '0' and ind != 0:
                if ind > 1:
                    if (s[ind-1] == '2' and s[ind] < '7') or (s[ind-1] == '1'):
                        dp[ind] = dp[ind-1] + dp[ind-2]
                    else:
                        dp[ind] = dp[ind-1]
                else:
                    if (s[ind-1] == '2' and s[ind] < '7') or (s[ind-1] == '1'):
                        dp[ind] = dp[ind-1] * 2
                    else:
                        dp[ind] = dp[ind-1]
        return dp[-1]
                    