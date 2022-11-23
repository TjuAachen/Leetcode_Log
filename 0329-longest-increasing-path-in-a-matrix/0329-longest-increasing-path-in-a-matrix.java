class Solution {
    
    int res = 1;
    int[][] dirs = new int[][]{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    public int longestIncreasingPath(int[][] matrix) {
        Map<Pair<Integer, Integer>, Integer> memo = new HashMap<>();
        Set<Pair<Integer, Integer>> visited = new HashSet<>();
        
        int nRow = matrix.length;
        int nCol = matrix[0].length;
        
        for(int row = 0; row < nRow; row++)
            for(int col = 0; col < nCol; col++){
                Pair<Integer, Integer> key = new Pair(row, col);
                visited.add(key);
                backtracking(matrix, memo, row, col, visited);
                visited.remove(key);
            }
        
        return res;
        
        
    }
    
    public int backtracking(int[][] matrix, Map<Pair<Integer, Integer>, Integer> memo, int x, int y, Set<Pair<Integer, Integer>> visited){
        
        Pair<Integer, Integer> key = new Pair(x, y);
        int curVal = matrix[x][y];
        int nRow = matrix.length;
        int nCol = matrix[0].length;
        
        
        if(memo.containsKey(key))
            return memo.get(key);
        
        int ans = 1;
        
        //nxt step
        for(int[] dir : dirs){
            int newX = x + dir[0];
            int newY = y + dir[1];
            Pair<Integer, Integer> newKey = new Pair(newX, newY);
            
            if(newX >= nRow || newX < 0 || newY >= nCol || newY < 0 || visited.contains(newKey) || matrix[newX][newY] <= curVal){
                continue;
            }
            
            visited.add(newKey);
            ans = Math.max(ans, backtracking(matrix, memo, newX, newY, visited) + 1);
            visited.remove(newKey);
        }
        
        memo.put(key, ans);
        
        res = Math.max(res, ans);
        
        return ans;
        
        
        
        
        
        
    }
}