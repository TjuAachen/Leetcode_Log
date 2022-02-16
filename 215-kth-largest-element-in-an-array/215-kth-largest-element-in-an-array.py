import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums, k):
            n = len(nums)
            pivot=random.randint(0, n-1)
            nums[-1], nums[pivot] = nums[pivot], nums[-1]
            j = 0
            for i in range(len(nums)-1):
                if nums[i] <= nums[-1]:
                    nums[i], nums[j] = nums[j], nums[i]
                    j = j + 1
            if j <n- k :
                return partition(nums[j:len(nums)-1],k)
            elif j >n- k:
                k = j - n + k 
                return partition(nums[:j],k)
            else:
                return nums[-1]
        return partition(nums, k)
                
            
            