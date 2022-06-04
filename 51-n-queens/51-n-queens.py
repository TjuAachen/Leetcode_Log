class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        global res, final
        def check(res, r_selected, c_selected):
            #same col
            for row in range(r_selected):
                if res[row][c_selected] == 'Q':
                    return False
            
            #diagonal
            sum_cor, diff_cor = r_selected - c_selected, r_selected + c_selected
            for row in range(n):
                col_sum, col_diff = row - sum_cor, diff_cor - row
                if 0 <= col_sum < n and res[row][col_sum] == 'Q':
                    return False
                if 0 <= col_diff < n and res[row][col_diff] == 'Q':
                    return False
            return True
        global res,final
        final = []
        res =[['.']*n for _ in range(n)]
        def dfs(step):
            global res,final
            if step == n:
                temp = [''.join(row) for row in res]
                final.append(temp)
                return
            for col in range(n):
                if not check(res, step, col):
                    continue
                res[step][col] = 'Q'
                dfs(step + 1)
                res[step][col] = '.'
        dfs(0)
        return final
        