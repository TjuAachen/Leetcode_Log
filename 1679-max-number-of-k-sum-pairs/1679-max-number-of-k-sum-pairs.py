class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i,j = 0, len(nums) - 1
        if k < nums[0] or len(nums) == 1:
            return 0
        count = 0
        while(i < j):
            right = k - nums[i]
            while(j > i and nums[j] > right):
                j = j - 1
            if j > i and nums[j] == right:
                count += 1
                j = j - 1
            i += 1
        return count
        
        