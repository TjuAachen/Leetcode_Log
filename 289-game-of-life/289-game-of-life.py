import copy
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        nxt = [[0]*n for i in range(m)]
        def neighbor(i,j):
            direction = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
            count = 0
            for incx, incy in direction:
                newx, newy = i + incx, j + incy
                if 0 <= newx < m and 0<= newy < n and board[newx][newy] == 1:
                    count += 1
            return count
                
        for i in range(m):
            for j in range(n):
                count_live = neighbor(i,j)
                if board[i][j] == 1 and count_live in [2, 3]:
                    nxt[i][j] = 1
                elif board[i][j] == 0 and count_live == 3:
                    nxt[i][j] = 1
          #      print(i,j,count_live, nxt[i][j])
        board[:] = nxt[:]
                
                