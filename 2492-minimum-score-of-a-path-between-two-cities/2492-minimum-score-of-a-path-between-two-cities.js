/**
 * @param {number} n
 * @param {number[][]} roads
 * @return {number}
 */
var map = new Map();

function buildGraph(n, roads) {
    for (var i = 1; i < n + 1; i++) {
        map.set(i, [])
    }
    roads.forEach((road) => {
                  map.get(road[0]).push([road[1], road[2]])
                    map.get(road[1]).push([road[0], road[2]])
                  })
}

var minScore = function(n, roads) {
    var queue = [[1, 10001]]
    var distanceMap = new Map()
    distanceMap.set(1, 10001)
    
    buildGraph(n, roads)
  
    while (queue.length > 0) {

        var popped = queue.shift()
        
        if (popped[1] > distanceMap.get(popped[0]))
            continue

        for (const nxt of map.get(popped[0])) {
            var curDistance = Math.min(popped[1], nxt[1])

            if (!distanceMap.has(nxt[0]) || (distanceMap.get(nxt[0]) > curDistance)) {
                
                distanceMap.set(nxt[0], curDistance)
                queue.push([nxt[0], curDistance])
            }
        } 
    }

    return distanceMap.get(n)
    
    
    
    
};
    
    
    