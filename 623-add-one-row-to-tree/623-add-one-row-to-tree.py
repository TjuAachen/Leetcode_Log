# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        #1. input : root
        #2. output : dumb.left
        #3. breaking down the problem:
        #3.1. set the dumb node and attach the root to the left
        #3.2. start from the dumb node, traverse nodes in a bfs way.
        #3.3 when the depth is equal to depth - 1, then stop the traversal, create a copy node of that node and also copy its left, right subtrees
        dumb = TreeNode()
        dumb.left = root
        queue = deque()
        self.bfs(dumb, queue, depth)
        for originNode in queue:
            copyNodeLeft = TreeNode(val)
            copyNodeRight = TreeNode(val)
            left = originNode.left
            right = originNode.right
            originNode.left = copyNodeLeft
            originNode.right = copyNodeRight
            copyNodeLeft.left = left
            copyNodeRight.right = right
        return dumb.left
        
        
    
    
    def bfs(self, root, queue, depth):
        queue.append(root)
        curDepth = 0
        while(queue):
            if curDepth == depth - 1:
                break
            size = len(queue)
            for i in range(size):
                popped = queue.popleft()
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            curDepth += 1
            
            
        
        
        
        
        
        