class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        record = defaultdict(int)
        max_res = 0
        for num in nums:
            if num in record:
                continue
            left, right = 0, 0
            if num - 1 in record:
                left = record[num - 1]
            if num + 1 in record:
                right = record[num + 1]
            if num not in record:
                record[num] = left + right + 1
            record[num - left] = record[num]
            record[num + right] = record[num]
            max_res = max(max_res, record[num])
        return max_res