# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        length = len(traversal)
        depth2node = {}
        root = None
        j = 0
        while(j < length): 
            #count the depth
            depth = 0
            i = j
            
            while(i < length and traversal[i] == '-'):
                i += 1
            depth = i - j
            #calculate the cur_node
            val = 0
            while(i < length and traversal[i] != '-'):
                val = 10 * val + int(traversal[i])
                i += 1
            newNode = TreeNode(val)
            if not root:
                root = newNode
            if depth - 1 in depth2node:
                parent = depth2node[depth-1]
                if not parent.left:
                    parent.left = newNode
                else:
                    parent.right = newNode
            depth2node[depth] = newNode
            j = i
        return root
            
            
            
            
            
                
            
            