class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        global left_most, right_most, up_most, low_most
        left_most, right_most = float('inf'), -float('inf')
        low_most, up_most = -float('inf'), float('inf')
        
        m, n = len(image), len(image[0])
        
        visited = set()
        diff = [(-1,0), (0,1),(1,0),(0,-1)]
        
        
        def dfs(x, y):
            global left_most, right_most, up_most, low_most
            if image[x][y] == '0':
                return
            visited.add((x,y))
            left_most, right_most = min(left_most, y), max(right_most, y)
            low_most, up_most = max(low_most, x), min(up_most, x)
            for dx, dy in diff:
                newx, newy = x + dx, y + dy
                if 0 <= newx < m and 0 <= newy < n and (newx, newy) not in visited:
                    dfs(newx, newy)
            return
        
        dfs(x,y)
        return (low_most - up_most + 1) * (right_most - left_most + 1)
                    
        