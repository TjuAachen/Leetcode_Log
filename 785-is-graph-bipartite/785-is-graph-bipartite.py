class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [False]*n
        visited = dict()
        def dfs(node):
            global final
            visited[node] = 1
            for neigh in graph[node]:
                if neigh in visited:
                    if color[neigh] == color[node]:
                        return True
                else:
                    color[neigh] = not color[node]
                    if dfs(neigh):
                        return True
            return False
        for i in range(n):
            if dfs(i):
                return False
        return True
            
        
            
        