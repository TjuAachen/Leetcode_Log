# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        index = 1
        pre, cur = None, head
        assist = None
        while(cur != None):
            if pre == None:
                pre = cur    
            pre = cur
            if assist != None:
                assist = assist.next
            if index == k:
                first = cur
                assist = head
            cur = cur.next
            index += 1
        assist.val, first.val = first.val, assist.val
        return head
        