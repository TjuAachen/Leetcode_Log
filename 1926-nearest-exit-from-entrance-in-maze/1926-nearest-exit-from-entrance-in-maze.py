class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        #BFS
        visited = set()
        
        #find all exits
        nRow, nCol = len(maze), len(maze[0])
        
        queue = deque()
        
        if maze[entrance[0]][entrance[1]] == '+':
            return -1
        
        visited.add(tuple(entrance))
        for row in range(nRow):
            key1 = tuple([row, 0])
            key2 = tuple([row, nCol - 1])
            if key1 not in visited and maze[row][0] == '.':
                queue.append([row, 0, 0])
                visited.add(key1)
            if key2 not in visited and maze[row][-1] == '.':
                queue.append([row, nCol - 1, 0])
                visited.add(key2)
        
        for col in range(nCol):
            key1 = tuple([0, col])
            key2 = tuple([nRow - 1, col])
            if key1 not in visited and maze[0][col] == '.':
                queue.append([0, col, 0])
                visited.add(key1)
            if key2 not in visited and maze[nRow - 1][col] == '.':
                queue.append([nRow - 1, col, 0])
                visited.add(key2)            
            
        step = 0
        while(queue):
           # print(queue, visited)
            size = len(queue)
            for i in range(size):
                row, col, curStep = queue.popleft()
                
                
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    newRow, newCol = row + dx, col + dy
                    newKey = tuple([newRow, newCol])
                    
                    if newRow == entrance[0] and newCol == entrance[1]:
                            return curStep + 1  
                    
                    if 0 <= newRow < nRow and 0 <= newCol < nCol and newKey not in visited and maze[newRow][newCol] != '+':                      
                        queue.append([newRow, newCol, curStep + 1])
                        visited.add(newKey)
        
        return -1
                    
                    
            
            
            