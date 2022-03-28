# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sanitel = ListNode()
        sanitel.next = head
        first, second =sanitel, head
        while(second and second.next):
            first.next = second.next
            second.next = second.next.next
            first.next.next = second
            first = first.next.next
            second = first.next
        return sanitel.next
            
            
            
            