function swapStr(str, first, last){
    return str.substr(0, first)
           + str[last]
           + str.substring(first+1, last)
           + str[first]
           + str.substr(last+1);
}


function bfs(str, map, visited) {
    var queue = [str]
    
    //modify the str and swap 2 letters to get the final step
    while (queue.length > 0) {
        var popped = queue.shift()
        var m = popped.length
        for (var i = 0; i < m; i++) 
            for (var j = i + 1; j < m; j++) {
                if (popped[i] == popped[j])
                    continue
                //swap
                swappedStr = swapStr(popped, i, j)
                if (visited.has(swappedStr))
                    continue
                if (map.has(swappedStr)) {
                    queue.push(swappedStr)
                    visited.add(swappedStr)
                }
            }
    }
}


/**
 * @param {string[]} strs
 * @return {number}
 */
var numSimilarGroups = function(strs) {
    //bfs 连通块问题
    var n = strs.length
    var map = new Set()
    var visited = new Set()
    var numGroups = 0

    //add all strings into the set 
    for (var i = 0; i < n; i++) {
        var str = strs[i]
        map.add(str)
    }
    
    for (var i = 0; i < n; i++) {
        var str = strs[i]
        if (visited.has(str)) {
            continue
        }
        bfs(str, map, visited)
        visited.add(str)
        numGroups += 1
    }
    
    
    return numGroups
};