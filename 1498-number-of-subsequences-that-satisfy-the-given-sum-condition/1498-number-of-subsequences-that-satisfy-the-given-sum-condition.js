function moduloMultiplication(a, b, mod)
{
     
    // Initialize result
    let res = 0; 
 
    // Update a if it is more than
    // or equal to mod
    a = (a % mod);
 
    while (b > 0)
    {
         
        // If b is odd, add a with result
        if ((b & 1) > 0)
        {
            res = (res + a) % mod;
        }
 
        // Here we assume that doing 2*a
        // doesn't cause overflow
        a = (2 * a) % mod;
 
        b = (b >> 1); // b = b / 2
    }
    return res;
}

function fastPower(exponent) {
    var MOD = 1000000007
    var ans = 1
    var x = 2
    while (exponent > 0) {
        if ((exponent & 1) != 0){
            ans = moduloMultiplication(ans, x, MOD)
        }
        exponent = exponent >> 1
        x = moduloMultiplication(x, x, MOD)
    }
    return ans % MOD
}
function rightTarget(nums, target, rightIdx) {
    var left = 0
    var right = rightIdx
    
    while (left + 1 < right) {
        var mid = Math.floor((left + right) / 2)
        var curVal = nums[mid]
        
        if (curVal > target) {
            right = mid
        }else{
            left = mid
        }
    }
    if (nums[right] <= target)
        return right
    if (nums[left] <= target)
        return left
    return -1
}
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var numSubseq = function(nums, target) {
    var MOD = 1000000007
    nums.sort((a, b) => a - b)
    var n = nums.length
    var dp = Array(n).fill(0)
    var prefix = Array(n).fill(0)
    
    if (nums[0] * 2 <= target){
        dp[0] = 1
        prefix[0] = 1
    }

    for (var i = 1; i < n; i++) {
        prefix[i] = prefix[i - 1]
        var curVal = nums[i]
        var prev = target - curVal
        var rightIdx = rightTarget(nums, prev, i)
        if (rightIdx == -1) {
            continue
        }
        if (rightIdx == i) {
            dp[i] = fastPower(i) % MOD
        }else{
            dp[i] = moduloMultiplication(prefix[rightIdx] , fastPower(i - rightIdx - 1) , MOD)
        }
        prefix[i] = (prefix[i - 1] + dp[i]) % MOD


    }

    return prefix[n - 1] % MOD
};