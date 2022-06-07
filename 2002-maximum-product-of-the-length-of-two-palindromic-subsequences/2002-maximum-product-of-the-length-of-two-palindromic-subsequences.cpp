class Solution:
    def maxProduct(self, s: str) -> int:
        length = len(s)
        num_of_case = 2**length
        
        def bit2str(number):
            i = 0
            res = []
            remove = []
            while(i < length):
                cur = (1<<i) & number
                if cur != 0:
                    res.append(s[i])
                else:
                    remove.append(s[i])
                i = i + 1
            return ''.join(res), ''.join(remove)
        def max_palindrome(s):
            n = len(s)
            if n == 0:
                return 0
            dp = [[0]*n for _ in range(n)]
            for i in range(n-1,-1,-1):
                for j in range(i,n):
                    if i == j:
                        dp[i][j] = 1
                    if i!= j and s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1]+2
                    elif i != j:
                        dp[i][j] = max(dp[i+1][j],dp[i][j-1])
            return dp[0][-1]
        final = 0
        for case in range(1, 2**length):
            str1, str2 = bit2str(case)
            final = max(final, max_palindrome(str1) * max_palindrome(str2))
        return final
            
        
        
        