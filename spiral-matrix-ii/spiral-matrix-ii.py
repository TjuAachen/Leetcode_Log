class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        output = [[0]*n for i in range(n)]
        cur = (0,0)
        output[0][0] = 1
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        i = 1
        while(i<n*n):
            step = direction[0]
            row, col = cur[0] + step[0],cur[1] + step[1]
            if row in range(n) and col in range(n) and output[row][col] == 0:
                output[row][col] = i+1
                cur = (row, col)
                i = i + 1
            else:
                direction = direction[1:]+[step]
        return output
                
            