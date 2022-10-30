class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        queue = deque([[0, 0, k - grid[0][0], 0]])
        length = 0
        nrow, ncol = len(grid), len(grid[0])
        visited = set()
        visited.add((0, 0, k - grid[0][0]))
        while(queue):
            size = len(queue)
            
            for i in range(size):
                x, y, curK, curLength = queue.popleft()
                if x == nrow - 1 and y == ncol - 1:
                    return curLength
                for xDiff, yDiff in [[0,1], [0, -1], [1, 0], [-1, 0]]:
                    nextX, nextY = x + xDiff, y + yDiff
                    nextKey = (nextX, nextY, curK)
                    if 0 <= nextX < nrow and 0 <= nextY < ncol and nextKey not in visited:
                        if curK - grid[nextX][nextY] >= 0:
                            visited.add(nextKey)
                            queue.append([nextX, nextY, curK - grid[nextX][nextY], curLength + 1])    
        return -1
        
        
        
        
        
        
        