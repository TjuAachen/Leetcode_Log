"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        queue = []
        queue.append(node)
        old2new = dict()
        if not node:
            return node
        newNode = Node(node.val, [])
        old2new[node] = newNode
        while(queue):
            size = len(queue)
            for i in range(size):
                popped = queue.pop(0)
                for nxt in popped.neighbors:
                    if nxt in old2new:
                        old2new[popped].neighbors.append(old2new[nxt])
                        continue
                    newNode = Node(nxt.val, [])
                    old2new[nxt] = newNode
                    old2new[popped].neighbors.append(old2new[nxt])
                    queue.append(nxt)
        return old2new[node]
                    
        
        