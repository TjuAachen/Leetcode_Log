# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseEvenLengthGroups(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #head is exclusive
        def reverse(head,k):
            b = head
            a = head.next
            if k == 1:
                return a
            while(k>-1):
                b = b.next
                if not b:
                    break
                k = k - 1
            pre = None
            cur = a
            nxt = a
            while(cur != b):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur =  nxt
            return pre
        #head is exclusive
        def reverseK(head, k):
            p = head
            m = k
            while(k > 0):
                k = k - 1
                p = p.next
                if not p:
                    if (m-k+1)%2 != 0:
                        return head.next
                    else:
                        return reverse(head,m)
            if m%2 != 0:
                p.next = reverseK(p,m+1)
                return head.next
            tail = head.next
            nextHead = reverseK(p,m+1)
            newHead = reverse(head, m)
            head.next = newHead
            tail.next = nextHead
            return head.next
        sanitel = ListNode()
        sanitel.next = head
        return reverseK(sanitel,1)

                
            
            
        