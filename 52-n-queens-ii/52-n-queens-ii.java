class Solution {
    private int res = 0;
    private int N;
    public int totalNQueens(int n) {
        LinkedList<String> temp = new LinkedList<>();
        N = n;
        solve(n, temp);
        return res;
    }
    
    public void solve(int n, LinkedList<String> temp){
        if(n == 0){
            res++;
            return;
        }
        StringBuilder curStr = new StringBuilder();
        //create initial string
        for(int i = 0; i < N; i++){
            curStr.append(".");
        }
        for(int j = 0; j < N; j++){
            if (check(temp, N - n, j)){
                curStr.replace(j,j+1, "Q");
                temp.addLast(curStr.toString());
                curStr.replace(j,j+1, ".");
                solve(n - 1, temp);
                temp.pollLast();
            }
        }
    }
    public boolean check(List<String> temp, int row, int col){
        
        //check column
        for(String elem : temp){
            if(elem.charAt(col) == 'Q')return false;      
        }
        //check diagonal
        for(int r = 0; r < row; r++){
            String curRow = temp.get(r);
            int c1 = r - row + col;
            int c2 = row + col - r;
            if(c1 >= 0 && c1 < N && curRow.charAt(c1) == 'Q')return false;
            if(c2 >= 0 && c2 < N && curRow.charAt(c2) == 'Q')return false;            
        }
        return true;
    }
}