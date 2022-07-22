# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head1, head2 = ListNode(0), ListNode(0)
        p1, p2 = head1, head2
        
        cur = head
        
        while(cur):
            nxt = cur.next
            if cur.val < x:
                p1.next = cur
                cur.next = None
                p1 = p1.next
            else:
                p2.next = cur
                cur.next = None
                p2 = p2.next                
            cur = nxt
        p1.next = head2.next
        return head1.next
                