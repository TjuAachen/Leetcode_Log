# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0
        #选择当前root作为startingNode
        #不选择当前root作为startingNode
        if not root:
            return 0
        res += self.pathSum(root.left, targetSum)
        res += self.pathSum(root.right, targetSum)
        
        res += self.numOfPathFromNode(root, targetSum)
        
        return res
        
    
    
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