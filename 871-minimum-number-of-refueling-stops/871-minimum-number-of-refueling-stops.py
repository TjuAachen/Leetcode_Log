class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        n = len(stations)
        #dp[station][num_stops],
        dp = [[0]*(n+1) for _ in range(n + 1)]
        
        for i in range(n+1):
            dp[i][0] = startFuel
        #stations = [[0, 0]] + stations
        for i in range(1, 1+n):
            for j in range(1, i+1):
                if dp[i-1][j-1] >= stations[i-1][0]:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + stations[i-1][1])
                else:
                    dp[i][j] = dp[i-1][j]

        
        for j in range(n+1):
            if dp[n][j] >= target:
                return j
        return -1
        
                
                
                
                
                
        
            