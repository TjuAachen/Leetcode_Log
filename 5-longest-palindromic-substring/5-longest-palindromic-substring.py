class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[True]*n for _ in range(n)]
        result = [0,0]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i >= j:
                    dp[i][j] = True
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                if dp[i][j] and result[1] - result[0] < j - i:
                    result = [i, j]
        return s[result[0]:result[1]+1]
                    
        
            
        