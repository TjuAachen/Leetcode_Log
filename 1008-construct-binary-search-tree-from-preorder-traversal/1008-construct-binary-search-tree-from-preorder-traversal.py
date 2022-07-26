# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        for num in preorder[1:]:
            newNode = TreeNode(num)
            if stack and stack[-1].val > num:
                
                stack[-1].left = newNode
            else:
                while(stack and stack[-1].val < num):
                    popped = stack.pop()
                popped.right = newNode
            stack.append(newNode)
        return root
                
                
            
        