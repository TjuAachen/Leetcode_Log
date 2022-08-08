from sortedcontainers import SortedDict
class HitCounter:

    def __init__(self):
       # self.timestamp2index = dict()
        self.get_hits_before = SortedDict()

    def hit(self, timestamp: int) -> None:
        if timestamp in self.get_hits_before:
            self.get_hits_before[timestamp] += 1
        else:
           # index = self.get_hits_before.bisect_left(timestamp)
            val = 0
            if len(self.get_hits_before) > 0:
                key, val = self.get_hits_before.peekitem(-1)
            self.get_hits_before[timestamp] = val + 1
        #print(self.get_hits_before)
                
            

    def getHits(self, timestamp: int) -> int:
        if len(self.get_hits_before) == 0:
            return 0
        beginning = max(1, timestamp - 299)
        begin_index = self.get_hits_before.bisect_left(beginning) - 1
        #print(begin_index, end_index, timestamp)
        if begin_index >= len(self.get_hits_before) - 1:
            return 0
        if begin_index == -1:
            begin = 0
        else:
            _, begin = self.get_hits_before.peekitem(begin_index)
        
        _, end = self.get_hits_before.peekitem(-1)
        return end - begin
        
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)