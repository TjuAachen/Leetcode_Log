class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nrow, ncol = len(board), len(board[0])
        F = [0 for _ in range(nrow*ncol+1)]
        for i in range(nrow):
            for j in range(ncol):
                index = i*ncol + j
                if board[i][j] == 'O':
                    if i == 0 or i == nrow - 1 or j == 0 or j == ncol-1:
                        F[index] = nrow*ncol
                    else:
                        F[index] = index
        F[nrow*ncol] = nrow*ncol
        def find(x):
            while(x != F[x]):
                F[x] = F[F[x]]
                x = F[x]
            return x
        def union(x,y):
            rootx, rooty = find(x), find(y)
            if rootx == rooty:
                return
            if rootx == nrow*ncol:
                F[rooty] = rootx
            elif rooty == nrow*ncol:
                F[rootx] = rooty
            else:
                F[rooty] = rootx
                
        for i in range(1,nrow-1):
            for j in range(1,ncol-1):
                index = i*ncol + j
                if board[i][j] == 'O':
                    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        newX, newY = i+dx, j+dy
                        newIndex = newX*ncol+newY
                        if board[newX][newY] == 'O':
                            if newX == 0 or newX == nrow-1 or newY == 0 or newY == ncol - 1:
                                union(index,nrow*ncol)
                            else:
                                union(index,newIndex)
      #  print(F)
        for i in range(1,nrow-1):
            for j in range(1,ncol-1):
                index = i*ncol + j
                if find(F[index]) != nrow*ncol and F[index] != 0:
                    board[i][j] = 'X'
        return board
                    
                        
        