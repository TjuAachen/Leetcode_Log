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
        if not head:
            return head
        senitel = ListNode(-101)
        senitel.next = head
        pre = senitel
        cur = senitel.next
        while cur:
            if cur.val == pre.val:
                pre.next = cur.next
                cur = pre.next
            else:
                pre = pre.next
                cur = cur.next
        return senitel.next
        