# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sanitel = ListNode(-101)
        sanitel.next = head
        p = sanitel.next
        q = sanitel
        while(p):
            r = p
            while(r.next and r.val == r.next.val):
                r = r.next
            if r == p:
                q.next = p
                q = q.next
                p = p.next
            else:
                p = r.next
        q.next = p
        return sanitel.next
        
            
            
            
        