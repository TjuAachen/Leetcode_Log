from heapq import *
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #shortest path
        queue = []
        distance = defaultdict(int)
        graph = defaultdict(list)
        stopNum = defaultdict(int)
        
        self.buildGraph(flights, graph)
        heappush(queue, [0, 0, src])
        
        while(queue):
            curDist, curStop, curCity = heappop(queue)
            
            if curStop > k:
                continue
            #soft deletion
            if curDist > distance[curCity] and curStop > stopNum[curCity]:
                continue
            if curCity == dst:
                if dst in distance:
                    return min(distance[dst], curDist)
                return curDist
            for nxt, nxtPrice in graph[curCity]:
                nxtDist = nxtPrice + curDist

                if (nxt not in distance or distance[nxt] > nxtDist):
                    distance[nxt] = nxtDist
                    stopNum[nxt] = curStop + 1
                    if curStop + 1 <= k:
                        heappush(queue, [nxtDist, curStop + 1, nxt])
                elif stopNum[nxt] > curStop + 1 and curStop + 1 <= k:
                    #stopNum[nxt] = curStop + 1
                    heappush(queue, [nxtDist, curStop + 1, nxt])
        
        if dst not in distance:
            return -1
        
        return distance[dst]
    
    def buildGraph(self, flights, graph):
        for start, end, price in flights:
            graph[start].append([end, price])
        
        