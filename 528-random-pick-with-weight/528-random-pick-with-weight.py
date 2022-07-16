import random
from bisect import *
class Solution:
    def prefix_sum(self):
        n = len(self.w)
        prefix = [0] * (n + 1)
        for i in range(1,n+1):
            prefix[i] = prefix[i-1] + self.w[i-1]
        return prefix
    
    def __init__(self, w: List[int]):
        self.w = w
        self.prefix = self.prefix_sum()
        self.minimum, self.maximum = 1, self.prefix[-1]
        
    def pickIndex(self) -> int:
        selected_num = random.randint(self.minimum, self.maximum)
        index = bisect_left(self.prefix, selected_num) 
        return index - 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()