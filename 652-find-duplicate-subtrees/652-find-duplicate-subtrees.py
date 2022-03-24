# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        record = dict()
        final = []
        def subtree(root):
            if not root:
                return '#'
            left = subtree(root.left)
            right = subtree(root.right)
            sub = left+','+right+','+str(root.val)
            if sub not in record:
                record[sub] = 1
            elif record[sub] == 1:
                final.append(root)
                record[sub] += 1
            return sub
        
        subtree(root)
        return final
        
            
                
                
        
                
            
        
        