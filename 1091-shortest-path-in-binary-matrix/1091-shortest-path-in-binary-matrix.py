from heapq import *
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        MAX = float('inf')
        queue = []
        heapify(queue)
        result = dict()
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        heappush(queue,[1,(0,0)])
        result[(0,0)] = 1
        move = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        
        #BFS
        while(queue):
            size = len(queue)
            for ind in range(size):
                distance, coor = heappop(queue)
                for dx, dy in move:
                    newX, newY = coor[0] + dx, coor[1] + dy
                    if 0 <= newX < nrow and 0 <= newY < ncol and grid[newX][newY] == 0:
                        if (newX,newY) not in result or result[(newX,newY)] > distance + 1:
                            result[(newX, newY)] = distance + 1
                            heappush(queue, [distance+1, (newX, newY)])
        if (nrow-1,ncol-1) in result:
            return result[(nrow-1,ncol-1)]
        return -1
                            
                            
                
            
        
        