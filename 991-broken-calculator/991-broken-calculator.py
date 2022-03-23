class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        time = 0
        prev = target
        while(target > startValue):
            time += 1
            if target%2 == 0:
                target = target // 2
            else:
                target = target + 1
        return time +startValue - target
                
        