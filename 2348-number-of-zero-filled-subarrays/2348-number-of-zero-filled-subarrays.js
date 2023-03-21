/**
 * @param {number[]} nums
 * @return {number}
 */
var zeroFilledSubarray = function(nums) {
    var map = new Map()
    var curCount = 0
    
    for (var i = 0; i < nums.length; i++) {
        var num = nums[i]
        
        if (num == 0) {
            curCount += 1
        }else if (curCount != 0) {
            map.set(curCount, (map.get(curCount) || 0) + 1)
            curCount = 0
        }
    }
    
    if (curCount != 0) {
        map.set(curCount, (map.get(curCount) || 0) + 1)
    }
    
    var ans = 0
    for (const [key, value] of map) {

        ans += value * (key + 1) * key / 2
    }
    
    return ans
    
    
    
};