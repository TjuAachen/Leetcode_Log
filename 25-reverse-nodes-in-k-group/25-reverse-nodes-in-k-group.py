# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sanitel = ListNode()
        sanitel.next = head
        def pullK(p,k):
            while(k > 1):
                if p:
                    p = p.next
                else:
                    return p, False
                k = k - 1
            return p, True
        p = head
        prev = sanitel
        while(True):
            ret = pullK(p, k)
            if not ret[1] or not ret[0]:
                break
            subHead = ret[0]
            sub_r = subHead
            r = prev.next
            index = 0
            while(r != subHead):
                prev.next = r.next
                r.next = subHead.next
                subHead.next = r

                r = prev.next
                if index == 0:
                    sub_r = subHead.next
                index += 1
            p = sub_r.next
            prev = sub_r
        return sanitel.next
            

                

            
        