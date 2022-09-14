class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int nrow = matrix.length, ncol = matrix[0].length;
        int row = 0, col = ncol - 1;
        int cur = 0;
        while(row >= 0 && row < nrow && col >= 0 && col < ncol){
            cur = matrix[row][col];
            if(cur == target) return true;
            if(cur > target)col-=1;
            if(cur < target)row+=1;
        }
        return false;
    }
}