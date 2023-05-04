from heapq import *
class SmallestInfiniteSet:

    def __init__(self):
        self.curInteger = 1
        self.addedIntegers = []
        self.addedBack = set()
        

    def popSmallest(self) -> int:
        if self.addedIntegers:
            popped = heappop(self.addedIntegers)
            self.addedBack.remove(popped)
            return popped
        self.curInteger += 1
        return self.curInteger - 1
        
    def addBack(self, num: int) -> None:
        if num >= self.curInteger:
            return
        if num not in self.addedBack:
            self.addedBack.add(num)
            heappush(self.addedIntegers, num)
            return
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)