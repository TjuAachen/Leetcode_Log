class Solution {
    public void setZeroes(int[][] matrix) {
        int nrow = matrix.length, ncol = matrix[0].length;
        boolean firstCol = false;
        boolean firstRow = false;
        for(int row = 0; row < nrow; row++){
            if(matrix[row][0] == 0)firstCol = true;
        }
        for(int col = 0; col < ncol; col++){
            if(matrix[0][col] == 0)firstRow = true;
        }        
        
        
        
        for(int row = 1; row < nrow; row++)
            for(int col = 1; col < ncol; col++){
                if(matrix[row][col] == 0){
                    matrix[row][0] = 0;
                    matrix[0][col] = 0;
                }
            }
        
        for(int col = 1; col < ncol; col++){
            if(matrix[0][col] == 0){
                for(int row = 1; row < nrow; row++){
                    matrix[row][col] = 0;
                }
            }
        }

        
        for(int row = 1; row < nrow; row++){
            if(matrix[row][0] == 0){
                for(int col = 1; col < ncol; col++){
                    matrix[row][col] = 0;
                }
            }
        }
        
        if(firstCol){
            for(int row = 0; row < nrow; row++)matrix[row][0] = 0;
        }
        if(firstRow){
            for(int col = 0; col < ncol; col++)matrix[0][col] = 0;
        }
        
        //the first row record the col
        
        
        //the first col record the row
        
        
        
    }
}