# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        senitel1, senitel2 = ListNode(), ListNode()
        senitel1.next = list1
        senitel2.next = list2
        r = senitel2
        p, q = list1, list2
        while(p and q):
            if p.val > q.val:
                r.next = q
                r = q
                q = q.next                
            elif p.val <= q.val:
                r.next = p
                r = p
                p = p.next
        if p:
            r.next = p
        if q:
            r.next = q
        return senitel2.next
                

                
        