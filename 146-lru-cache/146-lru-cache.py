class ListNode():
    def __init__(self,val = 0,key=0):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
        self.tail = None
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = 0
        self.head = ListNode(-1,-1)
        self.hash = dict()
        self.tail = self.head
        self.capacity = capacity
        
    def putTail(self,key, node):
        if key in self.hash and node != self.tail:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.tail
            self.tail.next = node
            node.next = None
            self.tail = node
        elif key not in self.hash:
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hash:
            self.putTail(key,self.hash[key])
            return self.hash[key].val
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hash:
            self.hash[key].val = value
            self.putTail(key, self.hash[key])
        else:
            if self.size + 1 > self.capacity:
                LRU = self.head.next
                self.head.next = LRU.next
                del self.hash[LRU.key]
                if self.tail != LRU:
                    LRU.next.prev = self.head
                else:
                    self.tail = self.head
                node = ListNode(value,key)
                self.putTail(key,node)
                self.hash[key] = node
            else:
                self.size += 1
                node = ListNode(value,key)
                self.putTail(key, node)
                self.hash[key] = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)