# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.cur = root
        self.pre = None
    def next(self) -> int:
        while(self.cur):
            if not self.cur.left:
                ans = self.cur.val
                self.cur = self.cur.right
                return ans
            self.pre = self.cur.left
            while(self.pre.right and self.pre.right != self.cur):
                self.pre = self.pre.right
            if self.pre.right:
                self.pre.right = None
                ans = self.cur.val
                self.cur = self.cur.right
                return ans
            else:
                self.pre.right = self.cur
                self.cur = self.cur.left
    def hasNext(self) -> bool:
        if not self.cur:
            return False
        return True
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()