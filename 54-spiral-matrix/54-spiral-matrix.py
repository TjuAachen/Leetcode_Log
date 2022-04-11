class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = [(-1,0),(0,-1),(1,0),(0,1)]
        m, n = len(matrix), len(matrix[0])
        point = (0,0)
        res = []
        visited = [[False]*n for i in range(m)]
        for i in range(m*n):
            row, col = point[0], point[1]
            res.append(matrix[row][col])
            visited[row][col] = True
            nxt_row, nxt_col = row+direction[-1][0], col + direction[-1][1]
            if  0<= nxt_row < m and 0<= nxt_col < n and not visited[nxt_row][nxt_col]:
                point =(row+direction[-1][0],col + direction[-1][1] )
            else:
                direction = [direction.pop()] + direction
                point =(row+direction[-1][0],col + direction[-1][1] )
        return res
                
                
            
            