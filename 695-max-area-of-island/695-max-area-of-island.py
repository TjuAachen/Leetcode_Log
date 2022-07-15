class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        global res
        nrow, ncol = len(grid), len(grid[0])
        dire = [(1,0), (0,-1),(-1,0),(0,1)]
        def maxArea(x, y):
            global res
            if grid[x][y] == 0:
                return
            res += 1
            grid[x][y] = 0
            for dx, dy in dire:
                newx, newy = x + dx, y + dy
                if 0 <= newy < ncol and 0 <= newx < nrow:
                    maxArea(newx, newy)
        ans = 0
        for i in range(nrow):
            for j in range(ncol):
                res = 0
                if grid[i][j] == 0:
                    continue
                maxArea(i,j)
                ans = max(ans, res)
        return ans
            
        