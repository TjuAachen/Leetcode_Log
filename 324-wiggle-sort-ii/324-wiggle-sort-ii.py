import random
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        #sort the nums first
        nums.sort()
        temp = []
        
        mid = n // 2
        
        less_part = nums[:mid+n%2]
        larger_part = nums[mid+n%2:]
       # print(less_part, larger_part)
        less_pointer, larger_pointer = len(less_part) - 1, len(larger_part) - 1
        cur_index = 0
        while(less_pointer >= 0 or larger_pointer >= 0):
            if cur_index % 2 == 0:
                temp.append(less_part[less_pointer])
                less_pointer -= 1
            else:
                temp.append(larger_part[larger_pointer])
                larger_pointer -= 1
            cur_index += 1
           # print(temp, less_part, larger_part)
        nums[:] = temp[:]
        return nums