class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        nrow, ncol = len(matrix), len(matrix[0])
        result = dict()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(node):
            if tuple(node) in result:
                return result[tuple(node)]
            count = 0
            for dx, dy in directions:
                newx, newy = node[0] + dx, node[1] + dy
                if 0 <= newx < nrow and 0 <= newy < ncol and matrix[newx][newy] > matrix[node[0]][node[1]]:
                    count = max(count,dfs([newx, newy]))
            result[tuple(node)] = count + 1
            return result[tuple(node)]
        res = 0
        for row in range(nrow):
            for col in range(ncol):
                res = max(res, dfs([row, col]))
        return res
                    
            
        
        