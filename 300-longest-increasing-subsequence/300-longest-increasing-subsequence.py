from bisect import *
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #intelligently built
        
        res = []
        longest = 0
        for num in nums:
            n = len(res)
            if not res or num > res[-1]:
                res.append(num)
            else:
                i = bisect_left(res, num)
                if 0 <= i < n:
                    res[i] = num
                   # res = res[:i+1]
            longest = max(longest, len(res))
           # print(res)
        return longest