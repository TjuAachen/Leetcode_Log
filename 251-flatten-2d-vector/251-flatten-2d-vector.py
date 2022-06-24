class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.data = []
        for vector in vec:
            for elem in vector:
                self.data.append(elem)
        self.length = len(self.data)
        self.cur = 0
    def next(self) -> int:
        val = self.data[self.cur]
        self.cur += 1
        return val
        

    def hasNext(self) -> bool:
        if self.cur < self.length:
            return True
        return False
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()