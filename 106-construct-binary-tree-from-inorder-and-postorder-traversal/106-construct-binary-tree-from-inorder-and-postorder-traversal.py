# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(inorder, postorder):
            root = TreeNode(postorder[-1])
            root_ind = inorder.index(root.val)
            left_inorder = inorder[:root_ind]
            right_inorder = inorder[root_ind+1:]
            len_left, len_right = len(left_inorder), len(right_inorder)
            left_postorder = postorder[:len_left]
            right_postorder = postorder[len_left:len(postorder)-1]
            if len_left == 0:
                root.left = None
            elif len_left == 1:
                root.left = TreeNode(left_inorder[0])
            else:
                root.left = build(left_inorder,left_postorder)
            if len_right == 0:
                root.right = None
            elif len_right == 1:
                root.right = TreeNode(right_inorder[0])
            else:
                root.right = build(right_inorder,right_postorder)           
            return root
        return build(inorder,postorder)
            
        