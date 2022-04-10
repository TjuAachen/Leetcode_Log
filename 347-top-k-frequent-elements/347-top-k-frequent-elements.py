import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == k:
            return nums
        record = dict()
        for num in nums:
            if num not in record:
                record[num] = 1
            else:
                record[num] += 1
        return heapq.nlargest(k, record.keys(),key=record.get)
            
        