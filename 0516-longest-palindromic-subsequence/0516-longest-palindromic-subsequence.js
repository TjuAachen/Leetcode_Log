/**
 * @param {string} s
 * @return {number}
 */
var longestPalindromeSubseq = function(s) {
    var n = s.length
    let dp = Array(n).fill().map(() => Array(n).fill(0));
    var ans = 0
    
    for (var left = n - 1; left >= 0; left--){
        for (var right = left; right < n; right++) {
            var curVal = 0
            if (left == right){
                dp[left][right] = 1
            }else if (s.charAt(left) == s.charAt(right)){
                dp[left][right] = dp[left + 1][right - 1] + 2
            }else{
                dp[left][right] = Math.max(dp[left + 1][right], dp[left][right - 1])
            }
            
        }
    }
    
    //console.log(dp)
    return dp[0][n - 1]
    
};