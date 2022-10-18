from heapq import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        origin = [0, 0]
    
        for point in points:
            curDistance = self.distance(point, origin)
            if len(heap) < k:
                heappush(heap, [-curDistance, point])
            elif -heap[0][0] > curDistance:
                heappop(heap)
                heappush(heap, [-curDistance, point])
        res = []
        while(heap):
            _, point = heappop(heap)
            res.append(point)
        return res
    
    
    
    def distance(self, p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**(0.5)
        