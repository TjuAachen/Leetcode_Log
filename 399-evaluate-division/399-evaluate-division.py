class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = dict()
        edgeV = dict()
        #build graph
        for ind, edge in enumerate(equations):
            n1, n2 = edge[0], edge[1]
            edgeV[(n1,n2)] = values[ind]
            edgeV[(n2,n1)] = 1/values[ind]
            if n1 not in graph:
                graph[n1] = [n2]
            else:
                graph[n1].append(n2)
            if n2 not in graph:
                graph[n2] = [n1]
            else:
                graph[n2].append(n1)
        def dfs(node, target):
            global track
            if node in visited:
                return False
            if node == target:
                return True
            visited[node] = 1
            for neigh in graph[node]:
                track = track*edgeV[(node,neigh)]
                if dfs(neigh,target):
                    return True
                track = track/edgeV[(node,neigh)]
            return False
        global track
        res = []
        for query in queries:
            visited = dict()
            track = 1
            n1, n2 = query[0], query[1]
            if n1 not in graph or n2 not in graph:
                res.append(-1.0)
            elif dfs(n1,n2):
                res.append(track)
            else:
                res.append(-1.0)
        return res
        
                
            
            