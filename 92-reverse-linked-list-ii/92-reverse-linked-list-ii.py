# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        sanitel = ListNode(-1)
        sanitel.next = head
        prev, cur = None, sanitel
        start, end = None, None
        ind = 0
        left_node = None
        while(ind <= right):
            if ind == left - 1:
                left_node = cur
            if ind == left:
                start = cur
            if ind == right:
                end = cur
            nxt = cur.next
            if ind >= left + 1:
                cur.next = prev
            prev = cur
            cur = nxt
            ind += 1
            
        left_node.next = end
        start.next = cur
        return sanitel.next
        
            
            
        