
function buildGraph(n, connections, graph) {
    for (var i = 0; i < n; i++) {
        graph.set(i, [])
    }
    
    for (const connection of connections) {
        graph.get(connection[0]).push(connection[1])
        graph.get(connection[1]).push(connection[0])
    }
}

function bfs(graph, visited, start) {
    var queue = [start]
    visited.add(start)
    while (queue.length > 0) {
        var popped = queue.shift()
        
        for (const nxt of graph.get(popped)) {
            if (!visited.has(nxt)) {
                queue.push(nxt)
                visited.add(nxt)
            }
        }
    }
}

/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number}
 */
var makeConnected = function(n, connections) {
    var connectNum = connections.length
    if (connectNum < n - 1)
        return -1
    
    var graph = new Map()
    var visited = new Set()
    buildGraph(n, connections, graph)
    var numOfUnions = 0
    
    // bfs, count the unions 
    for (var i = 0; i < n; i++) {
        if (visited.has(i))
            continue
        numOfUnions += 1
        bfs(graph, visited, i)
    }
    
    var needed = numOfUnions - 1

    return needed
    
    
    
    
};

