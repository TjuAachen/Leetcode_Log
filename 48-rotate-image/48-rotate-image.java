class Solution {
    public void rotate(int[][] matrix) {
        //transpose first
        int nrow = matrix.length, ncol = matrix[0].length;
        
        for(int row = 0; row < nrow; row++)
            for(int col = 0; col < ncol; col++){
                if (row <= col) continue;
                matrix[row][col] = matrix[row][col] ^ matrix[col][row];
                matrix[col][row] = matrix[row][col] ^ matrix[col][row];
                matrix[row][col] = matrix[row][col] ^ matrix[col][row];
                
            }

        //exchange values of i and ncol - i
        for (int newCol = 0; newCol < ncol/2; newCol++)
            for(int newRow = 0; newRow < nrow; newRow++){
                int other_newCol = ncol - 1 - newCol;
                int temp = matrix[newRow][other_newCol];
                matrix[newRow][other_newCol] = matrix[newRow][newCol];
                matrix[newRow][newCol] = temp;
            }
        
        
        
    }
}