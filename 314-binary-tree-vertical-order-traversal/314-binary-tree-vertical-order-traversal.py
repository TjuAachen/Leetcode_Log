# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = defaultdict(list)
        queue = deque()
        queue.append([root,0,0])
    
        while(queue):
            size = len(queue)
            for i in range(size):
                node_popped, row_popped, col_popped = queue.popleft()
                res[col_popped].append(node_popped.val)
                if node_popped.left:
                    queue.append([node_popped.left, row_popped +1, col_popped - 1])
                if node_popped.right:
                    queue.append([node_popped.right, row_popped +1, col_popped + 1])
        ans = []
        for col in sorted(res.keys()):
            ans.append(res[col])
        return ans
        
            