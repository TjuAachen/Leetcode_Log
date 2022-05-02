class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        final = []
        def find(n):
            final.append(res[:])
            for i in range(n,len(nums)):
                if i > n and nums[i] == nums[i-1]:
                    continue
                res.append(nums[i])
                find(i+1)
                res.pop()
        find(0)
        return final