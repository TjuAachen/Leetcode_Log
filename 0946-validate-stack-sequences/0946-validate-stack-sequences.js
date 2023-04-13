/**
 * @param {number[]} pushed
 * @param {number[]} popped
 * @return {boolean}
 */
var validateStackSequences = function(pushed, popped) {
    var stack = []
    
    while (pushed.length > 0 || popped.length > 0) {

        // do the pop operations first
        while (stack.length > 0 && popped.length > 0 && stack[stack.length - 1] == popped[0]) {
            stack.pop()
            popped.shift()
        }
        

        if (pushed.length > 0) {
            if (popped.length > 0 && popped[0] == pushed[0]) {
                popped.shift()
                pushed.shift()
            }else {
                var poppedFromPushed = pushed.shift()
                stack.push(poppedFromPushed)
            }
            
        }else if (popped.length > 0){
        
            var poppedElement = popped.shift()
            if (stack.length == 0 || stack[stack.length - 1] != poppedElement)
                return false
            
            stack.pop()
        }
    }
    
    return true
};