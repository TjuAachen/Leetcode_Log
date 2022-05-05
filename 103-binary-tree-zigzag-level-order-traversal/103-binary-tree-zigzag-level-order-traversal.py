from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue_reverse = deque()
        queue_normal = deque()
        queue_normal.append(root)
        queue_reverse.append(root)
        final = []
        is_reverse = False
        
        
        
        if not root:
            return final
        
        
        
        while(queue_normal):
            size = len(queue_normal)
            temp = []
                        
            for i in range(size):
                cur_reverse = queue_reverse.popleft()
                if cur_reverse.right:
                    queue_reverse.append(cur_reverse.right)
                if cur_reverse.left:    
                    queue_reverse.append(cur_reverse.left)
                    
                cur_normal = queue_normal.popleft()    
                if cur_normal.left:
                    queue_normal.append(cur_normal.left)
                if cur_normal.right:
                    queue_normal.append(cur_normal.right)
                if is_reverse:
                    temp.append(cur_reverse.val)
                else:
                    temp.append(cur_normal.val)
            
            
            final.append(temp)
            is_reverse = (not is_reverse)
        return final
                
                    
        