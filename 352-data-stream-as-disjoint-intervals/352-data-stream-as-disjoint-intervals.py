from sortedcontainers import SortedSet
class UnionFind:
    def __init__(self, N):
        self.parent = []
        self.size = []
        for i in range(N):
            self.parent.append(i)
            
    def find(self,x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
class SummaryRanges:
    def __init__(self):
        self.arr = SortedSet()
        self.dsu = UnionFind(10001)

    def addNum(self, val: int) -> None:
        self.arr.add(val)
        self.dsu.parent[val] = val + 1
                
    def getIntervals(self) -> List[List[int]]:
        res = []
        for num in self.arr:        
            if not res:                
                res = [[num, self.dsu.find(num)-1]]            
            if num > self.dsu.find(res[-1][1]):
                res.append([num, self.dsu.find(num)-1])
            else:
                res[-1][1] = self.dsu.find(num) - 1
        return res
        
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()