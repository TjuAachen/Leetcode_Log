class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        #calculate from the target
        count = 0
        while(maxDoubles > 0 and target > 1):
            if target % 2 == 0:
                target = target // 2
                maxDoubles = maxDoubles - 1
            else:
                target = target - 1
            count += 1
        return count + target - 1