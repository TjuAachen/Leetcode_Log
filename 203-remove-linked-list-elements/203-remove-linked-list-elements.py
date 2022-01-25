# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        if head.val == val:
            if not head.next:
                return None
            head = head.next
        cur = head.next
        pre = head
        while cur:
            if cur.val == val:
                pre.next = cur.next
                cur = pre.next
            else:
                pre = pre.next
                cur = cur.next
        if head.val == val:
            head = head.next
        return head