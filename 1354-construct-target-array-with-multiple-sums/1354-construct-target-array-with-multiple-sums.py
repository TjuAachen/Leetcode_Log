from heapq import *
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        max_heap = []
        heapify(max_heap)
        #construct a heap
        for elem in target:
            heappush(max_heap, -elem)
        target_sum = len(target)
        cur_sum = sum(target)
        #deduction till all ones or negative
        if target_sum == 1:
            if cur_sum != 1:
                return False
            else:
                return True
        while(cur_sum != target_sum):
            popped = -heappop(max_heap)
            res = (popped - 1)% (cur_sum - popped)
            if res == popped - 1:
                return False
            else:
                heappush(max_heap, -res - 1)
                cur_sum = cur_sum - popped + res + 1
        return True
                
            
            