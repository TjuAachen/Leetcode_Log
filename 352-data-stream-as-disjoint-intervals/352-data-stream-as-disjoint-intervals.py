from sortedcontainers import SortedSet
class SummaryRanges:

    def __init__(self):
        self.find = [i for i in range(10002)]
        self.points = SortedSet()

    def addNum(self, val: int) -> None:
        self.points.add(val)
        self.find[val] = self.find[val + 1]

    def getIntervals(self) -> List[List[int]]:
        ans = []
        for p in self.points:
            if ans and p <= ans[-1][1]:
                continue
            ans.append([p, self.f(p) - 1])
        return ans
    
    def f(self, x):
        if x == self.find[x]:
            return x
        self.find[x] = self.f(self.find[x])
        return self.find[x]
