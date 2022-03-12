class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1
        if n < 2:
            return n+1
        k = 1
        index = 0
        for index in range(n+1):
            if index > 1:
                if nums[index] != nums[k-1]:
                    k = k + 1
                    nums[k] = nums[index]
        return k + 1

        