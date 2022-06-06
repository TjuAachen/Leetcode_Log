# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pointerA, pointerB = headA, headB
        while(pointerA != pointerB):
            if pointerA:
                pointerA = pointerA.next
            else:
                pointerA = headB
            if pointerB:
                pointerB = pointerB.next
            else:
                pointerB = headA
        return pointerA
        
            
                
        