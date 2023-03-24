function buildGraph(n, connections, graph) {
    for (var i = 0; i < n; i++) {
        graph.set(i, [])
    }
    
    for (const connection of connections) {
        var start = connection[0]
        var end = connection[1]
        graph.get(start).push([end, 1])
        graph.get(end).push([start, 0])
    }
}

/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number}
 */
var minReorder = function(n, connections) {
    var graph = new Map()
    buildGraph(n, connections, graph)
    var queue = [0]
    var ans = 0
    var visited = new Set()
    visited.add(0)

    
    while (queue.length > 0) {
        var popped = queue.shift()
        
        for (const nxt of graph.get(popped)) {
            var [point, val] = nxt
            if (visited.has(point))
                continue

            visited.add(point)
            queue.push(point)
            ans += val
        }
    }
    
    return ans
    
    
    
    
};

