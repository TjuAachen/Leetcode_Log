# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(preorder, postorder):
            root = TreeNode(preorder[0])
            if len(preorder) == 1:
                return root
            else:
                left = preorder[1]
                left_ind = postorder.index(left)
                len_left = left_ind + 1
                left_preorder = preorder[1:len_left+1]
                left_postorder = postorder[0:left_ind+1]
                right_preorder=preorder[len_left+1:]
                right_postorder = postorder[left_ind+1:len(postorder)-1]
                len_right = len(right_preorder)
                if len_left == 0:
                    root.left = None
                elif len_left == 1:
                    root.left = TreeNode(left_preorder[0])
                else:
                    root.left = build(left_preorder,left_postorder)
                if len_right == 0:
                    root.right = None
                elif len_right == 1:
                    root.right = TreeNode(right_preorder[0])
                else:
                    root.right = build(right_preorder,right_postorder)         
            return root
        return build(preorder,postorder)
        