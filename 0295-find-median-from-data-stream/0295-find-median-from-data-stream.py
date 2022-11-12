from heapq import *
class MedianFinder:

    def __init__(self):
        self.left_length = 0
        self.right_length = 0
        self.left_half = []
        self.right_half = []
        heapify(self.left_half)
        heapify(self.right_half)
        

    def addNum(self, num: int) -> None:
        if self.left_length == self.right_length:
            if not self.left_half or -self.left_half[0] <= num:
                heappush(self.right_half,num)
            else:
                popped = heappop(self.left_half)
                heappush(self.left_half, -num)
                heappush(self.right_half, -popped)
            self.right_length += 1
        else:
            if self.right_half and self.right_half[0] >= num:
                heappush(self.left_half, -num)
            elif self.right_half:
                popped = heappop(self.right_half)
                heappush(self.left_half, -popped)
                heappush(self.right_half, num) 
            self.left_length += 1

    def findMedian(self) -> float:
        if self.left_length == self.right_length:
            return (self.right_half[0]-self.left_half[0])/2
        else:
            return self.right_half[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()