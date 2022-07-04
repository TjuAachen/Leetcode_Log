from heapq import *
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        num = len(ratings)
        minimum = num
        count = [0] * num
        heap = []
        heapify(heap)
        for i, rating in enumerate(ratings):
            heappush(heap, [rating, i])
        seen = {}
        layer = 0
        prev = None
        while(heap):
            popped, index = heappop(heap)
            if index in seen:
                continue
            else:
                seen[index] = 1
                left, right = 0, 0
                if index + 1 in seen and ratings[index + 1] < popped:
                    right = count[index + 1] + 1
                if index - 1 in seen and ratings[index - 1] < popped:
                    left = count[index - 1] + 1
                count[index] = max([left, right, layer])
            if prev and prev < popped:
                layer += 1
        return sum(count) + minimum
            
            
        
            
        