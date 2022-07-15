from heapq import *
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        heapify(heap)
        N = len(matrix)
        size = min(k, N)
        cur = 0
        
        #initialize
        for i in range(size):
            heappush(heap,[matrix[i][0], i, 0])
        
        while(cur < k):
            val, r, c = heappop(heap)
            if c < N - 1:
                heappush(heap, [matrix[r][c+1], r, c+1])
            cur += 1
        return val
        
        