/**
 * @param {string} s
 * @return {number}
 */
var minInsertions = function(s) {
    var n = s.length
    var dp = Array(n).fill().map(() => Array(n).fill(0))

    for (let i = n - 1; i >= 0; i--)
        for (let j = i + 1; j < n; j++) {
            var iChar = s.charAt(i)
            var jChar = s.charAt(j)
            
            if (iChar == jChar) {
                dp[i][j] = dp[i + 1][j - 1]
                continue
            }
            dp[i][j] = Math.min(dp[i][j - 1] + 1, dp[i + 1][j] + 1)
        }
    
    return dp[0][n - 1]
};