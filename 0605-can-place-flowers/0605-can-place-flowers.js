/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    var count = 0;
    for (var i = 0; i < flowerbed.length; i++) {
        if (flowerbed[i] == 0) {
            var emptyLeftPlot = (i == 0) || (flowerbed[i - 1] == 0)
            var emptyRightPlot = (i == flowerbed.length - 1) || (flowerbed[i + 1] == 0)
            
            if (emptyLeftPlot && emptyRightPlot) {
                flowerbed[i] = 1;
                count++;
            }
        }
    }

    
    return count >= n;
    
};