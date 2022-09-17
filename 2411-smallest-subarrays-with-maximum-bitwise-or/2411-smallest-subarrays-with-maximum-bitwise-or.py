import math
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        maximumBit = int(math.log(10**9, 2)) + 1
        seen = [0] * maximumBit
        ans = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(maximumBit + 1):
                if(nums[i] and (nums[i] & (1<<j))):
                    seen[j] = i
            ans[i] = max(1, max(seen) - i + 1)
        return ans
            
        
        
        
        
            