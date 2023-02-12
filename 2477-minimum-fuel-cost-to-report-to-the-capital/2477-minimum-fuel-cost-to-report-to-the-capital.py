#topological sort
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        global res
        res = 0
        graph = defaultdict(set)
        
        #build graph
        for road in roads:
            start, end = road
            graph[start].add(end)
            graph[end].add(start)
        
        self.dfs(0, -1, graph, seats)
        
        return res
        #dfs
    def dfs(self, cur, parent, graph, seats):
        global res
        size = 1
        
        for nxt in graph[cur]:
            if nxt == parent or nxt == 0:
                continue
            size += self.dfs(nxt, cur, graph, seats)
        
        if cur != 0:
            res += (size + seats - 1)//seats
        
        return size
        
        
                    
                
                
                
                
            
                