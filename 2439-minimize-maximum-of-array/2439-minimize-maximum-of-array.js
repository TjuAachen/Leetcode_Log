/**
 * @param {number[]} nums
 * @return {number}
 */
function check(mid, nums) {

    var n = nums.length
    
    var prevSum = 0

    for (var i = 0; i < n; i++) {
        if (nums[i] > mid) {
            if (i == 0)
                return false
            var decreased = nums[i] - mid
            if (prevSum + decreased > mid * i)
                return false
            prevSum += decreased
        }
        prevSum += Math.min(mid, nums[i])
    }
    
    return true
}


var minimizeArrayValue = function(nums) {
    var n = nums.length
    
    var left = 0
    var right = 1000000000
    
    while (left + 1 < right) {
        var mid = left + Math.floor((right - left) / 2)
        if (check(mid, nums)) {
            right = mid
        }else {
            left = mid
        }
    }
    
    if (check(left, nums))
        return left
    return right

};