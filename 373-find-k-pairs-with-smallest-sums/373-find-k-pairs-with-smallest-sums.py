from heapq import *
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        heap = []
        for i, num in enumerate(nums2):
            heappush(heap, [num + nums1[0], 0, i])
        n1, n2 = len(nums1), len(nums2)
        while(len(res) < k and heap):
            val, p1, p2 = heappop(heap)
            res.append([nums1[p1], nums2[p2]])
            if p1 + 1 < n1:
                heappush(heap, [nums1[p1+1] + nums2[p2], p1+1, p2])
        return res
            
        