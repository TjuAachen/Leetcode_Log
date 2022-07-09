# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def str_to_int(self, byte_str):
        res = 0
        sym = 1
        for i, num in enumerate(byte_str):
            if i == 0 and num == '-':
                sym = -1
                continue
            elif i == 0 and num == '+':
                continue
            res = res * 256 + ord(num)
        return res*sym
    
    def lenstr_to_int(self, byte_str):
        res = 0
        for i, num in enumerate(byte_str):
            res = res * 256 + ord(num)
        return res
    # represent string length of one layer
    def len_to_str(self,x):
        bytes = [chr(x>>(i*8)&0xff) for i in range(2)]
        bytes.reverse()
        return ''.join(bytes)
    #three bytes to represent the node value
    
    def num_to_str(self,num):
        sym = 1
        if num < 0:
            sym = -1
            num = -num
        bytes = [chr(num>>(i*8)&0xff) for i in range(2)]
        bytes.reverse()
        if sym < 0:
            return '-'+''.join(bytes)
        return '+' + ''.join(bytes)
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        queue = deque()
        queue.append((0,root))
        res = []
        while(queue):
            size = len(queue)
            temp = [self.len_to_str(size * 6)]
            for i in range(size):
                position, popped = queue.popleft()
                temp.extend([self.num_to_str(position), self.num_to_str(popped.val)])
                if popped.left:
                    queue.append((2*i,popped.left))
                if popped.right:
                    queue.append((2*i+1,popped.right))
            res.append(''.join(temp[:]))
        res = ''.join(res)
        return res

    def str_to_nodes(self, prev, string):
        i = 0
        n = len(string)
        cur = []
        while(i < n):
            pos, val = self.str_to_int(string[i:i+3]), self.str_to_int(string[i+3:i+6])
            newNode = TreeNode(val)
            cur.append(newNode)
            if prev:
                parent = prev[pos//2]
                if pos%2 == 0:
                    parent.left = newNode
                else:
                    parent.right = newNode
            i = i + 6
        return cur
            
            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        i = 0
        n = len(data)
        prev = None
        root = None
        while(i < n):
            length_in_str = data[i:i+2]
            cur_len = self.lenstr_to_int(length_in_str)
            i = i + 2
            cur_layer = data[i:i+cur_len]
            nodes = self.str_to_nodes(prev, cur_layer)
            if not root:
                root = nodes[0]
            prev = nodes[:]
            i = i + cur_len
        return root
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))