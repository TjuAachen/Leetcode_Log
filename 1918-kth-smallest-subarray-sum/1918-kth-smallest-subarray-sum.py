from bisect import *
class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        def numOfSubArrBelow(target):
            count = 0
            total = 0
            lptr = 0
            for rptr in range(len(nums)):
                total += nums[rptr]
                while total > target:
                    total -= nums[lptr]
                    lptr += 1
                count += (rptr - lptr + 1)
            return count
        
        n, low, high = len(nums), min(nums), sum(nums)
        while low<=high:
            mid = (low+high)//2
            if numOfSubArrBelow(mid)>=k:
                high = mid-1
            else:
                low = mid+1
                
        return low


        
        