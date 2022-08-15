import random
class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.nums = nums[:]
        self.n = len(nums)
    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        #simulation
        for i in range(self.n):
            choice = random.randint(0, i)
            self.nums[choice], self.nums[i] = self.nums[i], self.nums[choice]
        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()