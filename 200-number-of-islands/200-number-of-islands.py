class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        def backtrack(i,j):
            grid[i][j] = "0"
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                newX = i + dx
                newY = j + dy
                if 0 <= newX < row and 0 <= newY < col and grid[newX][newY] == "1":
                    backtrack(newX, newY)
            return
        num = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    num += 1
                    backtrack(i,j)
        return num
                
            