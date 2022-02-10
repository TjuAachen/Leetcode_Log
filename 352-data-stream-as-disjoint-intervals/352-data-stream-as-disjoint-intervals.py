class SummaryRanges:
    def search(self,tar, ind):
        left, right = 0, len(self.res)
        while(left < right):
            mid = left + ((right - left ) >> 1)
            if self.res[mid][1] >= tar:
                right = mid
            else:
                left = mid + 1
        return left
    def __init__(self):
        self.arr = []
        self.record = dict()
        self.res = []

    def addNum(self, val: int) -> None:
        self.arr.append(val)
        if not self.res:
            self.res = [[val, val]]
            self.record[val] = True
            return
        if val not in self.record:
            self.record[val] = True
            if val + 1 in self.record and val - 1 in self.record:
                ind = self.search(val-1,1)
                self.res[ind][1] = self.res[ind+1][1]
                del self.res[ind+1]
            elif val + 1 in self.record:
                ind = self.search(val+1,0)
                self.res[ind][0] = val
            elif val - 1 in self.record:
                ind = self.search(val-1,1)
                self.res[ind][1] = val
            else:
                ind = self.search(val,1)
                self.res.insert(ind,[val,val])
                        
    def getIntervals(self) -> List[List[int]]:
        return self.res
        
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()