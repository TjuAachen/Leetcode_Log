class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp=[[True]*len(s) for _ in range(len(s))]
        res =[0,0]
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                dp[i][j] = (i==j) or (s[i] == s[j] and dp[i+1][j-1])
                if dp[i][j] and res[1]-res[0] < j - i:
                    res = [i,j]
        return s[res[0]:res[1]+1]
    
                    
        
            