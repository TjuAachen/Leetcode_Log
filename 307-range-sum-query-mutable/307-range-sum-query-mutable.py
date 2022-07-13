class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.n = n - 1
        self.tree = [0] * 4*n
        self.nums = nums
        self.buildTree(1, 0, n - 1)
        
    def buildTree(self, index, left, right):
        if left == right:
            self.tree[index] = self.nums[left]
            return
        mid = left + (right - left) // 2
        self.buildTree(2*index, left, mid)
        self.buildTree(2*index + 1, mid + 1, right)
        self.tree[index] = self.tree[2*index] + self.tree[2*index + 1]
    def updateTree(self, tree_ind, left, right, index, val):
        if left == right == index:
            self.tree[tree_ind] = val
            return
        if right < index or index < left:
            return
        mid = left + (right - left) // 2

        self.updateTree(2*tree_ind, left, mid, index, val)
        
        self.updateTree(2*tree_ind + 1, mid + 1, right, index, val)

        self.tree[tree_ind] = self.tree[2*tree_ind] + self.tree[2*tree_ind + 1]
    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.updateTree(1, 0, self.n, index, val)
        
        
    def inquiry(self, index, left, right, l, r):
        if l <= left and right <= r:
            return self.tree[index]
        if right < l or r < left:
            return 0
        mid = left + (right - left) // 2
        left_part = self.inquiry(2 * index, left, mid, l, r)
        right_part = self.inquiry(2 * index + 1, mid + 1, right, l, r)
        return left_part + right_part
    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.inquiry(1, 0, self.n, left, right)
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)