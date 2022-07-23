class segmentTree:
    def __init__(self, n):
        self.tree = [0] * 4 * n
    
    def update(self,index, left, right, l):
        if left == l and right == l:
            self.tree[index] += 1
            return
        if right < l or l < left:
            return
        mid = left + (right - left) // 2
        self.update(index * 2, left , mid, l)
        self.update(index * 2 + 1, mid + 1, right, l)
        self.tree[index] = self.tree[index * 2] + self.tree[index * 2 + 1]
    
    def query(self,index, left, right, l, r):
        if l <= left and right <= r:
            return self.tree[index]
        if r < left or l > right:
            return 0
        mid = left + (right - left) // 2
        left_part = self.query(2 * index, left, mid, l, r)
        right_part = self.query(2 * index +1, mid + 1, right, l, r)
        return left_part + right_part
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = 2 * 10**4
        offset = 10**4
        tree = segmentTree(n)
        res = []
        for num in reversed(nums):
            new_num = num + offset
            res.append(tree.query(1, 0, 2 * 10**4, 0, new_num - 1))
            tree.update(1, 0, 2*10**4, new_num)
        return reversed(res)
        