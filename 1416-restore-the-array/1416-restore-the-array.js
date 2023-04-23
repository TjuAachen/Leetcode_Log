/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var numberOfArrays = function(s, k) {
    var MOD = 1000000007
    var n = s.length
    var dp = Array(n + 1).fill(0)
    // state: along the index n
    // recurrence: dp[i], the number of the possible arrays by selecting i digits
    dp[0] = 1
    var maxLength = k.toString().length
    
    for (var i = 1; i < n + 1; i++){
        var curVal = 0
        for (var prev = 0; prev < Math.min(i, maxLength); prev++) {
            var parsed = parseInt(s.charAt(i - prev - 1))
            if (parsed == 0)
                continue
            curVal = parsed * Math.pow(10, prev) + curVal
            
            if (curVal <= k && curVal >= 1) {
                dp[i] = (dp[i] + dp[i - prev - 1]) % MOD
            }
        }
    }
  //  console.log(dp)
    return dp[n]
};