// constructor function
var SmallestInfiniteSet = function() {
    this.popValues = []
};

/**
 * @return {number}
 */
SmallestInfiniteSet.prototype.popSmallest = function() {
    var curLength = this.popValues.length
    
    if (curLength == 0) {
        this.popValues.push(1)
        return 1
    }
    for (var i = 0; i < curLength; i++) {
        var curVal = this.popValues[i]
        var expectedVal = i + 1
        if (curVal != expectedVal) {
            this.popValues = this.popValues.slice(0, i).concat([expectedVal]).concat(this.popValues.slice(i, curLength))
            return expectedVal
        }
    }
    
    this.popValues.push(curLength + 1)    
    return curLength + 1
    
    
    
};

/** 
 * @param {number} num
 * @return {void}
 */
SmallestInfiniteSet.prototype.addBack = function(num) {
    var poppedLen = this.popValues.length
    
    // if poppedValues is empty or the added number has not been popped
    if (poppedLen == 0 || poppedLen[poppedLen - 1] < num || poppedLen[0] > num)
        return
    
    this.popValues = this.popValues.filter(function(item) {
    return item !== num
})
};

/** 
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * var obj = new SmallestInfiniteSet()
 * var param_1 = obj.popSmallest()
 * obj.addBack(num)
 */