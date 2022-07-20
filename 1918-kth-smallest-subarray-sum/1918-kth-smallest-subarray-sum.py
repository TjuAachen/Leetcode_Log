from bisect import *
class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        min_val = min(nums)

        max_val = sum(nums)
        
        def count(x):
            left, right = 0, 0
            running_sum = 0
            count = 0
            less, great = 0, float('inf')
            while(right < n):
                running_sum += nums[right]
                while(running_sum >= x):
                    great = min(great, running_sum)
                    running_sum -= nums[left]
                    left += 1
                count += right - left + 1
                right = right + 1
                less = max(less, running_sum)
            return count, less, great
                    
                
            
            
        
        
        left, right = min_val, max_val
        while(left <= right):
            mid = left + (right - left) // 2
            less_than_mid, less, great = count(mid)
         
            if less_than_mid == k - 1:
                return great
            elif less_than_mid < k - 1:
                left = mid + 1
            else:
                right = mid - 1
        if less_than_mid < k - 1:
            return great
        else:
            return less


        
        