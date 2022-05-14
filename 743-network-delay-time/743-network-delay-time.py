from heapq import *
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        direction = dict()
        result = dict()
        for time in times:
            source, target, w = time
            if source in direction:
                direction[source].append([target,w])
            else:
                direction[source] = [[target,w]]

        queue = []
        heapify(queue)
        heappush(queue,[0,k])
        result[k] = 0
        while(queue):
            size = len(queue)
            for i in range(size):
                _,popped = heappop(queue)
                if popped not in direction:
                    continue
                for nxt,distance in direction[popped]:
                    if nxt not in result or result[nxt] > result[popped] + distance:
                        result[nxt] = result[popped] + distance
                        heappush(queue,[result[nxt],nxt])
        if len(result) == n:
            return max([i for i in result.values()])
        return -1
                        
        
        
                
        