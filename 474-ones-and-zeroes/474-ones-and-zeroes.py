class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[[0]*(n+1) for _ in range(m+1)] for _ in range(1+len(strs))]
        def generate(char):
            count0, count1 = 0, 0
            for s in char:
                if s == '0':
                    count0+= 1
                else:
                    count1+= 1
            return count0, count1
        for ind, char in enumerate(strs):
            count0, count1 = generate(char)
            ind = ind + 1
            for i in range(m+1):
                for j in range(n+1):
                    if i >= count0 and j >= count1 and ind > 0:
                        dp[ind][i][j] = max(dp[ind-1][i-count0][j-count1]+1, dp[ind-1][i][j])
                    else:
                        dp[ind][i][j] = dp[ind-1][i][j]
                            
        return dp[-1][-1][-1]
                    
            
            
        