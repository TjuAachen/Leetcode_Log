# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def swap(head):
            if not head or not head.next:
                return head

            newHead = head.next
            head.next = swap(newHead.next)
            newHead.next = head
            return newHead
        return swap(head) #swap(sanitel).next
        
            
            
            
            
            
            
            
            
            