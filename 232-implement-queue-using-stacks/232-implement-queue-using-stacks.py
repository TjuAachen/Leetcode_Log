class MyQueue:

    def __init__(self):
        self.top = -1
        self.stack_in = []
        self.stack_out = []
        

    def push(self, x: int) -> None:
        if not self.stack_in:
            self.top = x
        self.stack_in.append(x)
        

    def pop(self) -> int:
        while(self.stack_in):
            self.stack_out.append(self.stack_in.pop())
        result = self.stack_out.pop()
        if self.stack_out:
            self.top = self.stack_out[-1]
        while(self.stack_out):
            self.stack_in.append(self.stack_out.pop())
        return result

    def peek(self) -> int:
        return self.top
        

    def empty(self) -> bool:
        if(len(self.stack_in) == 0 and len(self.stack_out) == 0):
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()