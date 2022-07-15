class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nrow, ncol = len(grid), len(grid[0])
        dire = [(1,0), (0,-1),(-1,0),(0,1)]
        def maxArea(x, y):
            stack = []
            grid[x][y] = 0
            stack.append([x,y])
            ans = 0
            while(stack):
                i, j= stack.pop()
                ans += 1                
                grid[i][j] = 0
                for dx, dy in dire:
                    newx, newy = i + dx, j + dy
                    if 0 <= newy < ncol and 0 <= newx < nrow:
                        if grid[newx][newy] == 1:
                            stack.append([newx, newy])
                            grid[newx][newy] = 0
                
            return ans
        ans = 0
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 0:
                    continue
                ans = max(ans, maxArea(i,j))
        return ans
            
        