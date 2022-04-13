class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        direction = [(-1,0),(0,-1),(1,0),(0,1)]
        stack = [m for m in range(1,n*n+1)]
        matrix = [[0]*n for _ in range(n)]
        x, y =0, 0
        for i in range(n*n):
                matrix[x][y] = stack[i]
                newx, newy = x + direction[-1][0], y + direction[-1][1]
                if 0 <= newx < n and 0 <= newy < n and matrix[newx][newy] == 0:
                    x, y = newx, newy
                else:
                    direction = [direction.pop()] + direction
                    x, y = x + direction[-1][0], y + direction[-1][1]
        return matrix
                    
                    
                
            
        
        