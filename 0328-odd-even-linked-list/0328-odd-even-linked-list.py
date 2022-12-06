# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Assume the head of the linked list is stored in a variable called 'head'

        # Initialize pointers to the head of the odd and even nodes
        if not head:
            return None
        
        odd = head
        even = head.next

        # Set up a pointer to the beginning of the even nodes
        even_head = even

        # Iterate through the linked list and rearrange the nodes
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        # Set the next pointer of the last odd node to the head of the even nodes
        odd.next = even_head
        
        return head
