/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function(path) {
    // states machine
    //use the stack
    var stack = []
    var n = path.length
    stack.push('/')
    path += '/'
    var i = 1
    var curPath = ''
    while (i < n + 1) {
        var curChar = path.charAt(i)
      //  console.log(stack, curChar, curPath)
        if (curChar == '/') {
            if (curPath == '..') {
                
                if (stack.length > 2) {
                    stack.pop()
                    stack.pop()
                }
            }else if (curPath != '.' && curPath != '') {
                stack.push(curPath)
                stack.push('/')
            }
            curPath = ''
        }else {
            curPath += curChar
        }
        i += 1
    }
    
    if (stack.length > 1 && stack[stack.length - 1] == '/')
        stack.pop()
    
    return stack.join("")
    
};