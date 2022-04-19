# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pre, cur = None, root
        res = []
        while(cur != None):
            if cur.left == None:
                res.append(cur.val)
                cur = cur.right
                continue
            pre = cur.left
            while(pre.right != None and pre.right != cur):
                pre = pre.right
            if(pre.right == None):
                pre.right = cur
                cur = cur.left
            else:
                pre.right = None
                res.append(cur.val)
                cur = cur.right
            
        return res
        