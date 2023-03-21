/**
 * @param {number[]} nums
 * @return {number}
 */
var zeroFilledSubarray = function(nums) {
    var numSubarray = 0;
    var ans = 0;
    
    nums.forEach((element) => {
        if (element == 0) {
            numSubarray += 1
        }else {
            numSubarray = 0;
        }
        ans += numSubarray
    })
    
    return ans
    
    
    
    
};