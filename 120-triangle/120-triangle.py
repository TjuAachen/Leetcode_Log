from heapq import *
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        queue = []
        max_layer = len(triangle)
        result = dict()
        heapify(queue)
        heappush(queue,[triangle[0][0], (0,0) ])
        result[(0,0)] = triangle[0][0]
        while(queue):
            size = len(queue)
            for i in range(size):
                cur_dist, (x, y) = heappop(queue)
                if x  == max_layer-1 or result[(x,y)] > cur_dist:
                    continue
                #add nxt
                for i in range(2):
                    if (x+1,y+i) not in result or result[(x+1,y+i)] > cur_dist + triangle[x+1][y+i]:
                        result[(x+1,y+i)] = cur_dist + triangle[x+1][y+i]
                        heappush(queue, [result[(x+1,y+i)], (x+1,y+i)])
        return min([result[(max_layer-1,i)] for i in range(max_layer)])
                        
                
        