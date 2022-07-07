class Node():
    def __init__(self, start, end, parent = None):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None
        self.parent = parent
    
    def update(self, l, r):
        if l > self.end or r < self.start or l > r or self.total == (self.end - self.start + 1):
            return
        if l <= self.start and r >= self.end:
		# not breaking it to leaves trees, thus faster
            delta = self.end - self.start + 1 - self.total
            if delta:
                cur = self
                while cur:
                    cur.total += delta
                    cur = cur.parent
            return

        mid = (self.start + self.end)//2
        if not self.left:
            self.left = Node(self.start, mid, self)
        if not self.right:
            self.right = Node(mid + 1, self.end, self)
        self.left.update(l, r)
        self.right.update(l, r)
            
class CountIntervals:
    def __init__(self):
        self.root = Node(0, 10**9 + 1)
        
    def add(self, left: int, right: int) -> None:
        self.root.update(left, right)

    def count(self) -> int:
        return self.root.total