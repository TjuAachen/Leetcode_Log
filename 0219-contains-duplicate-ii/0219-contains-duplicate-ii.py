class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        valPos = defaultdict(list)
        for i, num in enumerate(nums):
            valPos[num].append(i)
        for num, positions in valPos.items():
            minInterval = float('inf')
            for i, position in enumerate(positions):
                if i > 0:
                    minInterval = min(minInterval, position - positions[i - 1])
                    if minInterval <= k:
                        return True
        return False
            
            
            
        