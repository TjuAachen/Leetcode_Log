import random
class Solution:

    def __init__(self, nums: List[int]):
        self.val_index = defaultdict(list)
        
        for i, num in enumerate(nums):
            self.val_index[num].append(i)
        

    def pick(self, target: int) -> int:
        index_array = self.val_index[target]
        
        left, right = 0, len(index_array) - 1
        picked_index = random.randint(left, right)
        
        return index_array[picked_index]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)