class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.vectors = [v1, v2]
        self.queue = deque()
        for index, vector in enumerate(self.vectors):
            if len(vector) > 0:
                self.queue.append((index,0))
        
    def next(self):
        """
        :rtype: int
        """
        res = None
        if self.queue:
            cur_vec_ind, cur_elem_ind = self.queue.popleft()
            res = self.vectors[cur_vec_ind][cur_elem_ind]
            if cur_elem_ind + 1< len(self.vectors[cur_vec_ind]):
                cur_elem_ind += 1
                self.queue.append((cur_vec_ind, cur_elem_ind))
        return res
        
            

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.queue:
            return True
        return False
        
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())