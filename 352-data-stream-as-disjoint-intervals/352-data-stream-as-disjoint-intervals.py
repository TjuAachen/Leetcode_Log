class SummaryRanges:

    def __init__(self):
        self.arr = []

    def addNum(self, val: int) -> None:
        self.arr.append(val)

    def getIntervals(self) -> List[List[int]]:
        temp = []
        self.arr.sort()
        res = []
        for i in self.arr:
            if not temp:
                temp = [i, i]
            if i - temp[-1] == 1:
                temp[-1] = i
            elif i - temp[-1] != 0:
                res.append(temp)
                temp = [i, i]
        if temp:
            res.append(temp)
        return res
            
                
                
                
                
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()