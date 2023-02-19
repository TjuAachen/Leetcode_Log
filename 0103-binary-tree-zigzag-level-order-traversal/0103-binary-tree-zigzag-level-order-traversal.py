# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        #final result
        results = []
        self.dfs(root, 0, results)
        
        return results
        
    def dfs(self, root, level, results):
        if level >= len(results):
            results.append(deque([root.val]))
        else:
            if level % 2 == 0:
                results[level].append(root.val)
            else:
                results[level].appendleft(root.val)
        if root.left:
            self.dfs(root.left, level + 1, results)
        if root.right:
            self.dfs(root.right, level + 1, results)
        
        