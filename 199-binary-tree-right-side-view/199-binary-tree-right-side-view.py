from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #right most
        res = []
        queue = deque()
        if not root:
            return res
        queue.append(root)
        while(queue):
            size = len(queue)
            for i in range(size):
                popped = queue.popleft()
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            res.append(popped.val)
        return res
            
        