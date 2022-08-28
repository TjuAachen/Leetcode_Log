class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev_max = 0
        cur_max = 0
        count = 0
        for i, num in enumerate(nums):
            if i > prev_max:
                prev_max = cur_max
                count += 1
            cur_max = max(cur_max, num + i)
        return count
        