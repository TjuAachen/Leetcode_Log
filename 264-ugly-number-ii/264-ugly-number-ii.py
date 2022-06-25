from heapq import *
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyNums = []
        heap = []
        heapify(heap)
        exponent_num = 0
        cur_minimum = 2**exponent_num
        while(len(heap) < n or (-heap[0] > cur_minimum)):
            #generate ugly nums
            for i in range(exponent_num+1):
                for j in range(exponent_num + 1- i):
                    cur = 2**i * 3**j * 5**(exponent_num-i-j)
                    if len(heap) < n:
                        heappush(heap, -cur)
                    elif -heap[0] > cur:
                        heapreplace(heap, -cur)
            exponent_num += 1
            cur_minimum = 2**exponent_num
        return -heap[0]
                
        
                
        
                        