class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def check(chess,nrow,ncol):
            rcount, ccount = 0, 0
            for i in chess[nrow]:
                if i == "Q":
                    rcount += 1
            if rcount > 1:
                return False
            for i in range(n):
                if chess[i][ncol] == "Q":
                    ccount += 1
            if ccount > 1:
                return False
            diff = ncol - nrow
            add = ncol + nrow
            ldiag, rdiag = 0, 0
            for i in range(n):
                newr1, newc1 = i, i+diff
                newr2, newc2 = i, add - i
                if 0 <= newc1 < n and chess[newr1][newc1] == "Q":
                    ldiag += 1
                if 0<= newc2 < n and chess[newr2][newc2] == "Q":
                    rdiag += 1
            if ldiag > 1 or rdiag > 1:
                return False
            return True
        total = []
        chess = [['.']*n for i in range(n)]
        def backtracking(nrow):
            if nrow == n:
                res = [['.']*n for i in range(n)]
                for i,row in enumerate(chess):
                    res[i] = ''.join(row)
                total.append(res[:])
                return
            for ncol in range(n):
                chess[nrow][ncol] = 'Q'
                if check(chess, nrow, ncol):
                    backtracking(nrow + 1)
                chess[nrow][ncol] = '.'
        backtracking(0)
        return total
        
                
        