# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        index = 1
        pre, cur = None, head
        record = dict()
        while(cur != None):
            if pre == None:
                pre = cur    
            pre = cur
            record[index] = cur
            cur = cur.next
            index += 1
        record[k].val, record[len(record) + 1-k].val = record[len(record) + 1-k].val, record[k].val
        return head
        