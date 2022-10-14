# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dumb = ListNode()
        length = self.findLength(head)
        pointer = head
        newPointer = dumb
        i = 0
        while(i < length // 2):
            newPointer.next = pointer
            newPointer = newPointer.next
            pointer = pointer.next
            i += 1
        newPointer.next = None
        pointer = pointer.next
        i += 1
        while(i < length):
            newPointer.next = pointer
            newPointer = newPointer.next
            pointer = pointer.next
            i += 1
        return dumb.next
    
    def findLength(self, head):
        pointer = head
        length = 0
        while(pointer):
            length+= 1
            pointer = pointer.next
        return length