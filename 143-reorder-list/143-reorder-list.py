# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        global pos, p, r
        dumb = ListNode()
        r = dumb
        p = head
        visited = {}
        def reorder(head):
            global pos, p, r
            if not head:
                return
            reorder(head.next)
            if head in visited or (p in visited or not p):
                r.next = None
                return
            #p is forward
            r.next = p
            r = r.next
            visited[p] = 1
            p = p.next
            if head not in visited:
                r.next = head
                r = r.next
                visited[head] = 1

            #head is backward
            
            
            
        reorder(head)
        return dumb.next