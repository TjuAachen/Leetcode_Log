# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        global root
        root = None
        def construct(preorder, inorder):
            global root
            if not preorder and not inorder:
                return None            
            head = TreeNode(preorder[0])
            
            if not root:
                root = head
            
            i = 0
            n_inorder = len(inorder)
            while(i < n_inorder and inorder[i] != head.val):
                i = i + 1
            left_inorder = inorder[:i]
            right_inorder = inorder[i+1:]
            n_left_inorder = len(left_inorder)
            n_right_inorder = len(right_inorder)
            
            left_preorder = preorder[1:n_left_inorder+1]
            right_preorder = preorder[n_left_inorder+1:]
            
            left_node = construct(left_preorder, left_inorder)
            right_node = construct(right_preorder, right_inorder)
            head.left = left_node
            head.right = right_node
            return head
        construct(preorder, inorder)
        return root
            
            
            
        