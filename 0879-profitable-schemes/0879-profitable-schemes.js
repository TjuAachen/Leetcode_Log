/**
 * @param {number} n
 * @param {number} minProfit
 * @param {number[]} group
 * @param {number[]} profit
 * @return {number}
 */


var profitableSchemes = function(n, minProfit, group, profit) {
    //number of schemes
    // n max resource
    // group resource available
    var groupLen = group.length
    var maxNum = n
    var MOD = 1000000007
    var dp = Array(groupLen).fill().map(() => Array(minProfit + 1).fill().map(() => Array(maxNum + 1).fill(0)))
    // when groupLen == 0
    for (var curMinProfit = 0; curMinProfit < minProfit + 1; curMinProfit++)
        for(var curMaxNum = 0; curMaxNum < maxNum + 1; curMaxNum++) {
            if (curMinProfit == 0)
                dp[0][curMinProfit][curMaxNum] += 1
            if (curMaxNum >= group[0] && curMinProfit <= profit[0])
                dp[0][curMinProfit][curMaxNum] += 1
        }
    
    // when index > 0
    for (var index = 1; index < groupLen; index++) {
        for (var curMinProfit = 0; curMinProfit < minProfit + 1; curMinProfit++)
            for(var curMaxNum = 0; curMaxNum < maxNum + 1; curMaxNum++) {
                dp[index][curMinProfit][curMaxNum] = dp[index - 1][curMinProfit][curMaxNum]
                if (curMaxNum >= group[index])
                    dp[index][curMinProfit][curMaxNum] = (dp[index][curMinProfit][curMaxNum] + dp[index - 1][Math.max(0, curMinProfit - profit[index])][curMaxNum - group[index]]) % MOD
        }
    }
    
    return dp[groupLen - 1][minProfit][maxNum]
    
    
    
    
    
};