# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preorder,inorder):
            root = TreeNode(preorder[0])
            left_inorder = inorder[:inorder.index(root.val)]
            right_inorder = inorder[inorder.index(root.val)+1:]
            left_preorder = preorder[1:len(left_inorder)+1]
            right_preorder = preorder[len(left_inorder)+1:]
            if len(left_inorder) == 0:
                root.left = None
            elif len(left_inorder) ==1:
                root.left = TreeNode(left_inorder[0])
            else:
                root.left = build(left_preorder,left_inorder)
            if len(right_inorder) == 0:
                root.right = None
            elif len(right_inorder) == 1:
                root.right = TreeNode(right_inorder[0])
            else:
                root.right = build(right_preorder, right_inorder)
            return root
        return build(preorder,inorder)
                
        