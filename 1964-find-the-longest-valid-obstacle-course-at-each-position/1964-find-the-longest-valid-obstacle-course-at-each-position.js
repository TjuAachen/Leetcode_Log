function findRight(nums, target) {
    var left = 0
    var right = nums.length - 1
    
    while (left + 1 < right) {
        var mid = Math.floor((left + right) / 2)
        if (nums[mid] <= target) {
            left = mid
        }else{
            right = mid
        }
    }
    if (nums[left] > target)
        return left
    if (nums[right] > target)
        return right
    return nums.length
}
/**
 * @param {number[]} obstacles
 * @return {number[]}
 */
var longestObstacleCourseAtEachPosition = function(obstacles) {
    var n = obstacles.length
    var res = Array(n).fill(1)
    var builtArray = []
    
    builtArray.push(obstacles[0])
    
    for (var i = 1; i < n; i++) {
        var cur = obstacles[i]
        var idx = findRight(builtArray, cur)

        if (idx == builtArray.length) {
            res[i] = builtArray.length + 1
            builtArray.push(cur)
        }else{
            res[i] = idx + 1
            builtArray[idx] = cur
        }
        
        
 
    }
    
    return res
    
    
    
    
    
};