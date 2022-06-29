from heapq import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        res = []
        final = []
        heapify(res)
        def in_order(root):
            if not root:
                return
            in_order(root.left)
            cur = - abs(root.val - target)
            if len(res) < k:
                heappush(res, [cur, root.val])
            elif res[0][0] < cur:
                heapreplace(res, [cur, root.val])
            in_order(root.right)
        in_order(root)
        for elem, val in res:
            final.append(val)
        return final
        