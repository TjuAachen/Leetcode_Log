/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {Node} node
 * @return {Node}
 */
var cloneGraph = function(node) {
    
    if (node == null)
        return null
    
    
    var clonedOnes = new Map()
    var queue = [node]
    
    var clonedPopped = new Node(node.val)
    clonedOnes.set(node, clonedPopped)
    
    
    while (queue.length > 0) {
        var popped = queue.shift()
        
        var clonedPopped = clonedOnes.get(popped)
      //  clonedOnes.set(popped, clonedPopped)
        
        for (var nxt of popped.neighbors) {
            if (!clonedOnes.has(nxt)) {
                clonedOnes.set(nxt, new Node(nxt.val))
                queue.push(nxt)
            }
 
            clonedPopped.neighbors.push(clonedOnes.get(nxt))
            
        }
    }
    
    return clonedOnes.get(node)
    
    
    
    
};