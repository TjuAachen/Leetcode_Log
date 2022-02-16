# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwo(l1, l2):
            if l1 == None:
                return l2
            if l2 == None:
                return l1
            if l1.val < l2.val:
                l1.next = mergeTwo(l1.next,l2)
                return l1
            elif l1.val > l2.val:
                l2.next = mergeTwo(l1,l2.next)
                return l2
            else:
                l2.next = mergeTwo(l1.next,l2.next)
                l1.next = l2
                return l1                
        def divide(lists):
            n = len(lists)
            if n == 0:
                return None
            if n == 2:
                return mergeTwo(lists[0],lists[1])
            elif n == 1:
                return lists[0]
            return mergeTwo(divide(lists[:n//2]),divide(lists[n//2:]))
        return divide(lists)
                
                
                
                    