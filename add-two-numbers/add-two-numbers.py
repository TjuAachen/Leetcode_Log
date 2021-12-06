# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p,q=l1,l2
 #       result=ListNode()
        r=0
        while(p!=None or q!= None):
            if p.val+q.val+r<=9:
                p.val=p.val+q.val+r
                r=0
            else:
                p.val,r=(p.val+q.val+r)%10,(p.val+q.val+r)//10
            if p.next==None and q.next!=None:
                p.next=ListNode()
            elif q.next == None and p.next!=None:
                q.next=ListNode()
            elif p.next==None and q.next==None:
                break
            p=p.next
            q=q.next
        if r>0:
            p.next=ListNode(r)
        return l1
                

                
                
            
            
        

                
        