# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        pre, cur = None, head
        sanitel = ListNode(0)
        sanitel.next = head
        less, larger = None, None
        while(cur != None):
            nxt = cur.next
            if cur.val < x:
                if less == None:
                    less = cur
                    if not sanitel.next:
                        sanitel.next = cur
                    else:
                        temp = sanitel.next
                        sanitel.next = less
                        if not larger:
                            less.next = None
                        else:
                            less.next = temp                            
                elif not less.next:
                    less.next = cur
                else:
                    temp = less.next
                    less.next = cur
                    if not larger:
                        cur.next = None
                    else:
                        cur.next = temp
                less = cur
            else:
                if larger == None:
                    larger = cur
                    if less:
                        less.next = larger
                    else:
                        sanitel.next = larger
                    larger.next = None
                else:
                    larger.next = cur
                    cur.next = None
                    larger = cur
            cur = nxt
        return sanitel.next
                