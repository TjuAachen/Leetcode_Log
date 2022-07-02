# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = []
        res = []
        cur = root
        while(cur or stack):
            while(cur):
                stack.append(cur)
                cur = cur.left
            popped = stack.pop()
            res.append(popped.val)
            cur = popped.right
        return res
            