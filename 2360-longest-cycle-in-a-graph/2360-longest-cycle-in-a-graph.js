/**
 * @param {number[]} edges
 * @return {number}
 */
function bfs(start, edges, visited) {
    var queue = [[start, 0]]
    var orderNum = new Map()
    orderNum.set(start, 0)
    
    while (queue.length > 0) {

        var [popped, curOrder] = queue.shift()
        
        var nxt = edges[popped]
        
        if (orderNum.has(nxt)) {

            return curOrder + 1 - orderNum.get(nxt)
        }
        if (visited.has(nxt))
            return -1
        if (nxt == -1)
            return -1
        visited.add(nxt)
        orderNum.set(nxt, curOrder + 1)
        queue.push([nxt, curOrder + 1])
    }
    return -1
    
}


var longestCycle = function(edges) {
    var visited = new Set()
    var n = edges.length
    var ans = -1
    
    for (var i = 0; i < n; i++) {

        if (visited.has(i))
            continue
        ans = Math.max(bfs(i, edges, visited), ans)
    }
    
    return ans
};