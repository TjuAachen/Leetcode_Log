class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # biggest overlapping
        word1_len, word2_len = len(word1), len(word2)
        dp = [[0] * word2_len for _ in range(word1_len)]
        res = 0
        for i in range(word2_len):
            if word1[0] == word2[i]:
                dp[0][i] = 1
                res = 1
            elif i == 0:
                dp[0][i] = 0
            else:
                dp[0][i] = dp[0][i-1]
        for i in range(word1_len):
            if word1[i] == word2[0]:
                dp[i][0] = 1
                res = 1
            elif i == 0:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0]
        
        for i in range(1, word1_len):
            for j in range(1, word2_len):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max([dp[i-1][j], dp[i][j-1], dp[i-1][j-1]])
                res = max(res, dp[i][j])
        return word1_len - 2 * res + word2_len 