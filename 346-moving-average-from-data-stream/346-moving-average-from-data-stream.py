class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window = deque()
        self.sum = 0
    def next(self, val: int) -> float:
        if len(self.window) == self.size:
            popped = self.window.popleft()
            self.window.append(val)
            self.sum = self.sum - popped + val
        else:
            self.window.append(val)
            self.sum += val
        return self.sum / len(self.window)
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)