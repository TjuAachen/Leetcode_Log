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
        queue = deque()
        if not root:
            return None
        queue.append(root)
        while queue:
            size = len(queue)
            pre, nxt = None, None
            for i in range(size):
                pre = nxt
                nxt = queue.pop()
                nxt.next = pre
                if nxt.right:
                    queue.appendleft(nxt.right)
                if nxt.left:
                    queue.appendleft(nxt.left)
        return root
        