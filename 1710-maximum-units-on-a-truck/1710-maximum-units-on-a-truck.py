class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: (-x[1], x[0]))
        
        ans = 0
        for boxNum, unit in boxTypes:
            if truckSize == 0:
                return ans
            if boxNum <= truckSize:
                ans += boxNum * unit
                truckSize -= boxNum
            else:
                ans += truckSize * unit
                truckSize = 0
        return ans
        