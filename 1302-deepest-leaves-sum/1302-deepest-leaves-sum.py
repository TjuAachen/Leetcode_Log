# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        global result
        result = []
        global depth
        depth = 0
        def find(root):
            global depth,result
            if not root.left and not root.left:
                if not result or result[-1][1] < depth:
                    result = [(root.val, depth)]
                elif result and result[-1][1] == depth:
                    result.append((root.val,depth))
            depth += 1
            if root.left:
                find(root.left)
            if root.right:
                find(root.right)
            depth -= 1
        find(root)
        ans = 0
        for elem in result:
            ans += elem[0]
        return ans
                    
            
        