class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        final = []
        res = []
        n = len(nums)
        def subset(start):
            final.append(res[:])
            for j in range(start,n):
                res.append(nums[j])
                subset(j+1)
                res.pop()
        subset(0)
        return final
        