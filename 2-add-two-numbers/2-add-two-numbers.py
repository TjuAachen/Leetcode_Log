# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = l1
        n2 = l2
        root = ListNode(-1)
        next_pos = 0
        while(n1 and n2):            
            this = (n1.val + n2.val + next_pos)%10
            temp = (n1.val + n2.val + next_pos)/10
            if root.val == -1:
                root.val = this
                cur = root
            else:
                cur.next = ListNode(this)
                cur = cur.next
            n1 = n1.next
            n2 = n2.next
            next_pos = temp
        if n1:
            final = n1
            while(next_pos > 0 and final):
                temp = (final.val + next_pos)/10
                final.val = (final.val + next_pos)%10
                next_pos = temp
                if final.next:
                    final = final.next
                else:
                    break
            if next_pos > 0:
                final.next = ListNode(next_pos)
            cur.next = n1
            
        elif n2:
            final = n2
            while(next_pos > 0 and final):
                temp = (final.val + next_pos)/10
                final.val = (final.val + next_pos)%10
                next_pos = temp
                if final.next:
                    final = final.next
                else:
                    break
            if next_pos > 0:
                final.next = ListNode(next_pos)
            cur.next = n2
        else:
            if(next_pos>0):
                cur.next = ListNode(next_pos)
        return root
        
            
            
            
            
        