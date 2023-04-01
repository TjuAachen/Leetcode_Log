/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    var n = nums.length
    var left = 0
    var right = n - 1
    
    while (left + 1 < right) {
        var mid = left + Math.floor((right - left) / 2)
        var curVal = nums[mid]

        if (curVal == target)
            return mid
        if (curVal < target)
            left = mid
        if (curVal > target)
            right = mid
    }
    
    if (nums[left] == target)
        return left
    if (nums[right] == target)
        return right
    
    return -1
    
    
};