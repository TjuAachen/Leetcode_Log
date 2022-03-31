class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        f = [0] * len(nums)
        f[0] = nums[0]
        for ind, num in enumerate(nums):
            if ind > 0:
                f[ind] = max(f[ind-1]+num,num)
        return max(f)
        