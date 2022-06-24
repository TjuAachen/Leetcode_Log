class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.data = vec
        self.head = 0
        self.cur = 0
        self.total_length = len(self.data)
        if self.total_length == 0:
            self.size = 0
        else:
            #find the first non-empty
            self.find_nonempty()
            if self.head < self.total_length:
                self.size = len(self.data[self.head])
            else:
                self.size = 0
    def find_nonempty(self):
        while(self.head < self.total_length and not self.data[self.head]):
            self.head += 1
        
    def next(self) -> int:
        val = self.data[self.head][self.cur]
        if self.cur + 1 >= self.size:
            self.cur = 0
            self.head += 1
            self.find_nonempty()
            if self.head < self.total_length:
                self.size = len(self.data[self.head])
            else:
                self.size = 0
        else:
            self.cur += 1
        return val
        

    def hasNext(self) -> bool:
        
        if self.head < self.total_length and self.cur < self.size:
            return True
        else:
            return False
        
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()