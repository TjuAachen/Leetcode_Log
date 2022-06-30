class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.n1, self.n2 = len(v1), len(v2)
        self.v1 = v1
        self.v2 = v2
        self.p1, self.p2 = 0, 0
        self.order = 0
    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            if self.p1 < self.n1 and self.order%2 == 0:
                res = self.v1[self.p1]
                self.p1 += 1
                self.order = 1
            elif self.p2 < self.n2 and self.order%2 == 1:
                res = self.v2[self.p2]
                self.p2 += 1
                self.order = 0
            elif self.p1 < self.n1 and self.p2 == self.n2:
                res = self.v1[self.p1]
                self.p1 += 1
                self.order = 1
            elif self.p2 < self.n2 and self.p1 == self.n1:
                res = self.v2[self.p2]
                self.p2 += 1
                self.order = 0
            return res
            

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.p1 < self.n1  or self.p2 < self.n2:
            return True
        return False
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())