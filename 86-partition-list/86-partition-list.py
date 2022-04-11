# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        large = ListNode()
        small = ListNode()
        l = large
        s = small
        cur = head
        while cur:
            nxt = cur.next
            if cur.val < x:
                s.next = cur
                s = s.next
            else:
                l.next = cur
                l = l.next
            cur = nxt
        s.next = large.next
        l.next = None
        return small.next
        