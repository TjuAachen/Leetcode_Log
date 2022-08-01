class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums) + 1
        self.BIT = [0] * self.n
        self.nums = nums
        self.build()
    #    print(self.BIT)
    #initialize binary indexed tree
    def lowbit(self,num):
        return num&(-num)
    
    def build(self):
        for i in range(1, self.n):
            if i%2 == 1:
                self.BIT[i] = self.nums[i-1]
            else:
                self.BIT[i] = self.prefix_sum(i-1) - self.prefix_sum(i-self.lowbit(i)) + self.nums[i-1]
    def update(self,index, val):
        delta =  val - self.nums[index]
      #  print(self.BIT) 
        self.nums[index] = val
        i = index + 1
        while(i < self.n):
            self.BIT[i] += delta
            i += self.lowbit(i)
      #  print(self.BIT) 
    def prefix_sum(self, index):
        res = 0
        #index += 1
       # print(index,self.BIT)
        while(index > 0):
            res += self.BIT[index]
            index -= self.lowbit(index)
        return res
    
    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix_sum(right + 1) - self.prefix_sum(left)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)