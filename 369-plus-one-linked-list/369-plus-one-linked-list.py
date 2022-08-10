# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def res(head):
            if not head:
                return 1
            add = res(head.next)
            if head.val + add == 10:
                head.val = 0
                return 1
            head.val += add
            return 0
        first = res(head)
        if first != 0:
            newHead = ListNode(first)
            newHead.next = head
            return newHead
        return head