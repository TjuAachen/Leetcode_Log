/**
 * @param {string[]} words
 * @param {string} target
 * @return {number}
 */
var numWays = function(words, target) {
    var n = words.length
    var targetLen = target.length
    var ans = 0
    var MOD = 1000000007
    var wordLen = words[0].length
    

    var colCnt = Array(wordLen).fill().map(() => Array(26).fill(0))
    
    for (var col = 0; col < wordLen; col++){
        for (var row = 0; row < n; row++) {
            var curCharcode = words[row].charCodeAt(col) - 'a'.charCodeAt(0)
            colCnt[col][curCharcode] += 1
        }
    }
    
    
 //   console.log(colCnt)
    var dp = Array(wordLen).fill().map(() => Array(targetLen + 1).fill(0))
    
    for (var i = 0; i < wordLen; i++)
        dp[i][0] = 1
    
    
    for (var i = 0; i < wordLen; i++){
        for (var j = 1; j < Math.min(i + 2, targetLen + 1); j++) {
            if (i > 0)
                dp[i][j] += dp[i - 1][j]
            
            var targetCharCode = target.charCodeAt(j - 1) - 'a'.charCodeAt(0)
            if (i == 0){
                dp[i][j] = (dp[i][j] + colCnt[i][targetCharCode]) % MOD
            }else{
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] * colCnt[i][targetCharCode]) % MOD
            }
        }
    }

    //console.log(dp, colCnt)
    return dp[wordLen - 1][targetLen]
    
};