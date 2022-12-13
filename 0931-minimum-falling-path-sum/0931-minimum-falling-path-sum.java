class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int nrow = matrix.length;
        int ncol = matrix[0].length;
        
        int[][] fallingPathSum = new int[nrow][ncol];
        
        int ans = Integer.MAX_VALUE;
        //the first row
        for (int row = 0; row < nrow; row++)
            for (int col = 0; col < ncol; col++){
                if (row == 0){
                    fallingPathSum[row][col] = matrix[row][col];
                }else{
                    fallingPathSum[row][col] = Integer.MAX_VALUE;
                    
                    fallingPathSum[row][col] = Math.min(fallingPathSum[row][col], matrix[row][col] + fallingPathSum[row - 1][col]);
                    
                    if (col >= 1)
                        fallingPathSum[row][col] = Math.min(fallingPathSum[row][col], matrix[row][col] + fallingPathSum[row - 1][col - 1]);
                    
                    if (col < ncol - 1)
                        fallingPathSum[row][col] = Math.min(fallingPathSum[row][col], matrix[row][col] + fallingPathSum[row - 1][col + 1]);
                }
                
                if (row == nrow - 1)
                    ans = Math.min(fallingPathSum[row][col], ans);
                
            }
        
        return ans;
    }
}