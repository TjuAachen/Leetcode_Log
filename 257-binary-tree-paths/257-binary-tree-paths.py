# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stack = [['',root]]
        path =''
        res = []
        while stack:
            elem = stack.pop()
            path, cur = elem[0], elem[1]
            if cur != root:
                path += '->'+str(cur.val)
            else:
                path += str(cur.val)
            if cur.left == cur.right:
                res.append(path)           
            else:
                if cur.left:
                    stack.append([path,cur.left])
                if cur.right:
                    stack.append([path,cur.right])
        return res
            