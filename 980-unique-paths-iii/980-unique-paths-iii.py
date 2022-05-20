class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = dict()
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        endx, endy = 0, 0
        startx, starty = 0, 0
        onPath = dict()
        count = 0
        global res
        onPath = dict()
        res = 0
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    endx, endy = i, j
                if grid[i][j] == 1:
                    startx, starty = i, j
                if grid[i][j] != -1:
                    count += 1
        
        
        def dfs(x, y):
            global res
            onPath[(x,y)] = 1
            if (x,y) == (endx, endy) and len(onPath) == count:
                res += 1
                del onPath[(x,y)]
                return
            for dx, dy in directions:
                newx, newy = x+dx, y+dy
                if (newx, newy) in onPath:
                    continue
                if 0 <= newx < m and 0 <= newy < n and grid[newx][newy] != -1:
                    dfs(newx, newy)
            del onPath[(x,y)]
            return 
        dfs(startx, starty)
        
        return res
        