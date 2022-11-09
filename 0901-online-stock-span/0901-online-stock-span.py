from sortedcontainers import SortedList
class StockSpanner:

    def __init__(self):
        
        self.res = []
        self.array = []
        self.monoStack = []
        self.leftFirstLess = defaultdict()
        

    def next(self, price: int) -> int:
        
        n = len(self.array)
        while(self.monoStack and self.monoStack[-1][0] <= price):
            self.monoStack.pop()
        
        idx = -1
        
        if self.monoStack:
            val, idx = self.monoStack[-1]
            self.leftFirstLess[n] = idx
        
        self.monoStack.append([price, n])
        curRes = n - idx
        
        self.res.append(curRes)
        self.array.append(price)
        
        return self.res[-1]
        
            
        
        
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)