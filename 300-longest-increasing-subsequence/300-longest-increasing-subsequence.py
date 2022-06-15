class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        sub = []
        for ind, num in enumerate(nums):
            if not sub or num > sub[-1]:
                sub.append(num)
            else:
                pos = bisect_left(sub, num)
                sub[pos] = num
        return len(sub)
                