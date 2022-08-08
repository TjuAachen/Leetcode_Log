class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        row_count = {}
        col_count = {}
        #memo = {}
        
        def calculate(col_cor, row, row_index, flag):
            #left
            if flag == 1 and (row_index, col_cor) in row_count:
                return row_count[(row_index, col_cor)]
            if flag == 0 and (col_cor, row_index) in col_count:
                return col_count[(col_cor, row_index)]
            i = col_cor
            count_row = 0
            n = len(row)
            neighbor = []
            while(i >= 0 and row[i] != 'W'):
                if row[i] == 'E':
                    count_row += 1
                if row[i] == '0':
                    neighbor.append(i)
                i = i - 1
            #right
            j = col_cor
            while(j < n and row[j] != 'W'):
                if row[j] == 'E':
                    count_row += 1
                if row[j] == '0':
                    neighbor.append(j)
                j = j + 1
            for point in neighbor:
                #row
                if flag:
                    row_count[(row_index, point)] = count_row
                else:
                    col_count[(point, row_index)] = count_row
            return count_row

        maximum = 0
        grid_transpose = list(zip(*grid))
        for i in range(nrow):
            for j in range(ncol):
                col = grid_transpose[j]
                temp = 0
                if grid[i][j] == '0':
                    temp = calculate(j, grid[i], i, 1) +calculate(i, col, j, 0)
                    maximum = max(maximum, temp)
        return maximum
                    
                    
                    
                