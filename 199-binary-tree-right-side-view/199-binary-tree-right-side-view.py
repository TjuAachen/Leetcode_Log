# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = deque()
        if not root:
            return []
        queue.append(root)
        res = []
        while(queue):
            size = len(queue)
            temp = None
            for i in range(size):
                popped = queue.popleft()
                if not temp:
                    temp = popped
                    res.append(temp.val)
                if popped.right:
                    queue.append(popped.right)
                if popped.left:
                    queue.append(popped.left)
        return res
            
        