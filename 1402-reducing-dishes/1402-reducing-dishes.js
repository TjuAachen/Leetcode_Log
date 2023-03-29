/**
 * @param {number[]} satisfaction
 * @return {number}
 */
var maxSatisfaction = function(satisfaction) {
    satisfaction.sort(function(a, b){return a - b})
    var n = satisfaction.length
    var prefix = [0]
    var curSum = 0;
    
    for (var i = 0; i < n; i++) {

        curSum += satisfaction[i]
        prefix.push(curSum)
    }
    
    var res = 0
    var curRes = 0
    
    for (var j = n - 1; j >= 0; j--) {
        curRes += prefix[n] - prefix[j]
        res = Math.max(res, curRes)
    }
    
    return res
    
    
    
    
};