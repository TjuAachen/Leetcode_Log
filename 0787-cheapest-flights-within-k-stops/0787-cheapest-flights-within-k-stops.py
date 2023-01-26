class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        graph = defaultdict(list)
        queue = deque()
        distance = defaultdict(int)
        stop = 0
        queue.append([0, src])
        
        self.buildGraph(flights, graph)
        
        #bfs
        while queue and stop <= k:
            size = len(queue)
            
            for _ in range(size):
                curDist, curSrc = queue.popleft()
                #nxt node
                for nxt, nxtPrice in graph[curSrc]:
                    if nxt not in distance or curDist + nxtPrice < distance[nxt]:
                        distance[nxt] = curDist + nxtPrice
                        queue.append([distance[nxt], nxt])
            stop += 1
            
        
        if dst in distance:
            return distance[dst]
        return -1
    def buildGraph(self, flights, graph):
        for start, end, price in flights:
            graph[start].append([end, price])
        