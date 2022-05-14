from heapq import *
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        direction = dict()
        weight = dict()
        result = dict()
        for time in times:
            source, target, w = time
            if source in direction:
                direction[source].append(target)
            else:
                direction[source] = [target]
            if (source,target) not in weight:
                weight[(source,target)] = w
        queue = []
        heapify(queue)
        heappush(queue,[k,0])
        result[k] = 0
        while(queue):
            size = len(queue)
            for i in range(size):
                popped,_ = heappop(queue)
                if popped not in direction:
                    continue
                for nxt in direction[popped]:
                    distance = weight[(popped,nxt)]
                    if nxt in result and result[nxt] <= result[popped] + distance:
                        continue
                    else:
                        result[nxt] = result[popped] + distance
                        queue.append([nxt,result[nxt]])
        if len(result) == n:
            return max([i for i in result.values()])
        return -1
                        
        
        
                
        