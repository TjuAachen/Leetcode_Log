# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sanitel = ListNode()
        sanitel.next = head
        def swap(head):
            if not head.next:
                return None
            if not head.next.next:
                return head.next
            second = head.next
            third = head.next.next
            
            head.next = third
            second.next = third.next
            third.next = second
            second.next = swap(second)
            return head.next
        return swap(sanitel)
        
            
            
            
            
            
            
            
            
            