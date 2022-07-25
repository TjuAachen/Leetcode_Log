import random
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        #partition function
        def partition(nums, left, right):
            pivot_index = random.randint(left, right)
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            pivot = nums[right]
            j = left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    j = j + 1
            #post processing
            nums[right], nums[j] = nums[j], nums[right]
            return j
        
        
        #quick select find the median
        def find_median():
            left, right = 0, n - 1
            expected = (n+1) // 2 - 1
            while(left <= right):
                mid = partition(nums, left, right)
                if mid == expected:
                    return mid
                elif mid < expected:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        #transfer the address
        def transfer(i):
            return (2 * i + 1)%(n | 1)
        
        #three way partition
        mid_index = find_median()
        median = nums[mid_index]
        i, j, k = 0, 0, n - 1
      #  print(mid_index, nums)
        while(j <= k):
            new_i, new_j, new_k = transfer(i), transfer(j), transfer(k)
            if nums[new_j] > median:
                nums[new_j], nums[new_i] = nums[new_i], nums[new_j]
                j += 1
                i += 1
            elif nums[new_j] < median:
                nums[new_k], nums[new_j] = nums[new_j], nums[new_k]
                k -= 1
            else:
                j += 1
          #  print(nums, nums[new_j], median)