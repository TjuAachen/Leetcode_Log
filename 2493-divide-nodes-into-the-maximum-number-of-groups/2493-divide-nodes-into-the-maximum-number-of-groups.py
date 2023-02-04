class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        #build a graph
        graph = [[] for _ in range(n)]
        for x, y in edges:
            x -= 1
            y -= 1
            graph[x].append(y)
            graph[y].append(x)
        time = [0] * n
        
        global clock
        clock = 0
        
        def bfs(start):
            global clock
            mx = 0
            clock += 1 
            time[start] = clock
            queue = deque([(start, base)])
            
            while (queue):
                poppedNode, poppedId = queue.popleft()
                mx = max(mx, poppedId)
                for nxt in graph[poppedNode]:
                    if time[nxt] != clock:
                        time[nxt] = clock
                        queue.append((nxt, poppedId + 1))
            return mx
        
        colors = [0] * n
        
        def dfs(node, c):
            nodes.append(node)
            colors[node] = c
            for nxt in graph[node]:
                if colors[nxt] == c or colors[nxt] == 0 and not dfs(nxt, -c):
                    return False
            return True
        base = 0
        ans = 0
        
        for node, c in enumerate(colors):
            nodes = []
            if c != 0:
                continue
            if not dfs(node, 1):
                return -1
            base = ans + 1
          #  print(nodes, ans, base)
            for node in nodes:
                ans = max(bfs(node), ans)
        
        return ans
                
            