/**
 * @param {number[]} nums
 * @return {number}
 */
function sign(num) {
    if (num > 0)
        return 1
    if (num < 0)
        return -1
    return 0
}
var arraySign = function(nums) {
    var res = 1
    for (var num of nums) {
        res *= sign(num)
    }
    
    return res
};