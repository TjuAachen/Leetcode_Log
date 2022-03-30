# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        sanitel = ListNode()
        sanitel.next = head
        #head is exclusive
        def reverse(head, k):
            if k == 1:
                return head.next
            p = head.next.next
            end = head.next
            while(k > 1):
                k = k - 1
                r = p.next
                end.next = p.next
                p.next = head.next
                head.next = p
                p = r
            return head.next
        #head is exclusive        
        def reverseK(head, k):
            m = k
            p = head
            while(m > 0):
                if not p:
                    return head.next
                p = p.next
                m = m - 1
            if not p:
                return head.next
            q = head.next
            head.next = reverse(head,k)
            q.next = reverseK(q,k)       
            return head.next
        return reverseK(sanitel,k)
                
            
        