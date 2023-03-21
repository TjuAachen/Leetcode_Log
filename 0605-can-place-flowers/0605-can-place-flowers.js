/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    var flowerbedLength = flowerbed.length
    var i = 0;
    
    while (n > 0 && i < flowerbedLength) {
        var curPosition = flowerbed[i]
        if (curPosition == 0) {
            if (i > 0 && flowerbed[i - 1] == 0 && (i == flowerbedLength - 1 || flowerbed[i + 1] == 0)) {
                flowerbed[i] = 1
                n -= 1
            }else if (i == 0 && (i == flowerbedLength - 1 || flowerbed[i + 1] == 0)) {
                flowerbed[i] = 1
                n -= 1
            }
        }
        i += 1
    }
    
    return n == 0
    
};