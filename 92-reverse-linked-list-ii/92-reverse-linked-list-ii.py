# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        sanitel = ListNode()
        sanitel.next = head
        global prev
        global successor
        def reverse(head, left, right):
            global prev
            global successor
            if left > 0:
                if left == 1:
                    prev = head
                head.next = reverse(head.next, left - 1, right - 1)
                return head
            elif left == 0 and right > 0:
                newHead = reverse(head.next,0,right - 1)
                prev.next = newHead
                head.next.next = head
                head.next = successor
                return newHead
            elif right == 0 and left == 0:
                head.next = reverse(head.next,0,-1)
                return head
            elif right == -1:
                successor = head
                return head
        return reverse(sanitel,left,right).next
        
                
            
                
        