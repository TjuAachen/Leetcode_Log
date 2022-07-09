# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def preorder(root):
            if not root:
                res.append(str(None))
                return
            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        result = data.split(',')
        root = None
        stack = []
        cur = None
        newNode = None
        for i, elem in enumerate(result):
            if elem != 'None':
                value = int(elem)
                newNode = TreeNode(value)
                if cur:
                    cur.right = newNode
                    cur = None
                elif stack:
                    stack[-1].left = newNode
                stack.append(newNode)
            elif stack:
                cur = stack.pop()
            else:
                cur = None
            if not root:
                root = newNode
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))