# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        senitel = ListNode()
        senitel.next = head
        pre = senitel
        cur = senitel.next
        def dfs(pre, cur,senitel):
            if not cur:
                return senitel.next
            if cur.val == val:
                pre.next = cur.next
                cur = pre.next
            else:
                pre = pre.next
                cur = cur.next
            return dfs(pre, cur,senitel)
        return dfs(pre,cur,senitel)
        