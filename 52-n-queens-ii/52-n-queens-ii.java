class Solution {
    private int res = 0;
    private int N;
    public int totalNQueens(int n) {
        N = n;
        solve(n, new HashSet<>(), new HashSet<>(), new HashSet<>());
        return res;
    }
    
    public void solve(int row, Set<Integer> cols, Set<Integer> diagonals, Set<Integer> antiDiagonals){
        if(row == 0){
            res++;
            return;
        }
        for(int col = 0; col < N; col++){
            int curDiagonal = row - col;
            int curAntiDiagonal = row + col;
            if (cols.contains(col) || diagonals.contains(curDiagonal) || antiDiagonals.contains(curAntiDiagonal))continue;
            cols.add(col);
            diagonals.add(curDiagonal);
            antiDiagonals.add(curAntiDiagonal);
            solve(row - 1, cols, diagonals, antiDiagonals);
            cols.remove(col);
            diagonals.remove(curDiagonal);
            antiDiagonals.remove(curAntiDiagonal);
        }



    }
}