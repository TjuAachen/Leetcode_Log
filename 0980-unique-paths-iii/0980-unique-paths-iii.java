class Solution {
    int startingVal = 1;
    int endingVal = 2;
    int emptyVal = 0;
    int obstacleVal = -1;
    int nrow;
    int ncol;
    int obstacleNum = 0;
    int[][] directions = {{1, 0}, {-1, 0}, {0, -1}, {0, 1}};
    public int uniquePathsIII(int[][] grid) {
        
        Set<Pair<Integer, Integer>> visited = new HashSet<>();
        
        // find the starting
        nrow = grid.length;
        ncol = grid[0].length;
        int ans = 0;
        int startingX = -1;
        int startingY = -1;
        for (int row = 0; row < nrow; row++)
            for (int col = 0; col < ncol; col++){
                if (grid[row][col] == startingVal){
                    startingX = row;
                    startingY = col;
                }else if (grid[row][col] == obstacleVal){
                    this.obstacleNum += 1;
                }
            }
        if (startingX == -1 && startingY == -1)
            return 0;
        
        return numOfPaths(visited, startingX, startingY, grid);
        
        
    }
    
    public int numOfPaths(Set<Pair<Integer, Integer>> visited, int x, int y, int[][] grid) {
       // System.out.printf("%d %d\n", x, y);
        int curVal = grid[x][y];
        if (curVal == obstacleVal)
            return 0;
        if (curVal == endingVal){
            if (visited.size() == nrow * ncol - 1 - this.obstacleNum)
                return 1;
            return 0;
        }
        int ans = 0;
        Pair<Integer, Integer> key = new Pair(x, y);
        visited.add(key);
        for (int[] direction : directions) {
            int nxtX = direction[0] + x;
            int nxtY = direction[1] + y;
            Pair<Integer, Integer> newKey = new Pair<>(nxtX, nxtY);
            if (visited.contains(newKey))
                continue;
            if (nxtX < nrow && nxtX >= 0 && nxtY < ncol && nxtY >= 0){
            //    visited.add(newKey);
                ans += numOfPaths(visited, nxtX, nxtY, grid);
              //  visited.remove(newKey);
            }
        }
        visited.remove(key);
        
        return ans;
    }
}