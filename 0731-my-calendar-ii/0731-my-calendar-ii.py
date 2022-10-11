from sortedcontainers import SortedDict
class MyCalendarTwo:

    def __init__(self):
        self.diff = SortedDict()

    def book(self, start: int, end: int) -> bool:
        #find the first start
        self.diff[start] = self.diff.get(start, 0) + 1
        self.diff[end] = self.diff.get(end, 0) - 1
        cur = res = 0
        for delta in self.diff.values():
            cur += delta
            res = max(cur, res)
        if res >= 3:
            self.diff[start] = self.diff.get(start, 0) - 1
            self.diff[end] = self.diff.get(end, 0) + 1
            if self.diff[start] == 0:
                del self.diff[start]
            
            return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)