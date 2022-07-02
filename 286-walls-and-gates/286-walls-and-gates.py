class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        memoir = {}
        direction = [(1,0),(0,-1),(-1,0),(0,1)]
        m, n = len(rooms), len(rooms[0])
        def distance2gate(i, j, step):
            step = 0
            while(queue):
                size = len(queue)
                for _ in range(size):
                    i, j = queue.popleft()
                    for dx, dy in direction:
                        x, y = i + dx, j + dy
                        if 0 <= x < m and 0 <= y < n and rooms[x][y] != -1:
                            rooms[x][y] = min(rooms[x][y],step + 1)

                            if rooms[x][y] == step + 1 and (x,y) not in visited:
                                queue.append([x,y])
                                visited[(x,y)] = 1
                step = step + 1
         #   del visited[(i,j)]
            return
        queue = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    visited = {}
                    queue.append([i,j])
                    visited[(i,j)] =1
                    distance2gate(i,j, 0)
        