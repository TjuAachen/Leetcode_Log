class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        if not houses or not heaters:
            return -1
        
        houses = sorted(houses)
        heaters = sorted(heaters)
        
        n, m = len(houses), len(heaters)
        j = 0
        mini = float('-inf')
        for i in range(n):
            while j + 1 < m and abs(houses[i] - heaters[j]) >= abs(houses[i] - heaters[j + 1]):
                j += 1
           # print(abs(houses[i] - heaters[j]))
            mini = max(mini, abs(houses[i] - heaters[j]))
          #  print(mini)
        
        return mini
            
