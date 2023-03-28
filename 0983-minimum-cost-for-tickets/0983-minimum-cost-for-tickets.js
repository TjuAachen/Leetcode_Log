/**
 * @param {number[]} days
 * @param {number[]} costs
 * @return {number}
 */
var mincostTickets = function(days, costs) {
    var n = days.length
    var dp = []
    var minVal = Math.min.apply(Math, costs);

    

    for (var i = 0; i < n; i++) {
        var curRes = 3650000;
        var isOne = false
        var isSeven = false
        var isMonth = false
        
        for (var j = i - 1; j >= 0; j--) {
            if (days[j] <= days[i] - 1 && !isOne) {
                curRes = Math.min(curRes, dp[j] + costs[0])
                isOne = true
            }
            if (days[j] <= days[i] - 7 && !isSeven) {
                isSeven = true
                curRes = Math.min(curRes, dp[j] + costs[1])
            }
            if (days[j] <= days[i] - 30 && !isMonth) {
                isMonth = true
                curRes = Math.min(curRes, dp[j] + costs[2])
            }            
            
        }

        if (!isMonth) {
            curRes = Math.min(curRes, costs[2])
        }
        if (!isSeven) {
            curRes = Math.min(curRes, costs[1])
        }       
        if (!isOne) {
            curRes = Math.min(curRes, costs[0])
        } 
        dp.push(curRes)
        
        
        
        
    }

    return dp[n - 1]
};