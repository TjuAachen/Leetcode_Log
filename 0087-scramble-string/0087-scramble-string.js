var memo = new Map()

function isPossible(s1, s2) {
    var n1 = s1.length;
    var map1 = new Map();
    var map2 = new Map();
    
    for (var i = 0; i < n1; i++) {
        var char1 = s1.charAt(i)
        var char2 = s2.charAt(i)
        map1.set(char1, (map1.get(char1) || 0) + 1)
        map2.set(char2, (map2.get(char2) || 0) + 1)
    }
    var base = 'a'.charCodeAt(0)
    for (var j = 0; j < 26; j++) {
        var curChar = String.fromCharCode(j + base)
        if (map1.get(curChar) != map2.get(curChar))
            return false
    }
    
    return true
    
}

/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var isScramble = function(s1, s2) {

    var n = s1.length;
    var key = s1 + '*' + s2
    if (memo.has(key))
        return memo.get(key)
    if (!isPossible(s1, s2))
        return false;
    if (n == 1 && s1 != s2)
        return false
    if (s1 == s2)
        return true
    for (var i = 1; i < n; i++) {
        var left1 = s1.slice(0, i)
        var right1 = s1.slice(i, n)
        var left2 = s2.slice(0, i)
        var right2 = s2.slice(i, n)
        var leftSwapped2 = s2.slice(0, n - i)
        var rightSwapped2 = s2.slice(n - i, n)
        //not swapped
        var notSwappedRes = arguments.callee(left1, left2) && arguments.callee(right1, right2)
        if (notSwappedRes){
            memo.set(key, true)
            return true
        }
        //swapped
        var swappedRes = arguments.callee(leftSwapped2, right1) && arguments.callee(rightSwapped2, left1)
        if (swappedRes) {
            memo.set(key, true)
            return true
        }
    }
    memo.set(key, false)
    return false
};