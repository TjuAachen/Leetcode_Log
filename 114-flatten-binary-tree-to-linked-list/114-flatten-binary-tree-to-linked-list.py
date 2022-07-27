# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
       # head = root
        #Morris preorder traversal
        def rightmost_in_left_tree(node):
            node = node.left
            while(node.right):
                node = node.right
            return node
        head = TreeNode(-1)
        cur_list = head
        cur = root
        while(cur):
            cur_list.right = cur
            cur_list.left = None
            if cur.left != None:
                rightmost_in_left = rightmost_in_left_tree(cur)
                rightmost_in_left.right = cur.right
                cur = cur.left
            else:
                cur = cur.right
            cur_list = cur_list.right
        return root