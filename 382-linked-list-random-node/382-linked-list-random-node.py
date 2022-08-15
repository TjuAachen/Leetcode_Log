import random
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        #reservoir sampling
        self.rand = head.val
        self.head = head
        

    def getRandom(self):
        """
        :rtype: int
        """
        count = 0
        cur = self.head
        choice = self.head.val
        while(cur):
            if random.randint(0, count) == 0:
                choice = cur.val
            cur = cur.next
            count += 1
        return choice
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()