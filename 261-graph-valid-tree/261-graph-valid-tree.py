class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #graph generation
        graph = dict()
        if not edges:
            if n == 1:
                return True
            else:
                return False
        for p1, p2 in edges:
            start = p1
            p1_val = graph.setdefault(p1,[]) 
            p2_val = graph.setdefault(p2,[])
            p1_val.append(p2)
            p2_val.append(p1)
        visited = {}
        onPath = {}
        prev = None
        global isCycle
        isCycle = False
        def dfs(point, prev):
            global isCycle
            if isCycle:
                return
            visited[point] = 1
            for nxt in graph[point]:
                #form a cycle
                if nxt == prev:
                    continue
                if nxt in onPath:
                    isCycle = True
                    return
                if nxt in visited:
                    continue
                onPath[nxt] = 1
                dfs(nxt, point)
                del onPath[nxt]
        
        onPath[start] = 1
        dfs(start, prev)
        if len(visited) == n and not isCycle:
            return True
        return False
        
        
        #cycle detection
        