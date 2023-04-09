/**
 * @param {string} colors
 * @param {number[][]} edges
 * @return {number}
 */


function dfs(node, path, colors) {
    
    if (nodeAns.has(node))
        return 0
    
    var maxChars = []
    for (var i = 0; i < 26; i++) {
        maxChars.push(0)
    }

    if (graph.has(node)) {

        for (var nxt of graph.get(node)) {
            if (path.has(nxt))
                return -1
            path.add(nxt)
            if (arguments.callee(nxt, path, colors) == -1)
                return -1
            var chars = nodeAns.get(nxt)
           // var isOverlapping = false
            for (var i = 0; i < 26; i++) {
                maxChars[i] = Math.max(maxChars[i], chars[i])
            }

            path.delete(nxt)
        }
    }

    maxChars[colors.charCodeAt(node) - 'a'.charCodeAt(0)] += 1
    nodeAns.set(node, maxChars)
    
    return 0
    
    
}


var largestPathValue = function(colors, edges) {
   graph = new Map()
    nodeAns = new Map()
    
    // build graph
    for (var [start, end] of edges) {
        if (!graph.has(start))
            graph.set(start, [])
        graph.get(start).push(end)
    }
    
    var n = colors.length
    
    for (var node = 0; node < n; node++) {
        if (nodeAns.has(node))
            continue
        var path = new Set()
        path.add(node)
        if (dfs(node, path, colors) == -1)
            return -1
    }
    
    var ans = 0
  //  console.log(nodeAns)
    for (var node = 0; node < n; node++) {
        ans = Math.max(ans, nodeAns.get(node).reduce((a, b) => Math.max(a, b)))
    }
    
    return ans
};