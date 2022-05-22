"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur = root

        flag = True
        while(cur):
            #set the next
            if flag == True:
                if cur.left:
                    nxt = cur.left
                else:
                    nxt = cur.right
                flag = False
            #find the next real pointer
            p = cur.next
            if not p:
                if cur.left:
                    cur.left.next = cur.right
                    cur.right.next = None
                    cur = nxt
                    flag = True
                    continue
                else:
                    break
            if cur.left:
                cur.left.next = cur.right
                cur.right.next = p.left
                cur = p
            else:
                break
        return root
        
        