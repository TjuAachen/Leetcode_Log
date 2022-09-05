class Solution {
    public boolean isValidSudoku(char[][] board) {
        //row examination
        boolean isRowValid = isRowColValid(board, true);
        //col examination
        boolean isColValid = isRowColValid(board, false);
        //sub-boxes examination
        boolean isBoxValid = isSubValid(board);
        return isRowValid && isColValid && isBoxValid;
    }
    
    public boolean isRowColValid(char[][] board, boolean isRow){
        int nrow = board.length, ncol = board[0].length;
        boolean isRowValid = true;
        Set<Character> existed = null;
        if(!isRow){
            int temp = nrow;
            nrow = ncol;
            ncol = temp;
        }
        Character val = null;
        for(int row = 0; row < nrow; row++){
            existed = new HashSet<>();
            for(int col = 0; col < ncol; col++){
                if(isRow){
                    val = board[row][col];
                }else{
                    val = board[col][row];
                }
                if(!(Character.isDigit(val)))continue;
                if(existed.contains(val)){
                    isRowValid = false;
                    return isRowValid;
                }
                existed.add(val);
            }
            
        }
        return isRowValid;  
    }
    public boolean isSubValid(char[][] board){
        int nrow = board.length, ncol = board[0].length;
        Set<Character> existed = null;
        boolean ans = true;
        for(int col = 0; col < ncol; col += 3)
            for(int row = 0; row < nrow; row += 3){
                existed = new HashSet<>();
                for(int i = row; i < row + 3; i++)
                    for(int j = col; j < col + 3; j++){
                        if(!(Character.isDigit(board[i][j])))continue;
                        if(existed.contains(board[i][j]))return false;
                        existed.add(board[i][j]);
                    }
            }
        
        return true;
        
    }
    
}