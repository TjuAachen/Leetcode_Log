# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        self.targetSum = targetSum
        self.preorder(root)
        
        return self.res
    
    def preorder(self, root):
        if not root:
            return
        self.res += self.numOfPathFromNode(root, self.targetSum)
        self.preorder(root.left)
        self.preorder(root.right)
        
        return
        
    
    
    def numOfPathFromNode(self, startingNode, targetSum):
        if not startingNode:
            return 0
        res = 0
        if startingNode.val == targetSum:
            res += 1
        
        #不选，继续走
        res += self.numOfPathFromNode(startingNode.left, targetSum - startingNode.val)
        res += self.numOfPathFromNode(startingNode.right, targetSum - startingNode.val)
        
        return res