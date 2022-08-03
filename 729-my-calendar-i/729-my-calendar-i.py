from sortedcontainers import SortedDict
class MyCalendar:

    def __init__(self):
        self.calender = SortedDict()
        

    def book(self, start: int, end: int) -> bool:
    #    n = len(self.calender)
        start_index = self.calender.bisect(start) - 1
        end_index = start_index + 1
        s1, e1 = -float('inf'), -float('inf')
        s2, e2 = float('inf'), float('inf')
        if start_index >= 0:
            s1, e1 = self.calender.peekitem(start_index)
        if end_index < len(self.calender):
            s2, e2 = self.calender.peekitem(end_index)
      #  print(s1,e1,s2,e2, start, end)
        if e1 <= start and end <= s2:
            self.calender[start] = end
            return True
        return False
            
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)