from heapq import *
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        heapify(heap)
        heightNum = len(heights)
        if ladders >= heightNum - 1:
            return heightNum - 1
        for i in range(1, heightNum):
            cur_diff = heights[i] - heights[i-1]
            if cur_diff <= 0:
                continue
            if ladders > 0:
                ladders = ladders - 1
                heappush(heap,cur_diff)
                continue
            if heap and heap[0] < cur_diff:
                popped = heappop(heap)
                heappush(heap, cur_diff)
                if bricks < popped:
                    return i - 1
                else:
                    bricks = bricks - popped
            else:
                if bricks < cur_diff:
                    return i - 1
                else:
                    bricks = bricks - cur_diff
        return i
        
        