from bisect import *
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        num_heaters = len(heaters)
        record = {}
        ans = 0
        for house in houses:
            pos = bisect_left(heaters, house, 0, num_heaters) - 1
            left = float('inf')
            right = float('inf')
            if pos >= 0:
                left = abs(heaters[pos] - house)
            if pos + 1 < num_heaters:
                right = abs(heaters[pos+1] - house)
            if house in record:
                record[house] = min([record[house],left, right])
            else:
                record[house] = min(left, right)
            ans = max(ans, record[house])
        return ans
            
