class Solution {
    public void solve(char[][] board) {
        //@input : 2d matrix
        //@output : convert all O into X
        //@constraints : not convert for O in border, adjacent to an "O" not flipped
        //@edge case: no
        //@breaking down problem:
        //1. dfs search from borders with "O"
        //2. set "O" as "M"
        //3. set "O" as "X"; Set "M" as "O"
        setUnflipped(board);
        int nrow = board.length, ncol = board[0].length;
        for(int row = 0; row < nrow; row++)
            for(int col = 0; col < ncol; col++){
                if(board[row][col] == 'O')board[row][col] = 'X';
                if(board[row][col] == 'M')board[row][col] = 'O';
            }
        
         
        
        
        
    }
    public void setUnflipped(char[][] board){
        int nrow = board.length, ncol = board[0].length;
        
        //first row
        for(int col = 0; col < ncol; col++){
            if(board[0][col] == 'O'){
                dfs(0, col, board);
            }
            if(board[nrow - 1][col] == 'O'){
                dfs(nrow - 1, col, board);
            }
        }
        
        for(int row = 0; row < nrow; row++){
            if(board[row][0] == 'O'){
                dfs(row, 0, board);
            }
            if(board[row][ncol - 1] == 'O'){
                dfs(row, ncol - 1, board);
            }
        }
        
        
        
        
    }
    public void dfs(int row, int col, char[][] board){
        int[][] directions = {{1,0},{0,1},{0,-1},{-1,0}};
        int nrow = board.length, ncol = board[0].length;
        Pair key = new Pair(row, col);
        if(row >= nrow || row < 0 || col >= ncol || col < 0)return;
        if(board[row][col] != 'O')return;
        if(board[row][col] == 'M')return;
        board[row][col] = 'M';
        for( int[] direction : directions){
            int x = row + direction[0], y = col + direction[1];
            dfs(x, y, board);
        }
        
        
        
        
    }
    
    
    
}