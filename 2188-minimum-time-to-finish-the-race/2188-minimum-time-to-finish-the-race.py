from math import *
class Solution(object):
    def minimumFinishTime(self, tires, changeTime, numLaps):
        """
        :type tires: List[List[int]]
        :type changeTime: int
        :type numLaps: int
        :rtype: int
        """
        #after 17 laps, must change the tire
        dp = [float('inf') for _ in range(numLaps + 1)]
        dp[0] = 0
        max_lap = min(17,numLaps)
        for f, r in tires:
            for i in range(1, max_lap+1):
                dp[i] = min(dp[i], f*(1-r**i)//(1-r))
        for i in range(1, numLaps + 1):
            #not change tire
            #change tire
            for j in range(1,i):
                dp[i] = min(dp[i], dp[j] + changeTime + dp[i-j])
        print(dp)
        return dp[-1]
                