class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        #find all x,y of houses of friends
        nrow, ncol = len(grid), len(grid[0])
        house_x = defaultdict(int)
        house_y = defaultdict(int)
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 1:
                    house_x[i] += 1
                    house_y[j] += 1
        def distance(record):
            ans = float('inf')
            for key in record.keys():
                loc = key
                temp = 0
                for val, num in record.items():
                    temp += abs(val-loc) * num
                ans = min(temp, ans)
            return ans
        min_x = distance(house_x)
        min_y = distance(house_y)
        return min_x + min_y
                    
        