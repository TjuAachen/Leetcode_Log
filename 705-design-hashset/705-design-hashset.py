class TreeNode():
    def __init__(self,x=0):
        self.val = x
        self.left = None
        self.right = None
class MyHashSet(object):
    

    def __init__(self):
        self.size = 1
        self.l = [None]*self.size

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        hashcode = key%self.size
        if not self.l[hashcode]:
            self.l[hashcode] = TreeNode(key)
        else:
            p = self.l[hashcode]
            while(p):
                if p.val > key:
                    if p.left:
                        p = p.left
                    else:
                        p.left = TreeNode(key)
                        break
                elif p.val < key:
                    if p.right:
                        p = p.right
                    else:
                        p.right = TreeNode(key)
                        break
                else:
                    break
                    
        
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hashcode = key%self.size
     #   dump = TreeNode(-1)
     #   dump.right = self.l[hashcode]
        node = self.find(self.l[hashcode],key)
        if node:
            self.l[hashcode] = self.deleteNode(self.l[hashcode],key) 
    def find(self, root, target):
        if not root:
            return None
        if root.val == target:
            return root
        elif root.val > target:
            return self.find(root.left,target)
        else:
            return self.find(root.right,target)
        
        
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
    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        hashcode = key%self.size
        node =  self.find(self.l[hashcode],key)
        if node:
            return True
        else:
            return False
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)