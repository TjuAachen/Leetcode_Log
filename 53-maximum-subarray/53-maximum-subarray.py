class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        sub_array = [0]
        for num in nums:
            total += num
            sub_array.append(total)
        res = max(nums)
        max_sum = -10**9 - 1
        for ind in range(len(sub_array)-1, -1, -1):
            max_sum = max(sub_array[ind],max_sum)
            if max_sum != sub_array[ind]:
                res = max(max_sum - sub_array[ind], res)
        return res
        