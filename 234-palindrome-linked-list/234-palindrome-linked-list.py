# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        global left
        left = head
        def validate(head):
            global left
            if not head:
                return True
            if not validate(head.next):
                return False
            res = (left.val == head.val)
            left = left.next
            return res
        return validate(head)
            
        