class NumArray:
    def lowbit(self, num):
        return num&(-num)
    
    def point_update(self, index, delta):
        i = index
        
        while(i < self.n):
            self.bit[i] += delta
            i += self.lowbit(i)
    
    def build(self):
        for i, elem in enumerate(self.nums):
            self.point_update(i+1, elem)
    
    def __init__(self, nums: List[int]):
        self.bit = [0] * (len(nums) + 1)
        self.n = len(self.bit)
        self.nums = nums
        self.build()
        
    
    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self.point_update(index + 1, delta)
    
    def prefix_sum(self, i):
        ans = 0
        while(i > 0):
            ans += self.bit[i]
            i = i - self.lowbit(i)
        return ans
    
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum(right+1) - self.prefix_sum(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)