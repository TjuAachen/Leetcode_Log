function bisect(potions, target) {
    var left = 0
    var right = potions.length - 1
    
    while (left + 1 < right) {
        var mid = left + Math.floor((right - left) / 2)        
        var curVal = potions[mid]
        
        if (curVal < target) {
            left = mid
        }else {
            right = mid
        }
    }

    if (potions[left] >= target) {
        return potions.length - left
    }
    if (potions[right] >= target) {
        return potions.length - right
    }
    return 0
}
/**
 * @param {number[]} spells
 * @param {number[]} potions
 * @param {number} success
 * @return {number[]}
 */
var successfulPairs = function(spells, potions, success) {
    var ans = []
    potions.sort((a, b) => a - b)
    
    for (var spell of spells) {
        var target = Math.ceil(success / spell)

        ans.push(bisect(potions, target))
    }
    
    return ans
    
};

