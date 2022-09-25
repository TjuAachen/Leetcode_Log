class MyCircularQueue:
    
    def __init__(self, k: int):
        self.queue = [-1] * k
        self.front, self.rear = 0, 0
        self.k = k
        
    def enQueue(self, value: int) -> bool:
        k = self.k
        if self.isFull():
            return False
        self.queue[self.rear%k] = value
        self.rear += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        k = self.k
        self.queue[self.front%k] = -1
        self.front += 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front%self.k]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        k = self.k
        return self.queue[(self.rear - 1)%k]
        

    def isEmpty(self) -> bool:
        return (self.rear - self.front == 0)

    def isFull(self) -> bool:
        if (self.rear - self.front) == self.k:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()