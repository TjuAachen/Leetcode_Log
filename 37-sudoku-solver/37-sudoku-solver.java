class Solution {
    public void solveSudoku(char[][] board) {
        solve(board);
        return;
    }
    public boolean solve(char[][] board){
        int N = 9;
        
        for(int row = 0; row < N; row++)
            for(int col = 0; col < N; col++){
                if(board[row][col] == '.'){
                    for(int num = 0; num < 9; num++){
                        if(isValidStep(board, row, col, num)){
                            board[row][col] = Integer.toString(num+1).charAt(0);
                            if(solve(board))return true;
                            board[row][col] = '.';
                        }
                        
                    }
                    return false;
                }
            }
        return true;
        
        
    }
    public boolean isValidStep(char[][] board, int row, int col, int num){
        //examine row
        int N = 9;
        char curChar = Integer.toString(num+1).charAt(0);
        for(int i = 0; i < N; i++){
            if (board[row][i] == curChar)return false;
        }
        //examine col
        for(int j = 0; j < N; j++){
            if(board[j][col] == curChar)return false;
        }
        
        
        //examine sub
        for(int m = row/3*3; m < row/3*3+3; m++)
            for(int n = col/3*3; n < col/3*3 + 3; n++){
                if(board[m][n] == curChar)return false;
            }
        return true;
    }
    
    
}
                
            
                    
        