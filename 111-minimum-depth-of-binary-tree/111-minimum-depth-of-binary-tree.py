from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        count = 0
        if not root:
            return 0
        while(queue):
            size = len(queue)
            count += 1
            for i in range(size):
                cur = queue.popleft()
                if not cur.left and not cur.right:
                    return count
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        