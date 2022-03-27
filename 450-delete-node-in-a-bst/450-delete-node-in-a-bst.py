# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def insert(node,root):
            if node.val < root.val:
                if not root.left:
                    root.left = node
                    return
                insert(node, root.left)
            else:
                if not root.right:
                    root.right = node
                    return
                insert(node,root.right)
        stinel = TreeNode(10**5+1)
        stinel.left = root
        def delete(former, root):
            if not root:
                return
            if root.val < key:
                delete(root, root.right)
            elif root.val > key:
                delete(root, root.left)
            else:
                if former.left == root:
                    if root.left and not root.right:
                        former.left = root.left
                    elif root.right and not root.left:
                        former.left = root.right
                    elif not root.right and not root.left:
                        former.left = None
                    else:
                        former.left = root.right
                        insert(root.left, root.right)
                if former.right == root:
                    if root.left and not root.right:
                        former.right = root.left
                    elif root.right and not root.left:
                        former.right = root.right
                    elif not root.right and not root.left:
                        former.right = None
                    else:
                        former.right = root.right
                        insert(root.left, root.right) 
        delete(stinel, root)
        return stinel.left
                
                
        