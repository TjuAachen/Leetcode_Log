class ListNode:
    def __init__(self,key=-1,val=-1):
        self.key = key
        self.val = val
        self.next = None
        
class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.array = [None]*self.size
    def put(self, key: int, value: int) -> None:
        hashcode = key % self.size
        p = self.array[hashcode]
        prev = None
        while(p):

            if p.key != key:
                prev = p
                p = p.next
            else:
                p.val = value
                return
        if prev:
            prev.next = ListNode(key, value)
        else:
            self.array[hashcode] = ListNode(key, value)
                

    def get(self, key: int) -> int:
        hashcode = key % self.size
        p = self.array[hashcode]
        while(p):
            if p.key != key:
                p = p.next
            else:
                return p.val
        return -1
        

    def remove(self, key: int) -> None:
        hashcode = key % self.size
        p = self.array[hashcode]
        prev = None
        while(p):
            if p.key != key:
                prev = p
                p = p.next
            else:
                if prev:
                    prev.next = p.next
                    del p
                else:
                    self.array[hashcode] = p.next
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)