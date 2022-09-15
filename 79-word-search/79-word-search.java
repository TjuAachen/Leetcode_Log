class Solution {
    int[][] directions = new int[][]{{1,0}, {-1,0},{0,1},{0,-1}};
    int nrow;
    int ncol;
    int wordLen;
    Set<Pair> visited = new HashSet<>();
    public boolean exist(char[][] board, String word) {
        nrow = board.length;
        ncol = board[0].length;
        wordLen = word.length();
        for(int i = 0; i < nrow; i++)
            for(int j = 0; j < ncol; j++){
                char curChar = board[i][j];
                Pair key = new Pair(i, j);
                if(curChar == word.charAt(0)){
                    visited.add(key);
                    if (dfs(board, i, j, word, 1)) return true;
                    visited.remove(key);
                } 
            }
        return false;
    }
    public boolean dfs(char[][] board, int row, int col, String word, int wordIdx){
        if(wordIdx == wordLen)return true;
        for(int[] direction : directions){
            int x = row + direction[0], y = col + direction[1];
            Pair key = new Pair(x, y);
            if( x < nrow && x >= 0 && y >= 0 && y < ncol && !visited.contains(key) && board[x][y] == word.charAt(wordIdx)){
                visited.add(key);
                if (dfs(board, x, y, word, wordIdx + 1))return true;
                visited.remove(key);
                
            }
        }
        return false;
    }
}