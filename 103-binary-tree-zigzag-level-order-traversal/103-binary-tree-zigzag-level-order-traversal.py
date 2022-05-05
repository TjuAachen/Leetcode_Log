from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        final = []
        is_reverse = False
        

        if not root:
            return final
        
        
        while(queue):
            size = len(queue)
            temp = []
                        
            for i in range(size):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:    
                    queue.append(cur.right)
                    
                if is_reverse:
                    temp = [cur.val] + temp
                else:
                    temp.append(cur.val)
            
            
            final.append(temp)
            is_reverse = (not is_reverse)
        return final
                
                    
        