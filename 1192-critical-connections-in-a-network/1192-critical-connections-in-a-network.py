class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        #construct a graph
        graph = dict()
        remove = dict()
        for edge in connections:
            x, y = edge
            remove[tuple(sorted(edge))] = False
            if x not in graph:
                graph[x] = [y]
            else:
                graph[x].append(y)
            if y not in graph:
                graph[y] = [x]
            else:
                graph[y].append(x)
        
        global count
        count = 0
        rank = dict()
        def dfs(prev, node):
            global count
            if node in rank:
                return min(count, rank[node]) 
            if not graph[node]:
                return
            rank[node] = count
            minimum = 10**6
            for nxt in graph[node]:
                if nxt in rank and nxt == prev:
                    continue
                count += 1
                min_count = dfs(node,nxt)
                minimum = min(minimum, min_count)
                if min_count <= rank[node]:
                    remove[tuple(sorted([nxt,node]))] = True
            return min(minimum, rank[node])
        dfs(-1,connections[0][0])
        res = []
        for key,val in remove.items():
            if val == False:
                res.append(list(key))
        return res
                
                
                
            
        