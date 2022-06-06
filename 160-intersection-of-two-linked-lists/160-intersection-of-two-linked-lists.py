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
        diffA, diffB = 0, 0
        while(pointerA or pointerB):
            if not pointerA:
                diffA += 1
            if not pointerB:
                diffB += 1
            if pointerA:
                pointerA = pointerA.next
            if pointerB:
                pointerB = pointerB.next
        pointerA, pointerB = headA, headB
        while(diffB > 0):
            pointerA = pointerA.next
            diffB = diffB - 1
        while(diffA > 0):
            pointerB = pointerB.next
            diffA = diffA -1
        
        while(pointerA and pointerB):
            if pointerA == pointerB:
                return pointerA
            pointerA = pointerA.next
            pointerB = pointerB.next
        return None
            
                
        