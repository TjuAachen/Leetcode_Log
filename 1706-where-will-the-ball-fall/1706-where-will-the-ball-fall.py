class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        answer = []
        m, n = len(grid), len(grid[0])
        
        for col in range(n):
            row = 0
            while(row >= 0 and row < m):
                if col + grid[row][col] < n and grid[row][col+grid[row][col]] == -grid[row][col]:
                    answer.append(-1)
                    break
                col += grid[row][col]
                row += 1
                if col>= n or col < 0:
                    answer.append(-1)
                    break
            if row == m and 0 <= col < n:
                answer.append(col)
        return answer
                
                    
            
            