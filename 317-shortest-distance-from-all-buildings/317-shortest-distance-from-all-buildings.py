class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dirs = [(1,0), (0,1),(0, -1), (-1, 0)]
        nrow, ncol = len(grid), len(grid[0])
        total = [[0] * ncol for _ in range(nrow)]
        emptyLand = 0
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] != 1:
                    continue
                queue = deque()
                if grid[i][j] == 1:
                    minDist = float('inf')
                queue.append([i, j])
                step = 0
                while(queue):
                    step += 1
                    size = len(queue)
                    for k in range(size):
                        x, y = queue.popleft()
                        for dx, dy in dirs:
                            newx, newy = x + dx, y + dy
                            
                            if 0 <= newx < nrow and 0 <= newy < ncol and grid[newx][newy] == emptyLand:
                                grid[newx][newy] -= 1
                                total[newx][newy] += step
                                minDist = min(total[newx][newy], minDist)
                                queue.append([newx, newy])
                emptyLand -= 1
        if minDist == float('inf'):
            return -1
        return minDist
                
                
            
                        
                        
                        
            
            
        