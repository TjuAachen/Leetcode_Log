class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        colhits = [0] * ncol
        maximum = 0
        for row in range(nrow):
            for col in range(ncol):
                #reset rowhits
                if col == 0 or grid[row][col-1] == 'W':
                    rowhits = 0
                    for nxt_col in range(col, ncol):
                        if grid[row][nxt_col] == 'W':
                            break
                        if grid[row][nxt_col] == 'E':
                            rowhits += 1
                #reset colhits
                if row == 0 or grid[row-1][col] == 'W':
                    colhits[col] = 0
                    for nxt_row in range(row, nrow):
                        if grid[nxt_row][col] == 'W':
                            break
                        elif grid[nxt_row][col] == 'E':
                            colhits[col] += 1
                if grid[row][col] == '0':
                    maximum = max(maximum, colhits[col] + rowhits)
        return maximum
                    
                