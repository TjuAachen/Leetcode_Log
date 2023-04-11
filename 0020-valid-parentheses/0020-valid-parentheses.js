/**
 * @param {string} s
 * @return {boolean}
 */

var map = new Map()
map.set('(', ')')
map.set('[',']')
map.set('{', '}')


var isValid = function(s) {
    var stack = []
    var n = s.length
    
    for (var i = 0; i < n; i++) {
        var char = s.charAt(i)
       // console.log(stack)
        if (map.has(char)) {
            stack.push(char)
        }else{
            if (stack.length == 0)
                return false
            var popped = stack.pop()

            if (map.get(popped) != char)
                return false
        }
    }
    if (stack.length > 0)
        return false
    return true
};