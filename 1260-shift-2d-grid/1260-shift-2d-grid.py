class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def oneShift(grid):
            m, n = len(grid), len(grid[0])            
            final = [grid[i][n-1] for i in range(m)]
            for j in range(n-2,-1,-1):
                for i in range(m):
                    grid[i][j+1] = grid[i][j]                
            for i in range(m-2,-1,-1):
                grid[i+1][0] = final[i]
            grid[0][0] = final[m-1]
        for i in range(k):
            oneShift(grid)
        return grid
                
                