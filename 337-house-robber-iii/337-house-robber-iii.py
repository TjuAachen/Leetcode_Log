# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        res = defaultdict(list)
        def  postorder(root):
            if root not in res:
                res[root] = [0, root.val]
            if not root.left and not root.right:
                return
            if root.left:
                postorder(root.left)
                res[root][1] += res[root.left][0]
                res[root][0] += max([res[root.left][1], res[root.left][0]])
            if root.right:
                postorder(root.right)
                res[root][1] += res[root.right][0]
                res[root][0] += max([res[root.right][1], res[root.right][0]])
            return
        postorder(root)
        return max(res[root][1], res[root][0])
            
        