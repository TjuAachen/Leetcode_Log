from sortedcontainers import SortedList
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
      #  index = []
        n = len(nums)
        prefix = [0] * (n + 1)
        
        for i, num in enumerate(nums):
            prefix[i+1] = prefix[i] + num
        #print(prefix, index)
        i = 1
        sorted_prefix = SortedList()
        sorted_prefix.add(0)
        count = 0
      #  print(prefix)
        while(i < n + 1):
            left, right = prefix[i] - upper, prefix[i] - lower
            #print(left, right, sorted_prefix)
            left_index = sorted_prefix.bisect_left(left)
            right_index = sorted_prefix.bisect(right) - 1
           # print(left_index, right_index, left, right, sorted_prefix)
            count += right_index - left_index + 1

            sorted_prefix.add(prefix[i])
            i += 1
        return count
        
        
        
        