# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        senitel = ListNode(-101)
        senitel.next = head
        pre = senitel
        cur = senitel.next
        def remove(pre, cur, head):
            if not cur:
                return head
            if pre.val == cur.val:
                pre.next = cur.next
                cur = pre.next
                return remove(pre, cur, head)
            else:
                return remove(pre.next,cur.next,head)
        return remove(pre,cur,senitel.next)
        
                