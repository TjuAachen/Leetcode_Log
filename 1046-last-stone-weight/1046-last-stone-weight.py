import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heapq._heapify_max(stones)
        while(len(stones) > 1):
            stone1, stone2 = heapq._heappop_max(stones), heapq._heappop_max(stones)
            if stone1 != stone2:
                new = max(stone1,stone2) - min(stone1,stone2)
                heapq.heappush(stones,new)
                heapq._heapify_max(stones)
        if not stones:
            return 0
        return list(stones)[0]
        