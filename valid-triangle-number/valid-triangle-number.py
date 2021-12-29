class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        def twoSumLarger(nums, end, target):
            left, right = 0, end
            res = 0
            while(left < right):
                sum_ij = nums[left] + nums[right]
                if sum_ij <= target :
                    left = left + 1
                else:
                    res += right - left 
                    right = right - 1
            return res
        nums.sort()
        final = 0
        for i in range(len(nums)-1,1,-1):
            res = twoSumLarger(nums, i-1, nums[i])
            final += res
        return final
            