from bisect import *
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        num_heaters = len(heaters)
        ans = 0
        for house in houses:
            pos = bisect_left(heaters, house, 0, num_heaters) - 1
            left = float('inf')
            right = float('inf')
            if pos >= 0:
                left = abs(heaters[pos] - house)
            if pos + 1 < num_heaters:
                right = abs(heaters[pos+1] - house)
            ans = max(ans,  min(left, right))
        return ans
            
