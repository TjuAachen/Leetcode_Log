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
        p = l1
        q = l2
        carry = 0
        dummyhead = ListNode()
        cur = dummyhead
        while(p != None or q != None):
            if p != None:
                p_val = p.val
                p = p.next
            else:
                p_val = 0
            if q != None:
                q_val = q.val
                q = q.next
            else:
                q_val = 0  
            cur.next =ListNode((p_val + q_val + carry)%10)
            carry = (p_val + q_val + carry)/10 
            cur = cur.next
        if carry > 0:
            cur.next = ListNode(carry)
        return dummyhead.next
                
        
            
            
            
            
        