from sortedcontainers import SortedList
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        i = n - 2
        after_list = SortedList()
        after_list.add(nums[-1])
        ans = 0
        res = [0]
        while(i >= 0):
            cur = nums[i]
            index = after_list.bisect_left(cur)
            ans = index
            after_list.add(cur)
            i = i - 1
            res.append(ans)
        return res[::-1]
        
        