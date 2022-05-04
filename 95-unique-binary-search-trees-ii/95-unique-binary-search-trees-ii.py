# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        final = []
        def combine(temp,num,left,right):
            n1,n2 = len(left), len(right)
            for i in range(n1):
                for j in range(n2):
                    root = TreeNode(num)
                    root.left = left[i]
                    root.right = right[j]
                    temp.append(root)
        def generate(l):
            if not l:
                return [None]
            if len(l) == 1:
                return [TreeNode(l[0])]
            length = len(l)
            temp = []
            for i in range(length):
                left = generate(l[:i])
                right = generate(l[i+1:])
                combine(temp,l[i],left,right)
            return temp
        return generate([i for i in range(1,n+1)])
            
        
        