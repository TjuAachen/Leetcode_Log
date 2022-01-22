# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        deque = [root]
        res = [[root.val]]
        while(deque):
            temp = []
            for i in range(len(deque)):
                elem = deque.pop(0)
                if elem.left:
                    deque.append(elem.left)
                    temp.append(elem.left.val)
                if elem.right:
                    deque.append(elem.right)
                    temp.append(elem.right.val)
            if temp:
                res.append(temp)
        return res

            
                
            
        