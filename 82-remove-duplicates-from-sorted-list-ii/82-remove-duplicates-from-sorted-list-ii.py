# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode(-101)
        dummyhead.next = head
        def remove(l,prev):
            if not l:
                return None
            p = l
            while(p.next and p.next.val == l.val):
                p = p.next
            if p == l:
                prev = l
            final = remove(p.next,prev)
            if prev != final:
                prev.next = final
            return prev
        return remove(dummyhead,dummyhead).next
            