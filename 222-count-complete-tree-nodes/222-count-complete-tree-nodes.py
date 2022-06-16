# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        #calculate the layer first
        
        right_layer = 0
        left_layer = 0
        left_count, right_count = 0, 0
        
        start = root
        #traverse to the right
        while(start):
            right_count += 2**right_layer
            start = start.right
            right_layer += 1
        
        #traverse to the left
        start = root
        while(start):
            left_count += 2**left_layer
            start = start.left
            left_layer += 1
            
        #if left_layer == right_layer, full binary    
        if left_layer == right_layer:
            return left_count
        
        full_layer = min(left_layer, right_layer) - 1
        def check(root, layer):
            if not root.right:
                return True
            elif layer == full_layer:
                return False
            return check(root.right, layer + 1)
        
        res = 0
        cur_layer = 0
        
        res = 0
        node = root
        while(cur_layer < full_layer and node):
            if not node.left:
                return res
            if check(node.left, cur_layer + 1):
                node = node.left
                res = 2 * res
            elif check(node.right, cur_layer + 1):
                node = node.right
                res = 2 * res + 1
            cur_layer += 1
        if node.left:
            res = 2 * res + 1
        else:
            res = 2 * res
        return res + right_count
                