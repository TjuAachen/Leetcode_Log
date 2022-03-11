# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sanitel = ListNode()
        sanitel.next = head
        p = head
        q = head
        n = 0
        count = head
        while(count):
            count = count.next
            n = n + 1
        if n != 0:
            for i in range(k%n):
                p = p.next
            while(p.next):
                q = q.next
                p = p.next
            begin = sanitel
            for i in range(k%n):
                r = q.next
                q.next = r.next
                r.next = begin.next
                begin.next = r
                begin = begin.next
        return sanitel.next
            
        
        
            
            