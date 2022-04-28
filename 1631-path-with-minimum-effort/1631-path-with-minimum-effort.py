class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        nrow, ncol = len(heights), len(heights[0])
        max_value, min_value = max([max(heights[i]) for i in range(nrow)]), min([min(heights[i]) for i in range(nrow)])
        def check(val,i,j):
          #  print(val,i,j)
            if i == nrow-1 and j == ncol - 1:
                return True
            dire = [(-1,0),(0,1),(0,-1),(1,0)]
            visited[(i,j)] = 1
            for dx,dy in dire:
                newX, newY = i+dx, j+dy
                if 0 <= newX < nrow and 0 <= newY < ncol and (newX,newY) not in visited:
                    if abs(heights[newX][newY] - heights[i][j] ) <= val:
                        visited[(newX,newY)] = 1
                        if check(val, newX, newY):
                       #     del visited[(newX,newY)]
                            return True
                   # del visited[(newX,newY)]
            return False
        left, right = 0, 10**6
        while(left < right):
            mid = left + (right - left) // 2
            visited = dict()
            if check(mid,0,0):
                right = mid
                    
            else:
                left = mid + 1
        return left
                
            
                
                