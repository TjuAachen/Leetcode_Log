class Node:
    def __init__(self,key=0,value=0):
        self.val= value
        self.key = key
        self.prev=None
        self.next=None
        
        
        
        

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.tail.prev = self.head
        self.head.next = self.tail
        self.capacity=capacity
        self.size = 0
        self.dict_key=dict()
    def get(self, key: int) -> int:
        if key not in self.dict_key:
            return -1
        node = self.dict_key[key]
        self.makeRecently(node)
        return node.val
            
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict_key:
            node = self.dict_key[key]
            node.val = value
            self.makeRecently(node)
        else:
            node = Node(key,value)
            self.dict_key[key] = node
            if self.size + 1 > self.capacity:
                self.removeFirst()
                self.addLast(node)
            else:
                self.addLast(node)
                self.size += 1
    def makeRecently(self,node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        if nxt != None:
            nxt.prev = prev
        self.addLast(node)
        
    
    def removeFirst(self):
        first = self.head.next
        self.head.next = first.next
        if first.next:
            first.next.prev = self.head
        del self.dict_key[first.key]
        
        
    def addLast(self,node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        self.tail.prev = node
        node.next = self.tail
              
            
            
                
                
                
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)