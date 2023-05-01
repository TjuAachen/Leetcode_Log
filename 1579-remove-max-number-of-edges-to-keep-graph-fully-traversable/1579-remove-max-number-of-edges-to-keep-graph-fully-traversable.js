/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var UnionSet = function(n) {
    this.parent = Array(n).fill().map((_, i) => i)
    this.size = Array(n).fill(1)
    this.components = n - 1
}

UnionSet.prototype.find = function(node) {
    if (this.parent[node] == node)
        return node
    this.parent[node] = this.find(this.parent[node])
    //why not this.parent[node] = this.find(node)
    return this.parent[node]
}

UnionSet.prototype.union = function(n1, n2) {
    var p1 = this.find(n1)
    var p2 = this.find(n2)

    if (p1 == p2)
        return 0
    if (this.size[p1] <= this.size[p2]) {
        this.parent[p1] = this.parent[p2]
        this.size[p2] += this.size[p1]
    }else {
        this.parent[p2] = this.parent[p1]
        this.size[p1] += this.size[p2]        
    }
    
    this.components--
    return 1
}

UnionSet.prototype.isConnected = function() {
    return this.components == 1
}

var maxNumEdgesToRemove = function(n, edges) {
    var edgeRequired = 0
    var Alice = new UnionSet(n + 1)
    var Bob = new UnionSet(n + 1)
    
    for (var edge of edges) {
        if (edge[0] == 3) {
            edgeRequired += (Alice.union(edge[1], edge[2]) | Bob.union(edge[1], edge[2]))
        }
    }
    
    for (var edge of edges) {
        if (edge[0] == 1) {
            edgeRequired += Alice.union(edge[1], edge[2])
        }else if (edge[0] == 2) {
            edgeRequired += Bob.union(edge[1], edge[2])
        }
    }

    if (Alice.isConnected() && Bob.isConnected())
        return edges.length - edgeRequired
    return -1
    
};