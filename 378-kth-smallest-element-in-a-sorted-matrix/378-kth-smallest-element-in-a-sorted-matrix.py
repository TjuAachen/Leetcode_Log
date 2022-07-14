from heapq import *
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        heapify(heap)
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if len(heap) < k:
                    heappush(heap,-matrix[i][j])
                elif -heap[0] > matrix[i][j]:
                    heappop(heap)
                    heappush(heap,-matrix[i][j])
        return -heap[0]
        
        
        