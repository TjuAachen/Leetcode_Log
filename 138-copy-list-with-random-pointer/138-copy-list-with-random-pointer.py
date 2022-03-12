"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        sanitel = Node(0)
        q = sanitel
        p = head
        record = dict()
        def copy(p,q):            
            if not p:
                return
            if p not in record:
                q.next = Node(p.val)
                record[p] = q.next
            else:
                q.next = record[p]
            if p.random in record:
                q.next.random = record[p.random]
            else:
                if p.random:
                    q.next.random = Node(p.random.val)
                else:
                    q.next.random = None
                record[p.random] = q.next.random
            if p.next in record:
                q.next.next = record[p.next]
            else:
                if p.next:
                    q.next.next = Node(p.next.val)
                else:
                    q.next.next = None
                record[p.next] = q.next.next
            copy(p.next,q.next)
            return 
        copy(p,q)
        return sanitel.next

            
            
        
        
        
        
        