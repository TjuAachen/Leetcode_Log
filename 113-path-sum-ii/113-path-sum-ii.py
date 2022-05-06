# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        path = [root.val]
        final = []
        def find_target(root,targetSum):
            if not root.left and not root.right:
                if targetSum != 0:
                    return False
                elif targetSum == 0:
                    final.append(path[:])
                    return True
#            path = path.append(root.val)
            for nxt in [root.left, root.right]:
                if not nxt:
                    continue
                path.append(nxt.val)
                find_target(nxt,targetSum - nxt.val)
                path.pop()
        find_target(root,targetSum-root.val)
        return final