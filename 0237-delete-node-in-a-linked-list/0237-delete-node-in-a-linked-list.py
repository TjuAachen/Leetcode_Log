# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prevTail = node;
        
        while(node.next):
            node.val = node.next.val
            node = node.next
            if(prevTail.next != None and prevTail.next.next != None):
                prevTail = prevTail.next;
            
        prevTail.next = None
            
        