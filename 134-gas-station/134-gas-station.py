class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, n = 0, len(gas) - 1
        visited = dict()
        while(len(visited) <= n):
            cur = 0
            i = start
            while(cur + gas[i] >= cost[i]):
                visited[i] = 1
                cur += gas[i] - cost[i]
                i += 1
                i = i%(n+1)
                if i == start:
                    return start
            visited[i] = 1
            start = i + 1
        return -1
            
                
                