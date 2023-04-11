/**
 * @param {string} s
 * @return {string}
 */
var removeStars = function(s) {
  //  var i = 0
    var n = s.length
    var stack = []
    
    for (var i = 0; i < n; i++) {
        var curChar = s.charAt(i)
        
        if (curChar == '*') {
            stack.pop()
        }else {
            stack.push(curChar)
        }
    }
    
    return stack.join("")
    
};