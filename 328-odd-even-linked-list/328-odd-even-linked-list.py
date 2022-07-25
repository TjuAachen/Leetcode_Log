# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return 
        odd_head, even_head = ListNode(), ListNode()
        even, odd = even_head, odd_head
        cur = head
        index = 0
        while(cur):
            nxt = cur.next
            if index % 2 == 0:
                even.next = cur
                cur.next = None
                even = even.next
            else:
                odd.next = cur
                cur.next = None
                odd = odd.next
            cur = nxt    
            index += 1
        even.next = odd_head.next
        return even_head.next
        
        