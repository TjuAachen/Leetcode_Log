/**
 * @param {string} s
 * @return {number}
 */
var partitionString = function(s) {
    var numSubstrings = 0
    var n = s.length
    var charSet = new Set()
    
    for (var i = 0; i < n; i++) {
        var curChar = s.charAt(i)
        if (charSet.has(curChar)) {
            numSubstrings += 1

            charSet = new Set()
        }
        charSet.add(curChar)
    }

    if (charSet.size > 0)
        numSubstrings += 1
    
    return numSubstrings
    
};