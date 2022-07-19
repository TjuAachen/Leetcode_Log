class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nrow, ncol = len(grid), len(grid[0])
        
        barriers = set()
        houses = set()

        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 1:
                    houses.add((i,j))
                elif grid[i][j] == 2:
                    barriers.add((i,j))
        num_houses = len(houses)
        num_barriers = len(barriers)
        
        diff = [(1,0), (-1,0), (0,-1), (0,1)]
        total = [[float('inf')] * ncol for _ in range(nrow)]
        count = [[0] * ncol for _ in range(nrow)]
        max_count = 0
        j = 0
        for x, y in houses:
            queue = deque()
            queue.append([x,y])
            seen = set()
            step = 0
            while(queue):
                step += 1
                size = len(queue)
                for i in range(size):
                    x, y = queue.popleft()
                    for dx, dy in diff:
                        newx, newy = x + dx, y + dy
                        if 0 <= newx < nrow and 0 <= newy < ncol:
                            if (newx, newy) not in barriers and (newx, newy) not in houses and (newx, newy) not in seen:
                                if j == 0:
                                    total[newx][newy] = step
                                else:
                                    total[newx][newy] += step
                                queue.append([newx, newy])
                                seen.add((newx, newy))
                                count[newx][newy] += 1
                                max_count = max(count[newx][newy], max_count)
            
            j = j + 1
            if max_count != j:
                return -1
        ans = float('inf')
        for i in range(nrow):
            for j in range(ncol):
                if total[i][j] != float('inf') and count[i][j] == num_houses:
                    ans = min(total[i][j], ans)
        if ans != float('inf'):
            return ans
        return -1
                
            
                        
                        
                        
            
            
        