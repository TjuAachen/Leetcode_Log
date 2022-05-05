from collections import deque
class MyStack:

    def __init__(self):
        self.queue_in = deque()
        self.queue_out = deque()
        

    def push(self, x: int) -> None:
        self.queue_in.append(x)
 
    def pop(self) -> int:
        while(len(self.queue_in) > 1):
            self.queue_out.append(self.queue_in.popleft())
        result = self.queue_in.pop()
        while(len(self.queue_out) > 0):
            self.queue_in.append(self.queue_out.popleft())
        return result
    def top(self) -> int:
        while(len(self.queue_in) > 1):
            self.queue_out.append(self.queue_in.popleft())
        result = self.queue_in.pop()
        while(len(self.queue_out) > 0):
            self.queue_in.append(self.queue_out.popleft())
        self.queue_in.append(result)
        return result      
        

    def empty(self) -> bool:
        if len(self.queue_in) == 0 and len(self.queue_out) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()