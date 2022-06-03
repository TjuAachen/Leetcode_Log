# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dumb = ListNode()
        
        visited = {}
        def insert(node):
            p = dumb
            while(p.next and p.next.val < node.val):
                p = p.next
            temp = p.next
            p.next = node
            node.next = temp
        r = head
        
        while(r):
            nxt = r.next
            insert(r)
            r = nxt
        return dumb.next
        