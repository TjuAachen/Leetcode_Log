# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        dump = TreeNode(-10**5-1)
        dump.right = root
        def find(root,key):
            if not root:
                return None, None
            if root.left and root.left.val == key:
                return root,root.left
            elif root.right and root.right.val == key:
                return root,root.right
            elif root.val < key:
                return find(root.right, key)
            else:
                return find(root.left,key)
        parent,node = find(dump, key)
        if not node:
            return dump.right
        if not node.left and node.right:
            node.val, node.right.val = node.right.val, node.val
            node.left, node.right = node.right.left, node.right.right
        #    node.right = node.right.right
        elif not node.right and node.left:
            node.val, node.left.val = node.left.val, node.val
            node.left, node.right = node.left.left, node.left.right 
        #    node.right = node.left.right 
        elif not node.right and not node.left:
            if parent.val > key:
                parent.left = None
            else:
                parent.right = None
        else:
            prev,p = node ,node.left
            while(p.right):
                prev = p
                p = p.right
            node.val = p.val
            if prev == node:
                prev.left = p.left
            else:
                prev.right = p.left
        return dump.right
            
        