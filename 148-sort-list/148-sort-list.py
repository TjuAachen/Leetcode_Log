# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        def sort(head):
            if not head.next:
                return head
            #divide the list into two halves
            fast, slow = head, head
            while(slow and slow.next):
                fast = fast.next
                slow = slow.next.next
            if fast.next:
                second_half = fast.next
                fast.next = None
            else:
                second_half = fast
                head.next = None
            first_half = head
            sorted_first_half = sort(first_half)
            sorted_second_half = sort(second_half)
            return merge(sorted_first_half, sorted_second_half)
            
            
            
        def merge(head1, head2):
            p, q = head1, head2
            dumb = ListNode()
            r = dumb
            while(p and q):
                if p.val > q.val:
                    r.next = q
                    q = q.next
                    r = r.next
                else:
                    r.next = p
                    p = p.next
                    r = r.next
            if p:
                r.next = p
            else:
                r.next = q
            return dumb.next
        
        return sort(head)
        