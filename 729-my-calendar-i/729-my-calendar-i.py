from sortedcontainers import SortedDict
class MyCalendar:

    def __init__(self):
        self.calender = SortedDict()
        

    def book(self, start: int, end: int) -> bool:
    #    n = len(self.calender)
        start_index = self.calender.bisect_left(start) - 1
        end_index = self.calender.bisect_left(end) - 1
        s1, e1 = -float('inf'), -float('inf')
        s2, e2 = float('inf'), float('inf')
        if start_index >= 0:
            s1, e1 = self.calender.peekitem(start_index)
        if end_index >= 0:
            s2, e2 = self.calender.peekitem(end_index)
      #  print(s1,e1,s2,e2, start, end)
        if start < e1 or s2 < end <= e2:
            return False
        if s1 == -float('inf') and s2 != float('inf'):
            return False
        if s1 != float('inf') and s1 != s2 and end >= e2:
            return False
   #     print(s1,e1,s2,e2,start,end)
        self.calender[start] = end
        return True
            
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)