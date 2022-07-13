# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        queue = deque()
        
        if not root:
            return []
        
        queue.append(root)
        
        while(queue):
            size = len(queue)
            temp = []
            for i in range(size):
                popped = queue.popleft()
                temp.append(popped.val)
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            res.append(temp[:])
        return res