class Node():
    def __init__(self, range_left, range_right):
        self.left = None
        self.right = None
        self.range_left = range_left
        self.range_right = range_right
        self.val = 0, 1 #length, count
        self.range_mid = (range_left + range_right) // 2
    
    def update(self,cur_node, key, val):
        if cur_node.range_left == cur_node.range_right == key:
            cur_node.val = self.merge(cur_node.val, val)
            return
        if key < cur_node.range_left or key > cur_node.range_right:
            return
        cur_node.left = cur_node.left or Node(cur_node.range_left, cur_node.range_mid)
        cur_node.right = cur_node.right or Node(cur_node.range_mid + 1, cur_node.range_right)
        if key <= cur_node.range_mid:
            self.update(cur_node.left, key, val)
        if key > cur_node.range_mid:
            self.update(cur_node.right, key, val)
        cur_node.val = self.merge(cur_node.left.val, cur_node.right.val)
    
    def query(self, cur_node, key):
        if cur_node.range_right <= key:
            return cur_node.val
        if key < cur_node.range_left:
            return (0, 1)
        cur_node.left = cur_node.left or Node(cur_node.range_left, cur_node.range_mid)
        cur_node.right = cur_node.right or Node(cur_node.range_mid + 1, cur_node.range_right)
        left = self.query(cur_node.left, key)
        right = self.query(cur_node.right, key)
        return self.merge(left, right)
    
    def merge(self,v1, v2):
        if v1[0] == v2[0]:
            if v1[0] == 0: return (0, 1)
            return v1[0], v1[1] + v2[1]
        return max(v1, v2)
        
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        root = Node(min(nums), max(nums))
        
        for num in nums:
            length, count = root.query(root, num - 1)
            root.update(root, num, (length+1, count))
        return root.val[1]
        
                