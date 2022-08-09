# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        node_record = defaultdict(list)
        
        def layer_num(root):
            if not root.left and not root.right:
                node_record[0].append(root.val)
                return 0
            left, right = -float('inf'), -float('inf')
            if root.left:
                left = layer_num(root.left)
            if root.right:
                right = layer_num(root.right)
            cur_layer = max(left, right) + 1
            node_record[cur_layer].append(root.val)
            return cur_layer
        max_layer = layer_num(root)
        res = []
        for i in range(max_layer + 1):
            res.append(node_record[i])
        return res
        
        