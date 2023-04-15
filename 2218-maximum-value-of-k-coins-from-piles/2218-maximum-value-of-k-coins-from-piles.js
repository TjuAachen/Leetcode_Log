/**
 * @param {number[][]} piles
 * @param {number} k
 * @return {number}
 */

var maxValueOfCoins = function(piles, k) {
    // 实际为凑硬币问题或者部分背包问题的变种
    //从优化角度考虑为如何维护最少信息，求得后续。实际上对于此类题完全不用知道到底怎么选的。
    //只要考虑一个pile选完之后的影响即可
    
    var n = piles.length
    var dp = Array(n).fill().map(() => Array(k + 1).fill(0));
    var curSum = 0
    var ans = 0
    var i = 1
    for (var elem of piles[0]) {
        curSum += elem
        dp[0][i] = curSum
        ans = Math.max(ans, dp[0][k])
        i++
    }

    for (var i = 1; i < n; i++) {
        var pile = piles[i]
        var curSum = 0
        for (var j = 0; j < pile.length + 1; j++){
            var maxK = k - j
            if (j > 0) {
                curSum += pile[j - 1]
            }
            for (var prev = 0; prev <= maxK; prev++) {
                dp[i][j + prev] = Math.max(dp[i][j + prev], curSum + dp[i - 1][prev])
        }
        }
        ans = Math.max(ans, dp[i][k])
    }

    return ans
    
    
};