/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    var maxNum = candies.reduce((a, b) => Math.max(a, b), -Infinity);

    var ans = []
  //  console.log(maxNum)
    for (var candy of candies) {
        if (candy + extraCandies >= maxNum) {
            ans.push(true)
        }else{
            ans.push(false)
        }
    }
    
    return ans
};