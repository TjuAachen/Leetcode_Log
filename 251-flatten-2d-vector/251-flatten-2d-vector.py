class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.data = vec
        self.head = 0
        self.cur = 0
        self.total_length = len(self.data)
    def find_nonempty(self):
        while(self.head < self.total_length and self.cur >= len(self.data[self.head])):
            self.head += 1
            self.cur = 0
        
    def next(self) -> int:
        self.find_nonempty()
        val = self.data[self.head][self.cur]
        self.cur += 1
        return val
        

    def hasNext(self) -> bool:
        
        self.find_nonempty()
        return self.head < self.total_length
        
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()