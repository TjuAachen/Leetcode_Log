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
        copy = Node(head.val)
        def index(random):
            k = 0
            while(random):
                random = random.next
                k = k +1
            return k
        def insert(node, k):
            start = copy
            while(k>0):
                start = start.next
                k = k - 1
            node.random = start
        p = head.next
        total = 1
        q = copy
        arr = []
        arr.append(index(head.random))
        while(p):
            arr.append(index(p.random))
            q.next = Node(p.val)
            p = p.next
            q = q.next
            total += 1
        begin = copy
        for element in arr:
            index = total - element
            insert(begin,index)
            begin = begin.next
        return copy
            
            
        
        
        
        