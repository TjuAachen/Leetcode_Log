# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def pushLeftBranch(p):
            while(p != None):
                stack.append(p)
                p = p.left
        stack = []
        inorder = []
        visited = dict()
        pushLeftBranch(root)
        while(stack):
            p = stack[-1]
            if(not p.left or p.left in visited):
                cur = stack.pop()
                visited[cur] = True
                if inorder and inorder[-1] >= cur.val:
                    return False
                inorder.append(cur.val)
                pushLeftBranch(p.right)
        return True
                
                
        
                
        