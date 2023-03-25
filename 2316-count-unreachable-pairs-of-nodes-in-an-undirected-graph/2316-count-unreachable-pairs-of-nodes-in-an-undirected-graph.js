/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
function buildGraph(n, edges, graph) {

    for (var edge of edges) {
        var [node1, node2] = edge
        if (!graph.has(node1)) {
            graph.set(node1, [])
        }
        if (!graph.has(node2)) {
            graph.set(node2, [])
        }
        graph.get(node1).push(node2)
        graph.get(node2).push(node1)
    }
}

function bfs(start, graph, visited) {
    var queue = [start]
    var count = 1

    while (queue.length > 0) {
        var popped = queue.shift()
        if (!graph.has(popped))
            continue
        for (var nxt of graph.get(popped)) {

            if (visited.has(nxt))
                continue
            visited.add(nxt)
            count += 1
            queue.push(nxt)
        }
    }
    
    return count
}


var countPairs = function(n, edges) {
    var graph = new Map()
    buildGraph(n, edges, graph)

    var visited = new Set()
   // var remainingNodes = n
    var ans = 0
    
    for (var i = 0; i < n; i++) {
        if (visited.has(i))
            continue
        var queue = [i]
        visited.add(i)
        var sizeOfComponents = bfs(i, graph, visited)
        ans += sizeOfComponents * (n - sizeOfComponents) / 2
        
    }
    
    return ans
};