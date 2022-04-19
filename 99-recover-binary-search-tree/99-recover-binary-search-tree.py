# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        global prev
        global cur
        prev, cur = None, None
        global p,q
        p, q = None, None
        def compare(prev,cur,flag):
            if prev and cur:
                if prev.val > cur.val:
                    if flag:
                        return prev,cur
                    else:
                        return cur
            return None
        global flag
        flag = True
        def revert(root):
            global prev
            global cur
            global flag
            global p, q
            if not root:
                return 
            revert(root.left)
            prev = cur
            cur = root
            temp = compare(prev, cur,flag)
            if temp:
                if p and q:
                    q = temp
                else:
                    p, q = temp
                flag = False
            revert(root.right)
        revert(root)
        p.val, q.val = q.val, p.val
        return root
            
        