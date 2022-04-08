import heapq 
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.k = k
        n = len(nums)
        if k > n:
            self.min_heap = self.nums
        else:
            self.min_heap = self.nums[(n-k):]
#        heapq.heapify(self.max_heap)
        heapq.heapify(self.min_heap)

    def add(self, val: int) -> int:
        if not self.min_heap or len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap,val)
        elif val > self.min_heap[0]:
            heapq.heappushpop(self.min_heap,val)
        return self.min_heap[0]
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)